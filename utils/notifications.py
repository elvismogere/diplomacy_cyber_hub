import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG, NOTIFICATION_CONFIG

class NotificationManager:
    @staticmethod
    def send_email(recipient: str, subject: str, body: str) -> bool:
        """Send email notification"""
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_CONFIG['sender_email']
            msg['To'] = recipient
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'html'))

            server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
            server.starttls()
            server.login(EMAIL_CONFIG['smtp_username'], EMAIL_CONFIG['smtp_password'])
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Email sending failed: {e}")
            return False

    @staticmethod
    def send_alert(user_id: str, alert_type: str, message: str, priority: str):
        """Send alert through configured channels"""
        channels = NOTIFICATION_CONFIG['channels']
        
        if priority in channels['email']['priority']:
            # Send email alert
            pass
        
        if priority in channels['sms']['priority']:
            # Send SMS alert
            pass
        
        if priority in channels['in_app']['priority']:
            # Send in-app notification
            pass

    @staticmethod
    def format_notification(template_name: str, context: dict) -> str:
        """Format notification using template"""
        templates = {
            'security_alert': """
                <h2>Security Alert</h2>
                <p>Priority: {priority}</p>
                <p>{message}</p>
                <p>Time: {timestamp}</p>
            """,
            'system_notification': """
                <h2>System Notification</h2>
                <p>{message}</p>
                <p>Time: {timestamp}</p>
            """
        }
        
        template = templates.get(template_name, templates['system_notification'])
        return template.format(**context)
