# GitHub Workflow Configuratie

Dit document beschrijft de GitHub Actions workflows die worden gebruikt voor het autonome contentgoedkeuringssysteem.

## Wekelijkse Notificatie Workflow

Deze workflow stuurt elke maandag een e-mail naar de eigenaar met een overzicht van content die goedkeuring nodig heeft.

```yaml
name: Weekly Approval Notification

on:
  schedule:
    # Elke maandag om 9:00 UTC
    - cron: '0 9 * * 1'
  workflow_dispatch:
    # Handmatig kunnen triggeren indien nodig

jobs:
  send-notification:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests
      
      - name: Get pending approvals
        id: get-approvals
        run: |
          python .github/scripts/get_pending_approvals.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Send email notification
        if: steps.get-approvals.outputs.has_pending == 'true'
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: ${{ secrets.MAIL_SERVER }}
          server_port: ${{ secrets.MAIL_PORT }}
          username: ${{ secrets.MAIL_USERNAME }}
          password: ${{ secrets.MAIL_PASSWORD }}
          subject: "GoldForex4All - Content Goedkeuring Nodig"
          body: ${{ steps.get-approvals.outputs.email_body }}
          to: info@goldforex4all.eu
          from: GoldForex4All Content System
```

## Automatische Issue Labeling Workflow

Deze workflow voegt automatisch labels toe aan nieuwe Issues op basis van de titel en inhoud.

```yaml
name: Auto Label Issues

on:
  issues:
    types: [opened, edited]

jobs:
  auto-label:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
      
      - name: Auto-label issue
        run: |
          python .github/scripts/auto_label_issues.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ISSUE_NUMBER: ${{ github.event.issue.number }}
```

## Content Publicatie Notificatie Workflow

Deze workflow stuurt een notificatie wanneer content is gepubliceerd.

```yaml
name: Content Publication Notification

on:
  issues:
    types: [labeled]

jobs:
  notify-publication:
    if: github.event.label.name == 'Gepubliceerd'
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
      
      - name: Send publication notification
        run: |
          python .github/scripts/notify_publication.py
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          ISSUE_NUMBER: ${{ github.event.issue.number }}
```

## Python Scripts

De bovenstaande workflows maken gebruik van Python scripts die in de `.github/scripts/` map moeten worden geplaatst:

### get_pending_approvals.py

```python
import os
import json
import requests

# GitHub API setup
token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
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
response = requests.get(url, headers=headers, params=params)
issues = response.json()

has_pending = len(issues) > 0

# Create email body
if has_pending:
    email_body = f"Beste,\n\nEr {'is' if len(issues) == 1 else 'zijn'} {len(issues)} content item{'s' if len(issues) > 1 else ''} die op uw goedkeuring {'wacht' if len(issues) == 1 else 'wachten'}:\n\n"
    
    for issue in issues:
        email_body += f"- {issue['title']}: {issue['html_url']}\n"
    
    email_body += "\nU kunt deze items beoordelen door op de links te klikken en te reageren met 'GOEDGEKEURD' of 'REVISIE NODIG'.\n\n"
    email_body += "Met vriendelijke groet,\nHet GoldForex4All Content Systeem"
else:
    email_body = "Er zijn momenteel geen items die op goedkeuring wachten."

# Set outputs
print(f"::set-output name=has_pending::{str(has_pending).lower()}")
print(f"::set-output name=email_body::{email_body}")
```

### auto_label_issues.py

```python
import os
import json
import requests

# GitHub API setup
token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
issue_number = os.environ['ISSUE_NUMBER']
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Get issue details
url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
response = requests.get(url, headers=headers)
issue = response.json()

# Determine labels based on title and body
labels = []

# Check if title starts with content type
title = issue['title'].lower()
if title.startswith('[blog]'):
    labels.append('Blog')
elif title.startswith('[social]'):
    labels.append('Social Media')
elif title.startswith('[video]'):
    labels.append('Video')
elif title.startswith('[review]'):
    labels.append('Product Review')

# Add "Ter Goedkeuring" label by default for new issues
if 'pull_request' not in issue:
    labels.append('Ter Goedkeuring')

# Add labels to the issue
if labels:
    url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/labels'
    data = {'labels': labels}
    requests.post(url, headers=headers, json=data)
```

### notify_publication.py

```python
import os
import json
import requests

# GitHub API setup
token = os.environ['GITHUB_TOKEN']
repo = os.environ['GITHUB_REPOSITORY']
issue_number = os.environ['ISSUE_NUMBER']
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Get issue details
url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
response = requests.get(url, headers=headers)
issue = response.json()

# Add comment to the issue
url = f'https://api.github.com/repos/{repo}/issues/{issue_number}/comments'
comment = {
    'body': f"🎉 Deze content is nu gepubliceerd! Het issue wordt automatisch gesloten.\n\nBedankt voor uw bijdrage aan GoldForex4All."
}
requests.post(url, headers=headers, json=comment)

# Close the issue
url = f'https://api.github.com/repos/{repo}/issues/{issue_number}'
data = {'state': 'closed'}
requests.patch(url, headers=headers, json=data)
```
