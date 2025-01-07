import os
from pathlib import Path
from datetime import timedelta

# Create necessary directories
settings_dir = Path("settings")
settings_dir.mkdir(exist_ok=True)

# File paths
SETTINGS_FILE = settings_dir / "user_settings.json"
DATABASE_FILE = "users.db"

# Application Configuration
APP_CONFIG = {
    "name": "DiploCyber Hub",
    "version": "1.0.0",
    "description": "Secure Intelligence Platform for IGOs",
    "organization": "UN Agencies and IGOs in Kenya",
}

# Default settings
DEFAULT_SETTINGS = {
    "theme": "dark",
    "language": "en",
    "notifications_enabled": True,
    "session_timeout": 30,
    "date_format": "%Y-%m-%d",
    "time_format": "%H:%M:%S",
    "timezone": "Africa/Nairobi"
}

# Security Configuration
SECURITY_CONFIG = {
    "session_duration": timedelta(hours=8),
    "password_min_length": 8,
    "password_require_special": True,
    "password_require_numbers": True,
    "max_login_attempts": 3,
    "lockout_duration": timedelta(minutes=15),
    "mfa_enabled": False,
    "allowed_domains": ["*.un.org", "*.go.ke", "*.int"],
}

# Database Configuration
DB_CONFIG = {
    "type": "sqlite",
    "name": DATABASE_FILE,
    "backup_enabled": True,
    "backup_frequency": "daily",
    "max_connections": 20,
}

# Email Configuration
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "use_tls": True,
    "sender_email": "notifications@diplocyber.com",
    "reply_to": "support@diplocyber.com",
}

# Notification Settings
NOTIFICATION_CONFIG = {
    "channels": {
        "email": {
            "enabled": True,
            "priority": ["critical", "high"],
        },
        "in_app": {
            "enabled": True,
            "priority": ["critical", "high", "medium", "low"],
        },
    },
    "quiet_hours": {
        "enabled": False,
        "start": "23:00",
        "end": "07:00",
    },
}

# UI Configuration
UI_CONFIG = {
    "theme": {
        "dark": {
            "background": "#1E1E1E",
            "text": "#FFFFFF",
            "primary": "#90EE90",
            "secondary": "#FFD700",
            "accent": "#404040",
        },
        "light": {
            "background": "#FFFFFF",
            "text": "#000000",
            "primary": "#90EE90",
            "secondary": "#FFD700",
            "accent": "#F0F0F0",
        }
    },
    "fonts": {
        "primary": "Helvetica Neue",
        "secondary": "Arial",
        "monospace": "Courier New",
    },
    "animations": {
        "enabled": True,
        "duration": 300,
    }
}

# Feature Flags
FEATURES = {
    "mfa": False,
    "api_access": False,
    "export": True,
    "advanced_analytics": True,
    "threat_intelligence": True,
}

# API Configuration
API_CONFIG = {
    "version": "v1",
    "base_url": "https://api.diplocyber.com",
    "timeout": 30,
    "rate_limit": 100,
}

# Logging Configuration
LOG_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/diplocyber.log",
    "max_size": 10485760,  # 10MB
    "backup_count": 5,
}
