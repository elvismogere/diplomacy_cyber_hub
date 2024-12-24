import pytest
from datetime import datetime

@pytest.fixture
def test_organization():
    """Fixture for test organization data"""
    return {
        "id": "test_org_123",
        "name": "Test Organization",
        "type": "UN Agency",
        "country": "Kenya",
        "created_at": datetime.utcnow()
    }

@pytest.fixture
def test_user():
    """Fixture for test user data"""
    return {
        "id": "test_user_123",
        "email": "test@example.com",
        "username": "testuser",
        "organization_id": "test_org_123",
        "role": "administrator"
    }

@pytest.fixture
def test_threat():
    """Fixture for test threat data"""
    return {
        "id": "test_threat_123",
        "title": "Test Threat",
        "description": "Test description",
        "severity": "high",
        "organization_id": "test_org_123",
        "created_at": datetime.utcnow()
    }
