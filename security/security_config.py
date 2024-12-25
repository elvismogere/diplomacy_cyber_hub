from datetime import timedelta

# Security Configuration
SECURITY_CONFIG = {
    # Session Security
    "SESSION_LIFETIME": timedelta(hours=8),
    "SESSION_REFRESH_EACH_REQUEST": True,
    "PERMANENT_SESSION_LIFETIME": timedelta(days=1),
    
    # Password Policy
    "PASSWORD_MIN_LENGTH": 12,
    "PASSWORD_REQUIRE_UPPERCASE": True,
    "PASSWORD_REQUIRE_LOWERCASE": True,
    "PASSWORD_REQUIRE_NUMBERS": True,
    "PASSWORD_REQUIRE_SPECIAL": True,
    
    # Authentication
    "MAX_LOGIN_ATTEMPTS": 5,
    "LOCKOUT_DURATION": timedelta(minutes=30),
    "MFA_ENABLED": True,
    
    # API Security
    "API_KEY_LENGTH": 32,
    "API_KEY_EXPIRY": timedelta(days=90),
    "RATE_LIMIT_REQUESTS": 100,
    "RATE_LIMIT_PERIOD": timedelta(minutes=1),
    
    # Headers
    "SECURITY_HEADERS": {
        "X-Frame-Options": "SAMEORIGIN",
        "X-XSS-Protection": "1; mode=block",
        "X-Content-Type-Options": "nosniff",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    },
    
    # CORS Settings
    "CORS_ALLOWED_ORIGINS": [
        "https://diplocyber.com",
        "https://api.diplocyber.com"
    ],
    "CORS_ALLOWED_METHODS": ["GET", "POST", "PUT", "DELETE"],
    "CORS_ALLOWED_HEADERS": ["Content-Type", "Authorization"],
    
    # Encryption
    "ENCRYPTION_ALGORITHM": "HS256",
    "KEY_ROTATION_INTERVAL": timedelta(days=30),
    
    # Logging
    "SECURITY_LOG_LEVEL": "INFO",
    "AUDIT_LOG_ENABLED": True,
    "SENSITIVE_FIELDS": [
        "password",
        "token",
        "api_key",
        "secret"
    ]
}
