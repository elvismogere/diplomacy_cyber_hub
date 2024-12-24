import hashlib
import jwt
import secrets
from datetime import datetime, timedelta
from config import SECURITY_CONFIG
import re

class SecurityUtils:
    @staticmethod
    def hash_password(password: str) -> str:
        """Create secure password hash"""
        salt = secrets.token_hex(16)
        return hashlib.sha256(f"{password}{salt}".encode()).hexdigest() + ":" + salt

    @staticmethod
    def verify_password(stored_password: str, provided_password: str) -> bool:
        """Verify password against stored hash"""
        if ":" not in stored_password:
            return False
        stored_hash, salt = stored_password.split(":")
        verify_hash = hashlib.sha256(f"{provided_password}{salt}".encode()).hexdigest()
        return secrets.compare_digest(stored_hash, verify_hash)

    @staticmethod
    def generate_token(user_id: str, role: str) -> str:
        """Generate JWT token for user authentication"""
        expiration = datetime.utcnow() + timedelta(hours=8)
        payload = {
            'user_id': user_id,
            'role': role,
            'exp': expiration
        }
        return jwt.encode(payload, SECURITY_CONFIG['jwt_secret'], algorithm='HS256')

    @staticmethod
    def validate_password_strength(password: str) -> tuple[bool, str]:
        """Check if password meets security requirements"""
        if len(password) < SECURITY_CONFIG['min_password_length']:
            return False, f"Password must be at least {SECURITY_CONFIG['min_password_length']} characters"
        
        checks = {
            'uppercase': r'[A-Z]',
            'lowercase': r'[a-z]',
            'numbers': r'[0-9]',
            'special': r'[!@#$%^&*(),.?":{}|<>]'
        }
        
        missing = []
        for check_name, pattern in checks.items():
            if not re.search(pattern, password):
                missing.append(check_name)
        
        if missing:
            return False, f"Password must contain {', '.join(missing)}"
        
        return True, "Password meets requirements"

    @staticmethod
    def sanitize_input(input_string: str) -> str:
        """Sanitize user input to prevent XSS and injection attacks"""
        # Remove HTML tags
        clean = re.compile('<.*?>')
        sanitized = re.sub(clean, '', input_string)
        # Escape special characters
        sanitized = re.sub(r'[^\w\s-]', '', sanitized)
        return sanitized.strip()
