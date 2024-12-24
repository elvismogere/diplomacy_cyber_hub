from datetime import datetime
import uuid
from enum import Enum

class ThreatLevel(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class ThreatStatus(Enum):
    ACTIVE = "active"
    INVESTIGATING = "investigating"
    CONTAINED = "contained"
    RESOLVED = "resolved"

class UserRole(Enum):
    ADMINISTRATOR = "administrator"
    SECURITY_ANALYST = "security_analyst"
    VIEWER = "viewer"

class BaseModel:
    """Base model with common fields"""
    id: str = str(uuid.uuid4())
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    is_active: bool = True

class Organization(BaseModel):
    """Organization model for IGOs"""
    name: str
    type: str  # UN Agency, Regional IGO, etc.
    country: str
    address: str
    contact_email: str
    contact_phone: str
    security_level: str
    subscription_status: str
    max_users: int
    features_enabled: dict

class User(BaseModel):
    """User model for system access"""
    email: str
    username: str
    password_hash: str
    first_name: str
    last_name: str
    organization_id: str
    role: UserRole
    last_login: datetime
    mfa_enabled: bool
    failed_login_attempts: int
    password_changed_at: datetime
    is_locked: bool

class ThreatIncident(BaseModel):
    """Model for tracking security threats and incidents"""
    title: str
    description: str
    organization_id: str
    reported_by: str
    threat_level: ThreatLevel
    status: ThreatStatus
    affected_systems: list
    impact_assessment: str
    mitigation_steps: list
    resolution_notes: str
    resolved_at: datetime
    resolution_time: int  # in minutes

class SecurityAlert(BaseModel):
    """Security alert notifications"""
    title: str
    description: str
    organization_id: str
    threat_level: ThreatLevel
    source: str
    is_acknowledged: bool
    acknowledged_by: str
    acknowledged_at: datetime
    requires_action: bool
    action_taken: str

class AuditLog(BaseModel):
    """System audit logging"""
    user_id: str
    organization_id: str
    action: str
    resource_type: str
    resource_id: str
    ip_address: str
    user_agent: str
    details: dict

class RiskAssessment(BaseModel):
    """Risk assessment records"""
    organization_id: str
    conducted_by: str
    assessment_date: datetime
    overall_risk_score: float
    risk_factors: dict
    recommendations: list
    next_assessment_date: datetime
    compliance_status: dict

class SecurityPolicy(BaseModel):
    """Security policies and procedures"""
    organization_id: str
    title: str
    content: str
    version: str
    approved_by: str
    approved_at: datetime
    effective_date: datetime
    review_date: datetime
    policy_type: str
    attachments: list

class AssetInventory(BaseModel):
    """Digital asset inventory"""
    organization_id: str
    asset_name: str
    asset_type: str
    location: str
    status: str
    owner: str
    security_classification: str
    last_assessment_date: datetime
    vulnerabilities: list
    patches_applied: list

class VulnerabilityReport(BaseModel):
    """Vulnerability assessment reports"""
    organization_id: str
    scan_date: datetime
    scanner_type: str
    vulnerabilities: list
    risk_score: float
    remediation_steps: list
    assigned_to: str
    status: str
    verification_status: str

class TrainingRecord(BaseModel):
    """Security training records"""
    user_id: str
    organization_id: str
    training_type: str
    completion_date: datetime
    score: float
    certification: str
    valid_until: datetime
    training_provider: str
    materials_accessed: list

class IncidentResponse(BaseModel):
    """Incident response procedures"""
    organization_id: str
    incident_type: str
    response_team: list
    procedures: list
    contact_list: dict
    resources_required: list
    escalation_matrix: dict
    recovery_steps: list
    lessons_learned: str

class ComplianceReport(BaseModel):
    """Compliance monitoring and reporting"""
    organization_id: str
    framework: str
    assessment_date: datetime
    assessor: str
    compliance_score: float
    findings: list
    remediation_plan: dict
    next_review_date: datetime
    attachments: list

class NotificationSettings(BaseModel):
    """User notification preferences"""
    user_id: str
    organization_id: str
    email_enabled: bool
    sms_enabled: bool
    in_app_enabled: bool
    notification_types: dict
    quiet_hours: dict
    preferred_language: str

class APIKey(BaseModel):
    """API access keys"""
    organization_id: str
    key_name: str
    key_hash: str
    permissions: list
    last_used: datetime
    expires_at: datetime
    rate_limit: int
    created_by: str

class SystemMetrics(BaseModel):
    """System performance metrics"""
    timestamp: datetime
    organization_id: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    network_traffic: dict
    active_users: int
    response_time: float
    error_rate: float
