import logging
from datetime import datetime
from config import MONITORING_CONFIG

class Logger:
    def __init__(self):
        # Configure logging
        logging.basicConfig(
            level=MONITORING_CONFIG['log_level'],
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            filename='logs/diplocyber.log'
        )
        self.logger = logging.getLogger('DiploCyberHub')

    def log_activity(self, user_id: str, action: str, details: dict):
        """Log user activity"""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_id': user_id,
            'action': action,
            'details': details
        }
        self.logger.info(str(log_entry))

    def log_error(self, error_message: str, error_type: str, stack_trace: str = None):
        """Log error information"""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'error_type': error_type,
            'message': error_message,
            'stack_trace': stack_trace
        }
        self.logger.error(str(log_entry))

    def log_security_event(self, event_type: str, severity: str, details: dict):
        """Log security-related events"""
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'severity': severity,
            'details': details
        }
        self.logger.warning(str(log_entry))
