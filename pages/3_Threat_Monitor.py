import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub | Threat Monitor",
    page_icon="🔍",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'DiploCyber Hub - Threat Monitor'
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
    
    /* Monitor Header */
    .monitor-header {
        color: #000000;
        font-size: 2.5rem;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(to right, #FFFFFF, #90EE90, #FFFFFF);
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    
    /* Threat card styling */
    .threat-card {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .threat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Severity indicators */
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
    
    /* Status indicators */
    .status-indicator {
        height: 10px;
        width: 10px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 5px;
    }
    
    .status-active {
        background-color: #FF0000;
        animation: pulse 2s infinite;
    }
    
    .status-investigating {
        background-color: #FFD700;
    }
    
    .status-resolved {
        background-color: #90EE90;
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
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
st.markdown("<h1 class='monitor-header'>🔍 Threat Monitor</h1>", unsafe_allow_html=True)
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
    'location': ['IGO HQ', 'Regional Office', 'Diplomatic Mission', 'Data Center'],
    'threat_level': ['High', 'Medium', 'Critical', 'Low']
})

fig = px.scatter_mapbox(df_threats, 
                       lat='lat', 
                       lon='lon', 
                       size='size',
                       color='threat_level',
                       hover_name='location',
                       color_discrete_map={
                           'Critical': '#FF0000',
                           'High': '#FFD700',
                           'Medium': '#90EE90',
                           'Low': '#000000'
                       },
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
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_timeline, use_container_width=True)

# Threat Distribution
st.markdown("### Threat Distribution")

# Sample data for threat types
threat_types = ['Phishing', 'Malware', 'DDoS', 'Unauthorized Access', 'Data Breach']
threat_counts = [45, 32, 28, 20, 15]

fig_dist = go.Figure(data=[
    go.Bar(
        x=threat_types,
        y=threat_counts,
        marker_color=['#FFD700', '#90EE90', '#FF0000', '#000000', '#FFD700']
    )
])

fig_dist.update_layout(
    title='Threat Types Distribution',
    xaxis_title='Threat Type',
    yaxis_title='Number of Incidents',
    height=300,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_dist, use_container_width=True)

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
    status_class = alert["status"].lower()
    st.markdown(f"""
        <div class="threat-card {severity_class}">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4>{alert["type"]}</h4>
                <span class="status-indicator status-{status_class}"></span>
            </div>
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
    
    # Real-time Monitoring Status
    st.markdown("### Monitoring Status")
    st.markdown("""
        <div class="threat-card">
            <p>🟢 Threat Detection: Active</p>
            <p>🟢 Alert System: Operational</p>
            <p>🟢 Data Collection: Running</p>
            <p>Last Updated: {}</p>
        </div>
    """.format(datetime.now().strftime("%H:%M:%S")), unsafe_allow_html=True)
