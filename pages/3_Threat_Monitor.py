import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Threat Monitor | DiploCyber Hub",
    page_icon="🔍",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .threat-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .critical {
        border-left: 4px solid #FF0000;
    }
    .high {
        border-left: 4px solid #FFD700;
    }
    .medium {
        border-left: 4px solid #90EE90;
    }
    .low {
        border-left: 4px solid #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🔍 Threat Monitor")
st.markdown("### Real-time Cybersecurity Threat Intelligence")

# Create three columns for key metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="threat-card">
            <h3>Active Threats</h3>
            <h2 style="color: #FFD700;">23</h2>
            <p>↑ 15% from last week</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="threat-card">
            <h3>Threat Level</h3>
            <h2 style="color: #FFD700;">Elevated</h2>
            <p>Medium-High Risk</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="threat-card">
            <h3>Protected Assets</h3>
            <h2 style="color: #90EE90;">156</h2>
            <p>All systems operational</p>
        </div>
    """, unsafe_allow_html=True)

# Threat Map
st.markdown("### Global Threat Map")
# Sample data for the map
df_threats = pd.DataFrame({
    'lat': [-1.2921, -1.3, -1.25, -1.28],
    'lon': [36.8219, 36.85, 36.82, 36.81],
    'size': [20, 15, 25, 10],
    'location': ['IGO HQ', 'Regional Office', 'Diplomatic Mission', 'Data Center']
})

fig = px.scatter_mapbox(df_threats, 
                       lat='lat', 
                       lon='lon', 
                       size='size',
                       hover_name='location',
                       zoom=11)

fig.update_layout(
    mapbox_style="carto-positron",
    mapbox=dict(
        center=dict(lat=-1.2921, lon=36.8219),
    ),
    height=400,
    margin=dict(l=0, r=0, t=0, b=0)
)

st.plotly_chart(fig, use_container_width=True)

# Threat Timeline
st.markdown("### Threat Activity Timeline")

# Generate sample timeline data
dates = pd.date_range(start='2024-01-01', end='2024-02-29', freq='D')
threats = [abs(10 + (i % 5) + (i % 3)) for i in range(len(dates))]

fig_timeline = go.Figure()
fig_timeline.add_trace(go.Scatter(
    x=dates,
    y=threats,
    mode='lines+markers',
    line=dict(color='#FFD700', width=2),
    marker=dict(size=6, color='#000000')
))

fig_timeline.update_layout(
    title='Daily Threat Activity',
    xaxis_title='Date',
    yaxis_title='Number of Threats',
    height=300,
    margin=dict(l=20, r=20, t=40, b=20),
    plot_bgcolor='white'
)

st.plotly_chart(fig_timeline, use_container_width=True)

# Recent Alerts
st.markdown("### Recent Alerts")

alerts = [
    {
        "timestamp": "2024-02-29 14:23:00",
        "type": "Phishing Campaign",
        "severity": "High",
        "status": "Active",
        "details": "Targeted phishing campaign detected against diplomatic staff"
    },
    {
        "timestamp": "2024-02-29 13:15:00",
        "type": "Unauthorized Access Attempt",
        "severity": "Critical",
        "status": "Investigating",
        "details": "Multiple failed login attempts from suspicious IP addresses"
    },
    {
        "timestamp": "2024-02-29 12:30:00",
        "type": "Malware Detection",
        "severity": "Medium",
        "status": "Contained",
        "details": "Suspicious file quarantined by security system"
    }
]

for alert in alerts:
    severity_class = alert["severity"].lower()
    st.markdown(f"""
        <div class="threat-card {severity_class}">
            <h4>{alert["type"]}</h4>
            <p><strong>Severity:</strong> {alert["severity"]} | <strong>Status:</strong> {alert["status"]}</p>
            <p>{alert["details"]}</p>
            <p><small>{alert["timestamp"]}</small></p>
        </div>
    """, unsafe_allow_html=True)

# Sidebar with filters and controls
with st.sidebar:
    st.markdown("### Threat Filters")
    
    st.multiselect(
        "Threat Types",
        ["Phishing", "Malware", "DDoS", "Unauthorized Access", "Data Breach"],
        default=["Phishing", "Malware"]
    )
    
    st.slider(
        "Time Range",
        min_value=1,
        max_value=30,
        value=7,
        help="Show threats from the last X days"
    )
    
    st.selectbox(
        "Severity Level",
        ["All", "Critical", "High", "Medium", "Low"],
        index=0
    )
    
    # Quick Actions
    st.markdown("### Quick Actions")
    if st.button("Generate Threat Report"):
        st.success("Generating report...")
    
    if st.button("Export Alert Data"):
        st.success("Preparing export...")
