import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub | IGO Security Monitor",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #000000;
        text-align: center;
        padding: 1rem;
        border-bottom: 2px solid #90EE90;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
    }
    .status-indicator {
        height: 10px;
        width: 10px;
        border-radius: 50%;
        display: inline-block;
        margin-right: 5px;
    }
    .status-active {
        background-color: #90EE90;
    }
    .status-warning {
        background-color: #FFD700;
    }
    .status-critical {
        background-color: #FF4444;
    }
    </style>
""", unsafe_allow_html=True)

# Authentication placeholder (to be implemented)
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown("<h1 class='main-header'>🔒 DiploCyber Hub</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        username = st.text_input("Username")
    with col2:
        password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Add proper authentication later
        if username and password:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Please enter both username and password")

else:
    # Main Dashboard
    st.markdown("<h1 class='main-header'>🔒 DiploCyber Hub</h1>", unsafe_allow_html=True)
    st.markdown("### Real-time Security Intelligence Dashboard")

    # Quick Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <h3>Threat Level</h3>
                <h2 style="color: #FFD700;">Elevated</h2>
                <p>↑ from Moderate</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <h3>Active Incidents</h3>
                <h2>12</h2>
                <p>3 Critical, 9 Moderate</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-card">
                <h3>Protected Assets</h3>
                <h2>156</h2>
                <p>All systems operational</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="metric-card">
                <h3>Security Score</h3>
                <h2 style="color: #90EE90;">87/100</h2>
                <p>↑ 5 points this week</p>
            </div>
        """, unsafe_allow_html=True)

    # Threat Map and Activity Feed
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Threat Map")
        # Sample data for the map
        df_threats = pd.DataFrame({
            'lat': [-1.2921, -1.3, -1.25, -1.28],
            'lon': [36.8219, 36.85, 36.82, 36.81],
            'size': [20, 15, 25, 10],
            'location': ['UN Complex', 'Regional HQ', 'Diplomatic Mission', 'Data Center']
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
    
    with col2:
        st.markdown("### Live Activity")
        activities = [
            {"time": "2 min ago", "event": "Suspicious login attempt", "severity": "critical"},
            {"time": "5 min ago", "event": "Firewall rule updated", "severity": "warning"},
            {"time": "10 min ago", "event": "System backup completed", "severity": "active"},
            {"time": "15 min ago", "event": "New security patch", "severity": "active"}
        ]
        
        for activity in activities:
            st.markdown(f"""
                <div class="metric-card">
                    <div><span class="status-indicator status-{activity['severity']}"></span>{activity['event']}</div>
                    <small>{activity['time']}</small>
                </div>
            """, unsafe_allow_html=True)

    # Threat Analysis
    st.markdown("### Threat Analysis")
    
    tab1, tab2 = st.tabs(["Threat Distribution", "Timeline Analysis"])
    
    with tab1:
        # Sample threat distribution data
        threat_types = ['Phishing', 'Malware', 'DDoS', 'Unauthorized Access', 'Data Breach']
        threat_counts = [45, 32, 28, 20, 15]

        fig = go.Figure(data=[
            go.Bar(
                x=threat_types,
                y=threat_counts,
                marker_color=['#FFD700', '#90EE90', '#000000', '#FFD700', '#90EE90']
            )
        ])

        fig.update_layout(
            title='Threat Distribution by Type',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Generate sample timeline data
        dates = pd.date_range(start='2024-01-01', end='2024-02-29', freq='D')
        incidents = [abs(10 + (i % 5) + (i % 3)) for i in range(len(dates))]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=dates,
            y=incidents,
            mode='lines+markers',
            line=dict(color='#FFD700', width=2),
            marker=dict(size=6, color='#000000')
        ))

        fig.update_layout(
            title='Incident Timeline',
            height=400
        )

        st.plotly_chart(fig, use_container_width=True)

    # Sidebar
    with st.sidebar:
        st.markdown("### Quick Actions")
        
        if st.button("Generate Report"):
            st.success("Generating comprehensive report...")
        
        if st.button("Run Security Scan"):
            st.info("Initiating security scan...")
        
        st.markdown("### System Status")
        st.markdown("""
            <div style="padding: 10px; background-color: rgba(144, 238, 144, 0.1); border-radius: 5px;">
                <p>🟢 Core Systems: Operational</p>
                <p>🟢 Database: Connected</p>
                <p>🟢 Security Monitoring: Active</p>
                <p>Last Updated: {}</p>
            </div>
        """.format(datetime.now().strftime("%H:%M:%S")), unsafe_allow_html=True)
        
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.rerun()
