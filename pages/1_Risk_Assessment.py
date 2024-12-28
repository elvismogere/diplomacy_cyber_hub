import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Risk Assessment | DiploCyber Hub",
    page_icon="🎯",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .risk-header {
        font-size: 2rem;
        color: #000000;
        padding: 1rem 0;
        border-bottom: 2px solid #90EE90;
        margin-bottom: 2rem;
    }
    .risk-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .risk-high {
        border-left: 4px solid #FFD700;
    }
    .risk-medium {
        border-left: 4px solid #90EE90;
    }
    .risk-low {
        border-left: 4px solid #000000;
    }
    .recommendation-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='risk-header'>🎯 Risk Assessment</h1>", unsafe_allow_html=True)

# Main content
tab1, tab2, tab3 = st.tabs(["Quick Assessment", "Detailed Analysis", "Risk Matrix"])

with tab1:
    st.markdown("### Quick Risk Assessment")
    
    # Organization Info
    col1, col2 = st.columns(2)
    with col1:
        org_name = st.text_input("Organization Name")
        dept_name = st.text_input("Department")
    with col2:
        assessment_date = st.date_input("Assessment Date")
        assessor_name = st.text_input("Assessor Name")

    # Risk Categories
    st.markdown("### Risk Categories")
    
    # Technical Controls
    st.markdown("#### 1. Technical Controls")
    tech_controls = {
        "Data Encryption": st.select_slider(
            "Data Encryption Level",
            options=["None", "Basic", "Standard", "Advanced", "Military-Grade"],
            value="Standard"
        ),
        "Access Control": st.select_slider(
            "Access Control Measures",
            options=["Minimal", "Basic", "Standard", "Strong", "Very Strong"],
            value="Standard"
        ),
        "Network Security": st.select_slider(
            "Network Security Level",
            options=["Basic", "Standard", "Enhanced", "Advanced", "Enterprise"],
            value="Standard"
        )
    }

    # Policy & Procedures
    st.markdown("#### 2. Policy & Procedures")
    policy_controls = {
        "Security Policies": st.select_slider(
            "Security Policy Implementation",
            options=["None", "Partial", "Standard", "Comprehensive", "Advanced"],
            value="Standard"
        ),
        "Incident Response": st.select_slider(
            "Incident Response Readiness",
            options=["None", "Basic", "Standard", "Advanced", "Comprehensive"],
            value="Standard"
        )
    }

    # Human Factors
    st.markdown("#### 3. Human Factors")
    human_factors = {
        "Staff Training": st.select_slider(
            "Security Training Level",
            options=["None", "Basic", "Standard", "Advanced", "Comprehensive"],
            value="Standard"
        ),
        "Security Awareness": st.select_slider(
            "Security Awareness Program",
            options=["None", "Basic", "Standard", "Advanced", "Comprehensive"],
            value="Standard"
        )
    }

    if st.button("Calculate Risk Score"):
        # Calculate scores
        def convert_to_score(value):
            options = ["None", "Basic", "Standard", "Advanced", "Comprehensive"]
            return (options.index(value) + 1) / len(options)

        tech_score = sum(convert_to_score(v) for v in tech_controls.values()) / len(tech_controls)
        policy_score = sum(convert_to_score(v) for v in policy_controls.values()) / len(policy_controls)
        human_score = sum(convert_to_score(v) for v in human_factors.values()) / len(human_factors)
        
        total_score = (tech_score + policy_score + human_score) / 3
        
        # Display results
        st.markdown("### Assessment Results")
        
        col1, col2 = st.columns(2)
        with col1:
            # Risk level determination
            if total_score >= 0.8:
                risk_level = "Low Risk"
                color = "#90EE90"
            elif total_score >= 0.6:
                risk_level = "Medium Risk"
                color = "#FFD700"
            else:
                risk_level = "High Risk"
                color = "#FF0000"

            st.markdown(f"""
                <div class="risk-card">
                    <h2 style="color: {color};">{risk_level}</h2>
                    <h3>Overall Score: {total_score:.2%}</h3>
                    <p>Technical Controls: {tech_score:.2%}</p>
                    <p>Policy & Procedures: {policy_score:.2%}</p>
                    <p>Human Factors: {human_score:.2%}</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="risk-card">
                    <h3>Key Recommendations:</h3>
                    <ul>
                        <li>Enhance data encryption measures</li>
                        <li>Strengthen access controls</li>
                        <li>Update security policies</li>
                        <li>Improve staff training program</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Detailed Risk Analysis")
    
    # Historical Risk Trends
    st.markdown("#### Historical Risk Trends")
    
    # Sample data for historical trends
    dates = pd.date_range(start='2024-01-01', end='2024-02-29', freq='D')
    risk_scores = [0.7 + (i % 5) * 0.05 for i in range(len(dates))]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=risk_scores,
        mode='lines+markers',
        line=dict(color='#FFD700', width=2),
        marker=dict(size=6, color='#000000')
    ))

    fig.update_layout(
        title='Risk Score Trend',
        yaxis_title='Risk Score',
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

    # Vulnerability Assessment
    st.markdown("#### Vulnerability Assessment")
    
    vulnerabilities = [
        {"type": "Network", "severity": "High", "status": "Open"},
        {"type": "Application", "severity": "Medium", "status": "In Progress"},
        {"type": "Physical", "severity": "Low", "status": "Resolved"},
    ]

    for vuln in vulnerabilities:
        severity_class = f"risk-{vuln['severity'].lower()}"
        st.markdown(f"""
            <div class="risk-card {severity_class}">
                <h4>{vuln['type']} Vulnerability</h4>
                <p>Severity: {vuln['severity']}</p>
                <p>Status: {vuln['status']}</p>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Risk Matrix")
    
    # Create risk matrix
    impact_levels = ['Low', 'Medium', 'High', 'Critical']
    likelihood_levels = ['Rare', 'Unlikely', 'Possible', 'Likely']

    # Create sample risk data
    risk_data = []
    for i, impact in enumerate(impact_levels):
        for j, likelihood in enumerate(likelihood_levels):
            risk_score = (i + 1) * (j + 1)
            if risk_score <= 4:
                color = '#90EE90'  # Low risk
            elif risk_score <= 9:
                color = '#FFD700'  # Medium risk
            else:
                color = '#FF0000'  # High risk
            
            risk_data.append(dict(
                Impact=impact,
                Likelihood=likelihood,
                Risk_Score=risk_score,
                Color=color
            ))

    df = pd.DataFrame(risk_data)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Impact'],
        y=df['Likelihood'],
        mode='markers',
        marker=dict(
            size=40,
            color=df['Color'],
            symbol='square'
        ),
        text=df['Risk_Score'],
        textposition="middle center",
        textfont=dict(
            color='white',
            size=12
        )
    ))

    fig.update_layout(
        title='Risk Assessment Matrix',
        xaxis_title='Impact',
        yaxis_title='Likelihood',
        height=600,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# Sidebar
with st.sidebar:
    st.markdown("### Risk Assessment Tools")
    
    if st.button("Generate Risk Report"):
        st.success("Generating comprehensive risk report...")
    
    if st.button("Export Assessment"):
        st.info("Preparing export...")
    
    st.markdown("### Historical Assessments")
    st.markdown("""
        <div style="padding: 10px; background-color: rgba(144, 238, 144, 0.1); border-radius: 5px;">
            <p>Last Assessment: 2024-02-15</p>
            <p>Risk Trend: ↓ Improving</p>
            <p>Completed Assessments: 12</p>
        </div>
    """, unsafe_allow_html=True)
