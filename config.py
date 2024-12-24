import os
from datetime import timedelta

# Application Configuration
APP_CONFIG = {
    "name": "DiploCyber Hub",
    "version": "1.0.0",
    "description": "Secure Intelligence Platform for IGOs",
    "organization": "UN Agencies and IGOs in Kenya",
}

# Security Settings
SECURITY_CONFIG = {
    "session_duration": timedelta(hours=8),
    "password_expiry_days": 90,
    "min_password_length": 12,
    "require_special_chars": True,
    "require_numbers": True,
    "max_login_attempts": 3,
    "mfa_enabled": True,
}

# API Configuration
API_CONFIG = {
    "base_url": "https://api.diplocyber.com",
    "version": "v1",
    "timeout": 30,  # seconds
    "rate_limit": 100,  # requests per minute
}

# Database Configuration
DB_CONFIG = {
    "type": "sqlite",  # can be changed to postgresql for production
    "name": "diplocyber.db",
    "backup_enabled": True,
    "backup_frequency": "daily",
    "max_connections": 20,
}

# Monitoring Configuration
MONITORING_CONFIG = {
    "log_level": "INFO",
    "enable_audit_trail": True,
    "metrics_retention_days": 90,
    "alert_threshold": {
        "critical": 90,
        "warning": 70,
        "info": 50,
    },
}

# Email Configuration
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "use_tls": True,
    "sender_email": "notifications@diplocyber.com",
    "reply_to": "support@diplocyber.com",
}

# Threat Intelligence Sources
THREAT_INTELLIGENCE = {
    "sources": [
        {
            "name": "Kenya CERT",
            "enabled": True,
            "priority": "high",
        },
        {
            "name": "African Union Cybersecurity",
            "enabled": True,
            "priority": "high",
        },
        {
            "name": "UN Security Advisory",
            "enabled": True,
            "priority": "critical",
        },
    ],
    "update_frequency": "hourly",
}

# User Roles and Permissions
ROLES = {
    "administrator": {
        "can_view_dashboard": True,
        "can_modify_settings": True,
        "can_manage_users": True,
        "can_view_reports": True,
        "can_modify_rules": True,
    },
    "security_analyst": {
        "can_view_dashboard": True,
        "can_modify_settings": False,
        "can_manage_users": False,
        "can_view_reports": True,
        "can_modify_rules": True,
    },
    "viewer": {
        "can_view_dashboard": True,
        "can_modify_settings": False,
        "can_manage_users": False,
        "can_view_reports": True,
        "can_modify_rules": False,
    },
}

# UI Configuration
UI_CONFIG = {
    "theme": {
        "primary_color": "#000000",
        "secondary_color": "#FFFFFF",
        "accent_color": "#90EE90",
        "highlight_color": "#FFD700",
    },
    "dashboard": {
        "refresh_interval": 60,  # seconds
        "max_alerts_displayed": 10,
        "enable_animations": True,
    },
    "charts": {
        "default_height": 400,
        "enable_interactive": True,
        "color_palette": ["#FFD700", "#90EE90", "#000000"],
    },
}

# Feature Flags
FEATURES = {
    "enable_mfa": True,
    "enable_api_access": True,
    "enable_export": True,
    "enable_advanced_analytics": True,
    "enable_threat_intelligence": True,
    "enable_automated_response": False,  # Coming soon
    "enable_machine_learning": False,    # Coming soon
}

# Notification Settings
NOTIFICATION_CONFIG = {
    "channels": {
        "email": {
            "enabled": True,
            "priority": ["critical", "high"],
        },
        "sms": {
            "enabled": True,
            "priority": ["critical"],
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

# Regional Settings
REGIONAL_CONFIG = {
    "timezone": "Africa/Nairobi",
    "date_format": "%Y-%m-%d",
    "time_format": "%H:%M:%S",
    "language": "en",
    "country": "KE",
}

# Development Settings (should be False in production)
DEBUG = False
TESTING = False
