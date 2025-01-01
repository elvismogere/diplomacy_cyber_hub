import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="DiploCyber Hub | Risk Assessment",
    page_icon="🎯",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'DiploCyber Hub - Risk Assessment Module'
    }
)

# Custom styling with dark mode support
st.markdown("""
    <style>
    /* Global theme consistency */
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Risk Assessment Header */
    .risk-header {
        color: #000000;
        font-size: 2.5rem;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(to right, #FFFFFF, #90EE90, #FFFFFF);
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    
    /* Card styling */
    .risk-card {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .risk-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Risk level indicators */
    .risk-high {
        border-left: 4px solid #FFD700;
    }
    
    .risk-medium {
        border-left: 4px solid #90EE90;
    }
    
    .risk-low {
        border-left: 4px solid #000000;
    }
    
    /* Form styling */
    .stTextInput>div>div>input {
        border-radius: 5px;
        border: 1px solid var(--border-color);
    }
    
    .stSelectbox>div>div>div {
        border-radius: 5px;
        border: 1px solid var(--border-color);
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #000000;
        color: #FFFFFF;
        border-radius: 20px;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #90EE90;
        color: #000000;
        transform: translateY(-2px);
    }
    
    /* Dark mode styles */
    [data-theme="dark"] {
        --background-color: #1E1E1E;
        --text-color: #FFFFFF;
        --card-background: #2D2D2D;
        --border-color: #404040;
    }
    
    /* Light mode styles */
    [data-theme="light"] {
        --background-color: #FFFFFF;
        --text-color: #000000;
        --card-background: #FFFFFF;
        --border-color: #90EE90;
    }
    
    /* Chart containers */
    .chart-container {
        background-color: var(--card-background);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Section headers */
    .section-header {
        color: #000000;
        border-bottom: 2px solid #90EE90;
        padding-bottom: 10px;
        margin: 20px 0;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize theme state
if 'theme' not in st.session_state:
    st.session_state.theme = "light"

# Theme toggle in header
col1, col2 = st.columns([6,1])
with col2:
    if st.button("🌓 Toggle Theme"):
        st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
        st.rerun()

# Apply theme
st.markdown(f"""
    <script>
        document.body.setAttribute('data-theme', '{st.session_state.theme}');
    </script>
    """, unsafe_allow_html=True)

# Header
st.markdown("<h1 class='risk-header'>🎯 Risk Assessment</h1>", unsafe_allow_html=True)

# Main content
tab1, tab2, tab3 = st.tabs(["Quick Assessment", "Detailed Analysis", "Risk Matrix"])

with tab1:
    st.markdown("<h3 class='section-header'>Quick Risk Assessment</h3>", unsafe_allow_html=True)
    
    # Organization Info
    col1, col2 = st.columns(2)
    with col1:
        org_name = st.text_input("Organization Name")
        dept_name = st.text_input("Department")
    with col2:
        assessment_date = st.date_input("Assessment Date")
        assessor_name = st.text_input("Assessor Name")

    # Risk Categories
    st.markdown("<h3 class='section-header'>Risk Categories</h3>", unsafe_allow_html=True)
    
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
        st.markdown("<h3 class='section-header'>Assessment Results</h3>", unsafe_allow_html=True)
        
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
    st.markdown("<h3 class='section-header'>Detailed Risk Analysis</h3>", unsafe_allow_html=True)
    
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
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#000000')
    )

    st.plotly_chart(fig, use_container_width=True)

    # Vulnerability Assessment
    st.markdown("#### Vulnerability Assessment")
    
    vulnerabilities = [
        {"type": "Network Security", "severity": "High", "status": "Open", "description": "Outdated firewall configurations"},
        {"type": "Access Control", "severity": "Medium", "status": "In Progress", "description": "Weak password policies"},
        {"type": "Data Protection", "severity": "High", "status": "Open", "description": "Unencrypted data storage"},
        {"type": "Physical Security", "severity": "Low", "status": "Resolved", "description": "Server room access logs"},
    ]

    for vuln in vulnerabilities:
        severity_class = f"risk-{vuln['severity'].lower()}"
        st.markdown(f"""
            <div class="risk-card {severity_class}">
                <h4>{vuln['type']}</h4>
                <p><strong>Severity:</strong> {vuln['severity']}</p>
                <p><strong>Status:</strong> {vuln['status']}</p>
                <p><strong>Description:</strong> {vuln['description']}</p>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 class='section-header'>Risk Matrix</h3>", unsafe_allow_html=True)
    
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
            size=45,
            color=df['Color'],
            symbol='square',
            line=dict(color='#000000', width=1)
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
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#000000')
    )

    st.plotly_chart(fig, use_container_width=True)

    # Risk Matrix Legend
    st.markdown("""
        <div class="risk-card">
            <h4>Risk Level Guide</h4>
            <p><span style="color: #FF0000;">■</span> High Risk (Score: 10-16)</p>
            <p><span style="color: #FFD700;">■</span> Medium Risk (Score: 5-9)</p>
            <p><span style="color: #90EE90;">■</span> Low Risk (Score: 1-4)</p>
        </div>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Risk Assessment Tools")
    
    if st.button("Generate Risk Report"):
        st.success("Generating comprehensive risk report...")
    
    if st.button("Export Assessment"):
        st.info("Preparing export...")
    
    st.markdown("### Historical Assessments")
    st.markdown("""
        <div class="risk-card">
            <p><strong>Last Assessment:</strong> 2024-02-15</p>
            <p><strong>Risk Trend:</strong> <span style="color: #90EE90;">↓ Improving</span></p>
            <p><strong>Completed Assessments:</strong> 12</p>
            <p><strong>Next Scheduled:</strong> 2024-03-15</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Quick Actions")
    if st.button("Schedule Assessment"):
        st.success("Assessment scheduled successfully!")
    
    if st.button("View Previous Reports"):
        st.info("Loading previous reports...")
