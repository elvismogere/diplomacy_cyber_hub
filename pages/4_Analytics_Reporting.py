import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub | Analytics & Reporting",
    page_icon="📊",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'DiploCyber Hub - Analytics & Reporting'
    }
)

# Custom styling
st.markdown("""
    <style>
    /* Global theme consistency */
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
        font-family: 'Helvetica Neue', sans-serif;
    }
    
    /* Analytics Header */
    .analytics-header {
        color: #000000;
        font-size: 2.5rem;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(to right, #FFFFFF, #90EE90, #FFFFFF);
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    
    /* Analytics card styling */
    .analytics-card {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .analytics-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Metric styling */
    .metric-row {
        display: flex;
        justify-content: space-between;
        margin: 10px 0;
    }
    
    .trend-up {
        color: #90EE90;
    }
    
    .trend-down {
        color: #FFD700;
    }
    
    /* Chart containers */
    .chart-container {
        background-color: var(--card-background);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
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
st.markdown("<h1 class='analytics-header'>📊 Analytics & Reporting</h1>", unsafe_allow_html=True)
st.markdown("### Comprehensive Security Analytics Dashboard")

# Date Range Selector
col1, col2 = st.columns([2, 2])
with col1:
    start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
with col2:
    end_date = st.date_input("End Date", datetime.now())

# Key Metrics Row
metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.markdown("""
        <div class="analytics-card">
            <h3>Total Incidents</h3>
            <h2 style="color: #FFD700;">247</h2>
            <p class="trend-up">↑ 12% from last month</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown("""
        <div class="analytics-card">
            <h3>Resolution Rate</h3>
            <h2 style="color: #90EE90;">94%</h2>
            <p class="trend-up">↑ 3% improvement</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown("""
        <div class="analytics-card">
            <h3>Avg Response Time</h3>
            <h2 style="color: #FFD700;">45min</h2>
            <p class="trend-down">↓ 15% faster</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col4:
    st.markdown("""
        <div class="analytics-card">
            <h3>Security Score</h3>
            <h2 style="color: #90EE90;">87/100</h2>
            <p class="trend-up">↑ 5 points</p>
        </div>
    """, unsafe_allow_html=True)

# Threat Analysis Section
st.markdown("<h3 class='section-header'>Threat Analysis</h3>", unsafe_allow_html=True)

# Create sample data for threats over time
dates = pd.date_range(start=start_date, end=end_date, freq='D')
threat_data = pd.DataFrame({
    'Date': dates,
    'Phishing': np.random.randint(5, 15, size=len(dates)),
    'Malware': np.random.randint(3, 10, size=len(dates)),
    'DDoS': np.random.randint(1, 5, size=len(dates)),
    'Unauthorized_Access': np.random.randint(2, 8, size=len(dates))
})

# Create stacked area chart
fig = go.Figure()

for column in ['Phishing', 'Malware', 'DDoS', 'Unauthorized_Access']:
    fig.add_trace(go.Scatter(
        x=threat_data['Date'],
        y=threat_data[column],
        name=column,
        stackgroup='one',
        fill='tonexty'
    ))

fig.update_layout(
    title='Threat Distribution Over Time',
    xaxis_title='Date',
    yaxis_title='Number of Threats',
    height=400,
    showlegend=True,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig, use_container_width=True)

# Geographic Distribution
st.markdown("<h3 class='section-header'>Geographic Distribution of Threats</h3>", unsafe_allow_html=True)

# Sample data for geographic distribution
df_geo = pd.DataFrame({
    'lat': [-1.2921, -1.3, -1.25, -1.28],
    'lon': [36.8219, 36.85, 36.82, 36.81],
    'intensity': [80, 60, 40, 30],
    'location': ['Central HQ', 'Regional Office A', 'Regional Office B', 'Data Center']
})

fig_geo = px.density_mapbox(
    df_geo,
    lat='lat',
    lon='lon',
    z='intensity',
    radius=20,
    center=dict(lat=-1.2921, lon=36.8219),
    zoom=11,
    mapbox_style="carto-positron"
)

st.plotly_chart(fig_geo, use_container_width=True)

# Security Metrics
st.markdown("<h3 class='section-header'>Security Metrics</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Vulnerability Status
    labels = ['Resolved', 'In Progress', 'Open']
    values = [65, 25, 10]
    
    fig_vuln = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.3,
        marker_colors=['#90EE90', '#FFD700', '#FF0000']
    )])
    
    fig_vuln.update_layout(
        title='Vulnerability Status Distribution',
        height=300,
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_vuln, use_container_width=True)

