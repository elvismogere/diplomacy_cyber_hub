import streamlit as st
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Settings | DiploCyber Hub",
    page_icon="⚙️",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .settings-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .section-header {
        color: #000000;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .success-message {
        color: #90EE90;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .warning-message {
        color: #FFD700;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("⚙️ Settings")
st.markdown("### System Configuration and Preferences")

# Create tabs for different settings categories
tab1, tab2, tab3, tab4 = st.tabs([
    "Organization Profile", 
    "Security Settings", 
    "Notification Preferences",
    "System Configuration"
])

with tab1:
    st.markdown("<h3 class='section-header'>Organization Profile</h3>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
        org_name = st.text_input("Organization Name", "UN Agency")
        org_type = st.selectbox(
            "Organization Type",
            ["UN Agency", "Regional IGO", "Diplomatic Mission", "International NGO"]
        )
        country = st.selectbox("Country", ["Kenya", "Tanzania", "Uganda", "Rwanda", "Ethiopia"])
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
        primary_contact = st.text_input("Primary Contact Name")
        contact_email = st.text_input("Contact Email")
        phone = st.text_input("Phone Number")
        st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Update Profile"):
        st.success("Organization profile updated successfully!")

with tab2:
    st.markdown("<h3 class='section-header'>Security Settings</h3>", unsafe_allow_html=True)
    
    # Authentication Settings
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Authentication Settings")
    
    mfa_enabled = st.toggle("Enable Multi-Factor Authentication", value=True)
    session_timeout = st.slider("Session Timeout (minutes)", 5, 60, 30)
    password_expiry = st.slider("Password Expiry (days)", 30, 180, 90)
    
    st.markdown("#### Password Policy")
    min_length = st.number_input("Minimum Password Length", 8, 20, 12)
    require_special = st.checkbox("Require Special Characters", value=True)
    require_numbers = st.checkbox("Require Numbers", value=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Access Control
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Access Control")
    
    ip_whitelist = st.text_area("IP Whitelist (one per line)")
    allowed_domains = st.text_input("Allowed Email Domains (comma-separated)")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Save Security Settings"):
        st.success("Security settings updated successfully!")

with tab3:
    st.markdown("<h3 class='section-header'>Notification Preferences</h3>", unsafe_allow_html=True)
    
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Alert Settings")
    
    alert_levels = st.multiselect(
        "Receive alerts for threat levels:",
        ["Critical", "High", "Medium", "Low"],
        default=["Critical", "High"]
    )
    
    notification_methods = st.multiselect(
        "Notification Methods:",
        ["Email", "SMS", "In-App", "Webhook"],
        default=["Email", "In-App"]
    )
    
    alert_frequency = st.select_slider(
        "Alert Frequency",
        options=["Real-time", "Hourly", "Daily", "Weekly"]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Custom Alerts
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Custom Alert Rules")
    
    if st.button("Add Custom Alert Rule"):
        st.info("Custom alert rule configuration will be available in the next update.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Save Notification Settings"):
        st.success("Notification preferences updated successfully!")

with tab4:
    st.markdown("<h3 class='section-header'>System Configuration</h3>", unsafe_allow_html=True)
    
    # Data Management
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Data Management")
    
    data_retention = st.slider("Data Retention Period (days)", 30, 365, 180)
    backup_frequency = st.select_slider(
        "Backup Frequency",
        options=["Daily", "Weekly", "Monthly"]
    )
    
    st.markdown("#### System Integration")
    api_key = st.text_input("API Key", type="password")
    webhook_url = st.text_input("Webhook URL")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Advanced Settings
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Advanced Settings")
    
    debug_mode = st.checkbox("Enable Debug Mode")
    analytics_tracking = st.checkbox("Enable Analytics Tracking", value=True)
    
    if st.button("Export Configuration"):
        st.download_button(
            label="Download Configuration File",
            data=json.dumps({
                "organization": org_name,
                "security_settings": {
                    "mfa_enabled": mfa_enabled,
                    "session_timeout": session_timeout
                },
                "notification_settings": {
                    "alert_levels": alert_levels,
                    "methods": notification_methods
                }
            }),
            file_name=f"config_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar with quick actions
with st.sidebar:
    st.markdown("### Quick Actions")
    
    if st.button("Reset to Defaults"):
        st.warning("This will reset all settings to default values.")
        
    if st.button("Backup Settings"):
        st.success("Settings backed up successfully!")
    
    st.markdown("### System Status")
    st.info("System Version: 1.0.0")
    st.info("Last Updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Support Section
    st.markdown("### Support")
    st.markdown("""
        Need help? Contact support:
        - 📧 support@diplocyber.com
        - 📞 +254 XXX XXX XXX
    """)
