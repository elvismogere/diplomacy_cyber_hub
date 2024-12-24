import pytest
from services.threat_service import ThreatService
from services.risk_service import RiskService
from services.alert_service import AlertService
from datetime import datetime

class TestThreatService:
    @pytest.mark.asyncio
    async def test_report_threat(self):
        """Test threat reporting functionality"""
        threat_data = {
            "title": "Test Threat",
            "description": "Test description",
            "severity": "high",
            "organization_id": "test_org"
        }
        threat = await ThreatService.report_threat(threat_data)
        assert threat is not None
        assert threat.title == threat_data["title"]

    @pytest.mark.asyncio
    async def test_get_threats(self):
        """Test threat retrieval functionality"""
        threats = await ThreatService.get_threats("test_org")
        assert isinstance(threats, list)

class TestRiskService:
    @pytest.mark.asyncio
    async def test_perform_risk_assessment(self):
        """Test risk assessment functionality"""
        assessment = await RiskService.perform_risk_assessment("test_org")
        assert assessment is not None
        assert isinstance(assessment.overall_risk_score, float)

class TestAlertService:
    @pytest.mark.asyncio
    async def test_create_alert(self):
        """Test alert creation functionality"""
        alert_data = {
            "title": "Test Alert",
            "description": "Test description",
            "severity": "high",
            "organization_id": "test_org"
        }
        alert = await AlertService.create_alert(alert_data)
        assert alert is not None
        assert alert.title == alert_data["title"]
