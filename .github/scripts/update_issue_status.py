#!/usr/bin/env python3

import os
import requests
import json
from datetime import datetime

def update_issue_status(issue_number, new_status):
    """
    Update the status of an issue based on a comment.
    
    Args:
        issue_number: The GitHub issue number
        new_status: Either "GOEDGEKEURD" or "REVISIE NODIG"
    """
    # GitHub API setup
    token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPOSITORY', 'fx1960/goldforex4all-content')
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Add a comment confirming the status change
    comment_url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
    
    if new_status == "GOEDGEKEURD":
        # Add "Goedgekeurd" label and remove "Ter Goedkeuring" label
        labels_url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/labels'
        labels_data = {
            'labels': ['Goedgekeurd'],
            'remove': ['Ter Goedkeuring']
        }
        
        try:
            # Update labels
            response = requests.post(labels_url, headers=headers, json=labels_data)
            response.raise_for_status()
            
            # Add confirmation comment
            comment_data = {
                'body': '✅ **Content goedgekeurd!**\n\nDeze content is goedgekeurd en zal worden gepubliceerd volgens planning. Bedankt voor uw snelle reactie.'
            }
            response = requests.post(comment_url, headers=headers, json=comment_data)
            response.raise_for_status()
            
            print(f"Issue #{issue_number} marked as approved")
            return True
            
        except Exception as e:
            print(f"Error updating issue #{issue_number}: {e}")
            return False
            
    elif new_status == "REVISIE NODIG":
        # Add "Revisie Nodig" label and remove "Ter Goedkeuring" label
        labels_url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/labels'
        labels_data = {
            'labels': ['Revisie Nodig'],
            'remove': ['Ter Goedkeuring']
        }
        
        try:
            # Update labels
            response = requests.post(labels_url, headers=headers, json=labels_data)
            response.raise_for_status()
            
            # Add confirmation comment
            comment_data = {
                'body': '🔄 **Revisie nodig**\n\nDeze content heeft revisie nodig voordat deze kan worden gepubliceerd. We zullen de wijzigingen doorvoeren en opnieuw ter goedkeuring voorleggen.'
            }
            response = requests.post(comment_url, headers=headers, json=comment_data)
            response.raise_for_status()
            
            print(f"Issue #{issue_number} marked as needing revision")
            return True
            
        except Exception as e:
            print(f"Error updating issue #{issue_number}: {e}")
            return False
    
    else:
        print(f"Unknown status: {new_status}")
        return False

if __name__ == "__main__":
    # Test the function (uncomment to test)
    # update_issue_status(1, "GOEDGEKEURD")
    pass
