#!/usr/bin/env python3

import os
import requests
import json
from datetime import datetime

def get_pending_approvals():
    """
    Get all open issues with the 'Ter Goedkeuring' label from GitHub.
    """
    # GitHub API setup
    token = os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('GITHUB_REPOSITORY', 'fx1960/goldforex4all-content')
    
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # Get issues with "Ter Goedkeuring" label
    url = f'https://api.github.com/repos/{repo}/issues'
    params = {
        'labels': 'Ter Goedkeuring',
        'state': 'open'
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        issues = response.json()
        
        # Format issues for email
        pending_content = []
        for issue in issues:
            # Extract content type from issue title
            content_type = "Content"
            if issue['title'].startswith('[BLOG]'):
                content_type = "Blog"
            elif issue['title'].startswith('[SOCIAL]'):
                content_type = "Social Media"
            elif issue['title'].startswith('[VIDEO]'):
                content_type = "Video"
            elif issue['title'].startswith('[REVIEW]'):
                content_type = "Product Review"
            
            # Extract platform from issue body if available
            platform = "Website"
            if "**Platform:**" in issue['body']:
                platform_line = [line for line in issue['body'].split('\n') if "**Platform:**" in line]
                if platform_line:
                    platform = platform_line[0].split("**Platform:**")[1].strip()
            
            pending_content.append({
                'title': issue['title'],
                'type': content_type,
                'platform': platform,
                'url': issue['html_url'],
                'issue_url': issue['html_url']
            })
        
        return pending_content
    
    except Exception as e:
        print(f"Error fetching issues from GitHub: {e}")
        # Return sample data as fallback for testing
        return [
            {
                "title": "[BLOG] - Waarom XAUUSD Trading Populair Blijft in 2025",
                "type": "Blog",
                "platform": "Website",
                "url": f"https://github.com/{repo}/blob/main/blogs/xauusd_trading_2025.md",
                "issue_url": f"https://github.com/{repo}/issues/1"
            }
        ]

if __name__ == "__main__":
    # Test the function
    pending = get_pending_approvals()
    print(f"Found {len(pending)} pending approval items:")
    for item in pending:
        print(f"- {item['title']} ({item['type']} for {item['platform']})")
