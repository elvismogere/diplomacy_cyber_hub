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
    layout="wide"
)

# Enhanced Custom styling with better visibility and contrast
st.markdown("""
    <style>
    /* Main Layout */
    .main {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    
    /* Headers - Ensuring all titles are visible */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        margin-bottom: 1rem;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-header {
        color: #FFFFFF !important;
        border-bottom: 2px solid #2E8B57;
        padding-bottom: 10px;
        margin: 20px 0;
        font-weight: 600;
    }
    
    /* Cards */
    .analytics-card {
        background-color: #2D2D2D;
        border: 1px solid #2E8B57;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    
    /* Improved Select Boxes */
    .stSelectbox > div > div {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
        border: 1px solid #2E8B57 !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #3CB371 !important;
    }
    
    /* Improved Multiselect */
    .stMultiSelect > div > div {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
        border: 1px solid #2E8B57 !important;
    }
    
    /* Selected Items in Multiselect */
    .stMultiSelect div[data-baseweb="tag"] {
        background-color: #2E8B57 !important;
        color: #FFFFFF !important;
        border-radius: 5px;
        padding: 2px 8px;
        margin: 2px;
    }
    
    /* Dropdown Items */
    div[data-baseweb="popover"] div[data-baseweb="menu"] {
        background-color: #2D2D2D !important;
    }
    
    div[data-baseweb="popover"] div[role="option"] {
        color: #FFFFFF !important;
    }
    
    div[data-baseweb="popover"] div[role="option"]:hover {
        background-color: #2E8B57 !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #2E8B57;
        color: #FFFFFF;
        border-radius: 5px;
        padding: 8px 16px;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    
    .stButton > button:hover {
        background-color: #3CB371;
        transform: translateY(-2px);
    }
    
    /* Charts */
    .js-plotly-plot .plotly .main-svg {
        background-color: transparent !important;
    }
    
    /* Metrics Row */
    .metric-row {
        background-color: #2D2D2D;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #2E8B57;
        margin: 10px 0;
    }
    
    /* Date Picker */
    .stDateInput > div {
        background-color: #2D2D2D !important;
        color: #FFFFFF !important;
        border: 1px solid #2E8B57 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border: none;
        color: #FFFFFF;
        font-weight: 500;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #2E8B57 !important;
        color: #FFFFFF !important;
        border-radius: 5px 5px 0 0;
    }
    
    /* Sidebar Improvements */
    .css-1d391kg {
        background-color: #1E1E1E;
    }
    
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
    }
    
    /* Text Elements */
    p, li, span {
        color: #FFFFFF !important;
    }
    </style>
""", unsafe_allow_html=True)
# Header with improved visibility
st.markdown("<h1 class='section-header' style='text-align: center;'>📊 Analytics & Reporting</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FFFFFF;'>Comprehensive Security Analytics Dashboard</h3>", unsafe_allow_html=True)

# Date Range Selector with improved styling
st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 2])
with col1:
    start_date = st.date_input("Start Date", datetime.now() - timedelta(days=30))
with col2:
    end_date = st.date_input("End Date", datetime.now())
st.markdown("</div>", unsafe_allow_html=True)

# Key Metrics Row with enhanced visibility
metrics_col1, metrics_col2, metrics_col3, metrics_col4 = st.columns(4)

with metrics_col1:
    st.markdown("""
        <div class="analytics-card">
            <h3>Total Incidents</h3>
            <h2 style="color: #FFD700;">247</h2>
            <p style="color: #90EE90;">↑ 12% from last month</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col2:
    st.markdown("""
        <div class="analytics-card">
            <h3>Resolution Rate</h3>
            <h2 style="color: #90EE90;">94%</h2>
            <p style="color: #90EE90;">↑ 3% improvement</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col3:
    st.markdown("""
        <div class="analytics-card">
            <h3>Avg Response Time</h3>
            <h2 style="color: #FFD700;">45min</h2>
            <p style="color: #90EE90;">↓ 15% faster</p>
        </div>
    """, unsafe_allow_html=True)

with metrics_col4:
    st.markdown("""
        <div class="analytics-card">
            <h3>Security Score</h3>
            <h2 style="color: #90EE90;">87/100</h2>
            <p style="color: #90EE90;">↑ 5 points</p>
        </div>
    """, unsafe_allow_html=True)

# Threat Analysis Section
st.markdown("<h2 class='section-header'>Threat Analysis</h2>", unsafe_allow_html=True)

# Create sample data for threats over time
dates = pd.date_range(start=start_date, end=end_date, freq='D')
threat_data = pd.DataFrame({
    'Date': dates,
    'Phishing': np.random.randint(5, 15, size=len(dates)),
    'Malware': np.random.randint(3, 10, size=len(dates)),
    'DDoS': np.random.randint(1, 5, size=len(dates)),
    'Unauthorized_Access': np.random.randint(2, 8, size=len(dates))
})

# Create stacked area chart with improved visibility
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
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FFFFFF'),
    legend=dict(
        bgcolor='rgba(0,0,0,0)',
        font=dict(color='#FFFFFF')
    )
)

