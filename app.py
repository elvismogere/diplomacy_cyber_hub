import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
    }
    .stButton button {
        background-color: #000000;
        color: #FFFFFF;
    }
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🔒 DiploCyber Hub")
    st.subheader("IGO Security Monitor")
    
    # Navigation
    page = st.radio(
        "Navigate to",
        ["Dashboard", "Risk Assessment", "Resource Library", "Threat Monitor"]
    )

# Main content
if page == "Dashboard":
    st.title("Diplomatic Cybersecurity Dashboard")
    st.markdown("### Real-time monitoring of cyber threats affecting IGOs in Kenya")
    
    # Key metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <h3 style="color: #000000;">Active Threats</h3>
                <h2 style="color: #FFD700;">12</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <h3 style="color: #000000;">Risk Level</h3>
                <h2 style="color: #90EE90;">Moderate</h2>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-card">
                <h3 style="color: #000000;">Protected IGOs</h3>
                <h2 style="color: #000000;">25</h2>
            </div>
        """, unsafe_allow_html=True)
    
    # Threat timeline
    st.markdown("### Recent Threat Activity")
    
    # Sample data
    dates = ["Jan 1", "Jan 15", "Feb 1", "Feb 15", "Mar 1"]
    threats = [5, 8, 12, 7, 10]
    
    # Create timeline chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=threats,
        mode='lines+markers',
        line=dict(color='#FFD700', width=2),
        marker=dict(size=8, color='#000000')
    ))
    
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=20, l=20, r=20, b=20),
        xaxis_title="Date",
        yaxis_title="Number of Threats",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent alerts section
    st.markdown("### Recent Alerts")
    
    alerts = [
        {"time": "2 hours ago", "type": "Phishing Attempt", "severity": "High"},
        {"time": "5 hours ago", "type": "Unauthorized Access", "severity": "Medium"},
        {"time": "1 day ago", "type": "Data Breach", "severity": "High"}
    ]
    
    for alert in alerts:
        severity_color = "#FFD700" if alert["severity"] == "High" else "#90EE90"
        st.markdown(f"""
            <div style="padding: 15px; margin: 10px 0; border-left: 4px solid {severity_color}; background-color: white;">
                <strong>{alert['type']}</strong><br/>
                {alert['time']} | Severity: {alert['severity']}
            </div>
        """, unsafe_allow_html=True)
