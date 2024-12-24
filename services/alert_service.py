from typing import List, Optional
from models import SecurityAlert
from utils.notifications import NotificationManager
from utils.logger import Logger

logger = Logger()
notifications = NotificationManager()

class AlertService:
    @staticmethod
    async def create_alert(alert_data: dict) -> SecurityAlert:
        """Create and process security alert"""
        try:
            alert = SecurityAlert(**alert_data)
            
            # Store alert
            # Implementation needed
            
            # Send notifications
            await AlertService._send_alert_notifications(alert)
            
            return alert
        except Exception as e:
            logger.log_error(str(e), "ALERT_SERVICE")
            raise

    @staticmethod
    async def get_alerts(
        organization_id: str,
        status: Optional[str] = None
    ) -> List[SecurityAlert]:
        """Retrieve security alerts"""
        try:
            # Implement alert retrieval logic
            return []
        except Exception as e:
            logger.log_error(str(e), "ALERT_SERVICE")
            raise

    @staticmethod
    async def _send_alert_notifications(alert: SecurityAlert):
        """Send alert notifications through configured channels"""
        try:
            notification_data = {
                'title': alert.title,
                'description': alert.description,
                'severity': alert.threat_level,
                'timestamp': alert.created_at
            }
            
            await notifications.send_alert(
                alert_type="security_alert",
                data=notification_data,
                priority=alert.threat_level
            )
        except Exception as e:
            logger.log_error(str(e), "ALERT_SERVICE")
            raise
