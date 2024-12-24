import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class AnalyticsEngine:
    @staticmethod
    def calculate_threat_metrics(threats: list) -> dict:
        """Calculate threat-related metrics"""
        df = pd.DataFrame(threats)
        
        metrics = {
            'total_threats': len(threats),
            'critical_threats': len(df[df['severity'] == 'critical']),
            'high_threats': len(df[df['severity'] == 'high']),
            'medium_threats': len(df[df['severity'] == 'medium']),
            'low_threats': len(df[df['severity'] == 'low']),
            'average_resolution_time': df['resolution_time'].mean(),
            'threat_trend': df.groupby('date').size().to_dict()
        }
        
        return metrics

    @staticmethod
    def generate_risk_score(assessment_data: dict) -> float:
        """Generate risk score based on assessment data"""
        weights = {
            'technical_controls': 0.3,
            'policy_compliance': 0.2,
            'user_awareness': 0.2,
            'incident_history': 0.3
        }
        
        score = sum(assessment_data[key] * weights[key] 
                   for key in weights if key in assessment_data)
        
        return round(score, 2)

    @staticmethod
    def analyze_incident_patterns(incidents: list) -> dict:
        """Analyze patterns in security incidents"""
        df = pd.DataFrame(incidents)
        
        analysis = {
            'common_types': df['type'].value_counts().to_dict(),
            'time_distribution': df.groupby('hour')['id'].count().to_dict(),
            'severity_distribution': df['severity'].value_counts().to_dict(),
            'average_response_time': df['response_time'].mean()
        }
        
        return analysis
