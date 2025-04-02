#!/usr/bin/env python3

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Email configuration
SENDER_EMAIL = "notifications@goldforex4all.eu"  # Replace with actual sender email
RECEIVER_EMAIL = "info@goldforex4all.eu"
SMTP_SERVER = "smtp.example.com"  # Replace with actual SMTP server
SMTP_PORT = 587
SMTP_USERNAME = "username"  # Replace with actual SMTP username
SMTP_PASSWORD = "password"  # Replace with actual SMTP password

def get_pending_content():
    """
    Simulate getting pending content that needs approval.
    In a real implementation, this would query the GitHub API.
    """
    # This is a placeholder. In production, this would fetch actual data from GitHub
    pending_content = [
        {
            "title": "[BLOG] - Waarom XAUUSD Trading Populair Blijft in 2025",
            "type": "Blog",
            "platform": "Website",
            "url": "https://github.com/fx1960/goldforex4all-content/blob/main/blogs/xauusd_trading_2025.md",
            "issue_url": "https://github.com/fx1960/goldforex4all-content/issues/1"
        },
        {
            "title": "[SOCIAL] - 5 XAUUSD Trading Tips voor Beginners",
            "type": "Social Media",
            "platform": "Instagram",
            "url": "https://github.com/fx1960/goldforex4all-content/blob/main/social_media/instagram_trading_tips.md",
            "issue_url": "https://github.com/fx1960/goldforex4all-content/issues/2"
        }
    ]
    return pending_content

def create_email_content(pending_content):
    """
    Create the email content with the list of pending content for approval.
    """
    # Get current date
    current_date = datetime.now().strftime("%d-%m-%Y")
    
    # Create email subject
    subject = f"GoldForex4All - Wekelijkse Content Goedkeuring ({current_date})"
    
    # Create email body
    body = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                padding: 20px;
            }}
            h1 {{
                color: #0066cc;
                border-bottom: 1px solid #ddd;
                padding-bottom: 10px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                padding: 12px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            .button {{
                display: inline-block;
                background-color: #0066cc;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                margin-top: 20px;
            }}
            .footer {{
                margin-top: 30px;
                font-size: 12px;
                color: #777;
                border-top: 1px solid #ddd;
                padding-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>GoldForex4All Wekelijkse Content Goedkeuring</h1>
            <p>Beste,</p>
            <p>Er {'is' if len(pending_content) == 1 else 'zijn'} {len(pending_content)} content item{'s' if len(pending_content) > 1 else ''} die op uw goedkeuring {'wacht' if len(pending_content) == 1 else 'wachten'}.</p>
            
            <table>
                <tr>
                    <th>Titel</th>
                    <th>Type</th>
                    <th>Platform</th>
                    <th>Actie</th>
                </tr>
    """
    
    # Add each pending content item to the table
    for item in pending_content:
        body += f"""
                <tr>
                    <td>{item['title']}</td>
                    <td>{item['type']}</td>
                    <td>{item['platform']}</td>
                    <td><a href="{item['issue_url']}" style="color: #0066cc;">Bekijken</a></td>
                </tr>
        """
    
    # Complete the email body
    body += f"""
            </table>
            
            <p>U kunt deze items beoordelen door op de "Bekijken" links te klikken. Voor elk item kunt u reageren met:</p>
            <ul>
                <li><strong>GOEDGEKEURD</strong> - als de content direct gepubliceerd kan worden</li>
                <li><strong>REVISIE NODIG</strong> - als er wijzigingen nodig zijn (voeg specifieke feedback toe)</li>
            </ul>
            
            <a href="https://github.com/fx1960/goldforex4all-content/issues" class="button">Alle Items Bekijken</a>
            
            <div class="footer">
                <p>Dit is een geautomatiseerd bericht van het GoldForex4All Content Systeem.</p>
                <p>© {datetime.now().year} GoldForex4All</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return subject, body

def send_email(subject, body):
    """
    Send the email with the pending content for approval.
    """
    # Create message
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    
    # Attach HTML content
    html_part = MIMEText(body, 'html')
    message.attach(html_part)
    
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        
        # Send email
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
        
        print(f"Email sent successfully to {RECEIVER_EMAIL}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def main():
    """
    Main function to run the email notification script.
    """
    # Get pending content
    pending_content = get_pending_content()
    
    # If there's pending content, create and send email
    if pending_content:
        subject, body = create_email_content(pending_content)
        send_email(subject, body)
    else:
        print("No pending content found. No email sent.")

if __name__ == "__main__":
    main()
