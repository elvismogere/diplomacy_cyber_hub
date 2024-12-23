import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Analytics & Reporting | DiploCyber Hub",
    page_icon="📊",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .analytics-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .stat-card {
        text-align: center;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .gold-text {
        color: #FFD700;
    }
    .green-text {
        color: #90EE90;
    }
    .report-section {
        margin-top: 30px;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Analytics & Reporting")
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
        <div class="stat-card">
            <h3>Total Incidents</h3>
            <h2 class="gold-text">247</h2>
            <p>↑ 12% from last month</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown("""
        <div class="stat-card">
            <h3>Resolution Rate</h3>
            <h2 class="green-text">94%</h2>
            <p>↑ 3% improvement</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown("""
        <div class="stat-card">
            <h3>Avg Response Time</h3>
            <h2 class="gold-text">45min</h2>
            <p>↓ 15% faster</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col4:
    st.markdown("""
        <div class="stat-card">
            <h3>Security Score</h3>
            <h2 class="green-text">87/100</h2>
            <p>↑ 5 points</p>
        </div>
    """, unsafe_allow_html=True)

# Threat Distribution Analysis
st.markdown("### Threat Distribution Analysis")

# Sample data for threat distribution
threat_types = ['Phishing', 'Malware', 'DDoS', 'Unauthorized Access', 'Data Breach']
threat_counts = [45, 32, 28, 20, 15]

fig_threats = go.Figure(data=[
    go.Bar(
        x=threat_types,
        y=threat_counts,
        marker_color=['#FFD700', '#90EE90', '#000000', '#FFD700', '#90EE90']
    )
])

fig_threats.update_layout(
    title='Threat Distribution by Type',
    xaxis_title='Threat Type',
    yaxis_title='Number of Incidents',
    height=400
)

st.plotly_chart(fig_threats, use_container_width=True)

# Temporal Analysis
st.markdown("### Temporal Analysis")

# Generate sample temporal data
dates = pd.date_range(start=start_date, end=end_date, freq='D')
incidents = np.random.randint(5, 15, size=len(dates))
resolved = np.random.randint(3, 12, size=len(dates))

fig_temporal = go.Figure()
fig_temporal.add_trace(go.Scatter(
    x=dates,
    y=incidents,
    name='Incidents',
    line=dict(color='#FFD700', width=2)
))
fig_temporal.add_trace(go.Scatter(
    x=dates,
    y=resolved,
    name='Resolved',
    line=dict(color='#90EE90', width=2)
))

fig_temporal.update_layout(
    title='Incident Timeline',
    xaxis_title='Date',
    yaxis_title='Number of Incidents',
    height=400
)

st.plotly_chart(fig_temporal, use_container_width=True)

# Geographic Distribution
st.markdown("### Geographic Distribution of Threats")

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

# Report Generation Section
st.markdown("### Report Generation")

report_col1, report_col2 = st.columns(2)

with report_col1:
    st.markdown("""
        <div class="analytics-card">
            <h4>Custom Report Builder</h4>
            <p>Generate tailored security reports</p>
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
    """, unsafe_allow_html=True)
    
    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "Monthly", "Quarterly"]
    )
    
    recipients = st.text_input("Email Recipients (comma-separated)")
    
    if st.button("Schedule Reports"):
        st.success("Report schedule configured successfully!")

# Export Options
st.sidebar.markdown("### Export Options")
export_format = st.sidebar.selectbox(
    "Export Format",
    ["PDF", "Excel", "CSV", "JSON"]
)

if st.sidebar.button("Export Analytics Data"):
    st.sidebar.success(f"Exporting data in {export_format} format...")

# Filters
st.sidebar.markdown("### Analysis Filters")
st.sidebar.multiselect(
    "Organization Type",
    ["UN Agencies", "Regional Bodies", "Diplomatic Missions", "International NGOs"],
    default=["UN Agencies"]
)

st.sidebar.multiselect(
    "Threat Categories",
    ["Cyber Attacks", "Data Breaches", "Policy Violations", "System Vulnerabilities"],
    default=["Cyber Attacks"]
)

# Advanced Analytics
st.sidebar.markdown("### Advanced Analytics")
if st.sidebar.button("Run Predictive Analysis"):
    st.sidebar.info("Analyzing trends and generating predictions...")

if st.sidebar.button("Generate Risk Score"):
    st.sidebar.success("Calculating organizational risk score...")
