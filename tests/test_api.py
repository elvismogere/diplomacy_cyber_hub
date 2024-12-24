import pytest
from fastapi.testclient import TestClient
from api.routes import api
from datetime import datetime

client = TestClient(api)

class TestAPIEndpoints:
    def setup_method(self):
        """Setup test environment"""
        self.api_key = "test_api_key"
        self.headers = {"X-API-Key": self.api_key}
        self.organization_id = "test_org_123"

    def test_get_threats(self):
        """Test threat retrieval endpoint"""
        response = client.get(
            f"/api/v1/threats?organization_id={self.organization_id}",
            headers=self.headers
        )
        assert response.status_code == 200
        assert "data" in response.json()

    def test_report_threat(self):
        """Test threat reporting endpoint"""
        threat_data = {
            "title": "Test Threat",
            "description": "Test description",
            "severity": "high",
            "organization_id": self.organization_id
        }
        response = client.post(
            "/api/v1/threats",
            json=threat_data,
            headers=self.headers
        )
        assert response.status_code == 200
        assert response.json()["status"] == "success"

    def test_get_risk_assessment(self):
        """Test risk assessment retrieval"""
        response = client.get(
            f"/api/v1/risk-assessment/{self.organization_id}",
            headers=self.headers
        )
        assert response.status_code == 200

    def test_invalid_api_key(self):
        """Test invalid API key handling"""
        response = client.get(
            f"/api/v1/threats?organization_id={self.organization_id}",
            headers={"X-API-Key": "invalid_key"}
        )
        assert response.status_code == 403
