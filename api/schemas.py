from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class ThreatReportSchema(BaseModel):
    title: str
    description: str
    severity: str
    affected_systems: List[str]
    reported_by: str
    organization_id: str

class AlertSchema(BaseModel):
    title: str
    description: str
    severity: str
    organization_id: str
    source: str

class RiskAssessmentSchema(BaseModel):
    organization_id: str
    risk_factors: dict
    overall_score: float
    recommendations: List[str]

class AssetSchema(BaseModel):
    name: str
    type: str
    organization_id: str
    location: str
    owner: str
    security_classification: str

class ComplianceReportSchema(BaseModel):
    organization_id: str
    framework: str
    compliance_score: float
    findings: List[dict]
    remediation_plan: dict

class AnalyticsRequestSchema(BaseModel):
    organization_id: str
    metric_type: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