with col2:
    # Incident Response Times
    response_times = np.random.normal(45, 15, 100)
    
    fig_response = go.Figure(data=[go.Histogram(
        x=response_times,
        nbinsx=20,
        marker_color='#90EE90'
    )])
    
    fig_response.update_layout(
        title='Incident Response Time Distribution (minutes)',
        xaxis_title='Response Time',
        yaxis_title='Frequency',
        height=300,
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig_response, use_container_width=True)

# Compliance Metrics
st.markdown("<h3 class='section-header'>Compliance & Policy Metrics</h3>", unsafe_allow_html=True)

compliance_data = {
    'Category': ['Data Protection', 'Access Control', 'Incident Response', 'Security Training', 'Network Security'],
    'Score': [92, 88, 95, 78, 85]
}

fig_compliance = go.Figure(data=[
    go.Bar(
        x=compliance_data['Category'],
        y=compliance_data['Score'],
        marker_color=['#90EE90' if score >= 90 else '#FFD700' if score >= 80 else '#FF0000' 
                     for score in compliance_data['Score']]
    )
])

fig_compliance.update_layout(
    title='Compliance Scores by Category',
    yaxis_title='Compliance Score (%)',
    height=300,
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_compliance, use_container_width=True)

# Report Generation Section
st.markdown("<h3 class='section-header'>Report Generation</h3>", unsafe_allow_html=True)

report_col1, report_col2 = st.columns(2)

with report_col1:
    st.markdown("""
        <div class="analytics-card">
            <h4>Custom Report Builder</h4>
            <p>Generate tailored security reports</p>
        </div>
    """, unsafe_allow_html=True)
    
    report_type = st.selectbox(
        "Report Type",
        ["Executive Summary", "Technical Detail", "Compliance Report", "Incident Analysis"]
    )
    
    include_metrics = st.multiselect(
        "Include Metrics",
        ["Threat Distribution", "Response Times", "Geographic Analysis", "Temporal Trends"],
        default=["Threat Distribution"]
    )
    
    if st.button("Generate Report"):
        st.success("Generating custom report... Please wait.")

with report_col2:
    st.markdown("""
        <div class="analytics-card">
            <h4>Scheduled Reports</h4>
            <p>Configure automated report delivery</p>
        </div>
    """, unsafe_allow_html=True)
    
    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "Monthly", "Quarterly"]
    )
    
    recipients = st.text_input("Email Recipients (comma-separated)")
    
    if st.button("Schedule Reports"):
        st.success("Report schedule configured successfully!")

# Sidebar
with st.sidebar:
    st.markdown("### Analytics Controls")
    
    # Filters
    st.markdown("#### Data Filters")
    st.multiselect(
        "Organization Type",
        ["UN Agencies", "Regional Bodies", "Diplomatic Missions", "International NGOs"],
        default=["UN Agencies"]
    )
    
    st.multiselect(
        "Threat Categories",
        ["Cyber Attacks", "Data Breaches", "Policy Violations", "System Vulnerabilities"],
        default=["Cyber Attacks"]
    )
    
    # Export Options
    st.markdown("#### Export Options")
    export_format = st.selectbox(
        "Export Format",
        ["PDF", "Excel", "CSV", "JSON"]
    )
    
    if st.button("Export Analytics"):
        st.success(f"Exporting data in {export_format} format...")
    
    # Advanced Analytics
    st.markdown("#### Advanced Analytics")
    if st.button("Run Predictive Analysis"):
        st.info("Analyzing trends and generating predictions...")
    
    if st.button("Generate Risk Score"):
        st.success("Calculating organizational risk score...")
