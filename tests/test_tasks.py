import pytest
from tasks.security_tasks import SecurityTasks
from tasks.maintenance_tasks import MaintenanceTasks
from tasks.report_tasks import ReportTasks

class TestSecurityTasks:
    @pytest.mark.asyncio
    async def test_security_scan(self):
        """Test security scanning functionality"""
        results = await SecurityTasks.perform_security_scan("test_org")
        assert results is not None
        assert "network_status" in results
        assert "vulnerabilities" in results

class TestMaintenanceTasks:
    @pytest.mark.asyncio
    async def test_cleanup_old_data(self):
        """Test data cleanup functionality"""
        await MaintenanceTasks.cleanup_old_data()
        # Add assertions for cleanup verification

class TestReportTasks:
    @pytest.mark.asyncio
    async def test_generate_security_report(self):
        """Test report generation functionality"""
        report = await ReportTasks.generate_security_report("test_org")
        assert report is not None
Create tests/test_utils.py:
import pytest
from utils.security import SecurityUtils
from utils.analytics import AnalyticsEngine
from utils.validators import Validators

class TestSecurityUtils:
    def test_password_hashing(self):
        """Test password hashing functionality"""
        password = "TestPassword123!"
        hashed = SecurityUtils.hash_password(password)
        assert SecurityUtils.verify_password(hashed, password)

    def test_token_generation(self):
        """Test token generation and validation"""
        token = SecurityUtils.generate_token("test_user", "admin")
        assert token is not None

class TestAnalyticsEngine:
    def test_risk_score_calculation(self):
        """Test risk score calculation"""
        assessment_data = {
            "technical_controls": 0.8,
            "policy_compliance": 0.7,
            "user_awareness": 0.6,
            "incident_history": 0.9
        }
        score = AnalyticsEngine.generate_risk_score(assessment_data)
        assert 0 <= score <= 1

class TestValidators:
    def test_email_validation(self):
        """Test email validation"""
        valid_email = "test@example.com"
        invalid_email = "invalid-email"
        assert Validators.validate_email(valid_email)
        assert not Validators.validate_email(invalid_email)

    def test_phone_validation(self):
        """Test phone number validation"""
        valid_phone = "+254123456789"
        invalid_phone = "123"
        assert Validators.validate_phone(valid_phone)
        assert not Validators.validate_phone(invalid_phone)