st.plotly_chart(fig, use_container_width=True)

# Geographic Distribution
st.markdown("<h2 class='section-header'>Geographic Distribution of Threats</h2>", unsafe_allow_html=True)

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

fig_geo.update_layout(
    height=400,
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_geo, use_container_width=True)
# Security Metrics Section
st.markdown("<h2 class='section-header'>Security Metrics</h2>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Vulnerability Status with improved visibility
    labels = ['Resolved', 'In Progress', 'Open']
    values = [65, 25, 10]
    
    fig_vuln = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.3,
        marker_colors=['#2E8B57', '#FFD700', '#FF4444']
    )])
    
    fig_vuln.update_layout(
        title='Vulnerability Status Distribution',
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#FFFFFF'),
        showlegend=True,
        legend=dict(
            font=dict(color='#FFFFFF'),
            bgcolor='rgba(0,0,0,0)'
        )
    )
    
    st.plotly_chart(fig_vuln, use_container_width=True)

with col2:
    # Incident Response Times with enhanced visibility
    response_times = np.random.normal(45, 15, 100)
    
    fig_response = go.Figure(data=[go.Histogram(
        x=response_times,
        nbinsx=20,
        marker_color='#2E8B57'
    )])
    
    fig_response.update_layout(
        title='Incident Response Time Distribution (minutes)',
        xaxis_title='Response Time',
        yaxis_title='Frequency',
        height=300,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#FFFFFF')
    )
    
    st.plotly_chart(fig_response, use_container_width=True)

# Compliance & Policy Metrics
st.markdown("<h2 class='section-header'>Compliance & Policy Metrics</h2>", unsafe_allow_html=True)

compliance_data = {
    'Category': ['Data Protection', 'Access Control', 'Incident Response', 'Security Training', 'Network Security'],
    'Score': [92, 88, 95, 78, 85]
}

fig_compliance = go.Figure(data=[
    go.Bar(
        x=compliance_data['Category'],
        y=compliance_data['Score'],
        marker_color=['#2E8B57' if score >= 90 else '#FFD700' if score >= 80 else '#FF4444' 
                     for score in compliance_data['Score']]
    )
])

fig_compliance.update_layout(
    title='Compliance Scores by Category',
    yaxis_title='Compliance Score (%)',
    height=300,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#FFFFFF')
)

st.plotly_chart(fig_compliance, use_container_width=True)

# Report Generation Section with improved styling
st.markdown("<h2 class='section-header'>Report Generation</h2>", unsafe_allow_html=True)

report_col1, report_col2 = st.columns(2)

with report_col1:
    st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF;'>Custom Report Builder</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: #FFFFFF;'>Generate tailored security reports</p>", unsafe_allow_html=True)
    
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
    st.markdown("</div>", unsafe_allow_html=True)

with report_col2:
    st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF;'>Scheduled Reports</h4>", unsafe_allow_html=True)
    st.markdown("<p style='color: #FFFFFF;'>Configure automated report delivery</p>", unsafe_allow_html=True)
    
    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "Monthly", "Quarterly"]
    )
    
    recipients = st.text_input("Email Recipients (comma-separated)")
    
    if st.button("Schedule Reports"):
        st.success("Report schedule configured successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar with improved styling
with st.sidebar:
    st.markdown("<h3 style='color: #FFFFFF;'>Analytics Controls</h3>", unsafe_allow_html=True)
    
    # Filters with enhanced visibility
    st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF;'>Data Filters</h4>", unsafe_allow_html=True)
    
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
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Export Options
    st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF;'>Export Options</h4>", unsafe_allow_html=True)
    export_format = st.selectbox(
        "Export Format",
        ["PDF", "Excel", "CSV", "JSON"]
    )
    
    if st.button("Export Analytics"):
        st.success(f"Exporting data in {export_format} format...")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Advanced Analytics
    st.markdown("<div class='analytics-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #FFFFFF;'>Advanced Analytics</h4>", unsafe_allow_html=True)
    if st.button("Run Predictive Analysis"):
        st.info("Analyzing trends and generating predictions...")
    
    if st.button("Generate Risk Score"):
        st.success("Calculating organizational risk score...")
    st.markdown("</div>", unsafe_allow_html=True)
