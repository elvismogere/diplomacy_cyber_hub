import streamlit as st
import json
from datetime import datetime
from config import (
    DEFAULT_SETTINGS, 
    UI_CONFIG, 
    SECURITY_CONFIG, 
    NOTIFICATION_CONFIG,
    EMAIL_CONFIG,
    APP_CONFIG
)

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub | Settings",
    page_icon="⚙️",
    layout="wide",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': f"{APP_CONFIG['name']} - Settings"
    }
)

# Custom styling
st.markdown("""
    <style>
    /* Main Layout */
    .main {
        background-color: var(--background-color);
        color: var(--text-color);
    }
    
    /* Settings Header */
    .settings-header {
        color: var(--text-color);
        font-size: 2.5rem;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(to right, rgba(144, 238, 144, 0.1), rgba(144, 238, 144, 0.2), rgba(144, 238, 144, 0.1));
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    /* Settings Cards */
    .settings-card {
        background-color: var(--card-background);
        border: 1px solid var(--border-color);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    
    /* Section Headers */
    .section-header {
        color: var(--text-color);
        border-bottom: 2px solid #90EE90;
        padding-bottom: 10px;
        margin: 20px 0;
    }
    
    /* Form Elements */
    .stTextInput>div>div>input,
    .stSelectbox>div>div>div {
        background-color: var(--background-color);
        color: var(--text-color);
        border-color: var(--border-color);
    }
    
    /* Dark mode */
    [data-theme="dark"] {
        --background-color: #1E1E1E;
        --text-color: #FFFFFF;
        --card-background: #2D2D2D;
        --border-color: #404040;
    }
    
    /* Light mode */
    [data-theme="light"] {
        --background-color: #FFFFFF;
        --text-color: #000000;
        --card-background: #FFFFFF;
        --border-color: #90EE90;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for settings
if 'settings' not in st.session_state:
    st.session_state.settings = DEFAULT_SETTINGS

# Header
st.markdown("<h1 class='settings-header'>⚙️ Settings</h1>", unsafe_allow_html=True)

# Create tabs for different settings categories
tab1, tab2, tab3, tab4 = st.tabs([
    "General Settings", 
    "Security", 
    "Notifications",
    "System"
])

with tab1:
    st.markdown("<h3 class='section-header'>General Settings</h3>", unsafe_allow_html=True)
    
    # Theme Selection
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Theme Settings")
    theme = st.selectbox(
        "Application Theme",
        ["Dark", "Light"],
        index=0 if st.session_state.settings['theme'] == 'dark' else 1
    )
    
    # Language Selection
    language = st.selectbox(
        "Language",
        ["English", "French", "Spanish", "Arabic"],
        index=0
    )
    
    # Timezone Selection
    timezone = st.selectbox(
        "Timezone",
        ["Africa/Nairobi", "UTC", "Europe/London", "US/Eastern"],
        index=0
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Profile Settings
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Profile Settings")
    organization = st.text_input("Organization Name", value=st.session_state.get('organization', ''))
    email = st.text_input("Contact Email", value=st.session_state.get('email', ''))
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Save General Settings"):
        st.session_state.settings['theme'] = theme.lower()
        st.session_state.settings['language'] = language
        st.success("Settings saved successfully!")

with tab2:
    st.markdown("<h3 class='section-header'>Security Settings</h3>", unsafe_allow_html=True)
    
    # Authentication Settings
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Authentication")
    
    mfa_enabled = st.toggle("Enable Two-Factor Authentication", value=SECURITY_CONFIG['mfa_enabled'])
    session_timeout = st.slider(
        "Session Timeout (minutes)",
        min_value=5,
        max_value=60,
        value=30
    )
    
    st.markdown("#### Password Policy")
    min_length = st.number_input(
        "Minimum Password Length",
        min_value=8,
        max_value=20,
        value=SECURITY_CONFIG['password_min_length']
    )
    require_special = st.checkbox("Require Special Characters", value=SECURITY_CONFIG['password_require_special'])
    require_numbers = st.checkbox("Require Numbers", value=SECURITY_CONFIG['password_require_numbers'])
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Save Security Settings"):
        st.success("Security settings updated successfully!")

with tab3:
    st.markdown("<h3 class='section-header'>Notification Settings</h3>", unsafe_allow_html=True)
    
    # Alert Settings
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Alert Preferences")
    
    alert_levels = st.multiselect(
        "Receive alerts for threat levels:",
        ["Critical", "High", "Medium", "Low"],
        default=["Critical", "High"]
    )
    
    notification_methods = st.multiselect(
        "Notification Methods:",
        ["Email", "In-App", "Browser"],
        default=["Email", "In-App"]
    )
    
    alert_frequency = st.select_slider(
        "Alert Frequency",
        options=["Real-time", "Hourly", "Daily", "Weekly"]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Quiet Hours
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Quiet Hours")
    enable_quiet_hours = st.checkbox("Enable Quiet Hours")
    if enable_quiet_hours:
        col1, col2 = st.columns(2)
        with col1:
            quiet_start = st.time_input("Start Time", value=datetime.strptime("22:00", "%H:%M").time())
        with col2:
            quiet_end = st.time_input("End Time", value=datetime.strptime("07:00", "%H:%M").time())
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("Save Notification Settings"):
        st.success("Notification preferences updated successfully!")

with tab4:
    st.markdown("<h3 class='section-header'>System Settings</h3>", unsafe_allow_html=True)
    
    # System Information
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### System Information")
    st.info(f"Version: {APP_CONFIG['version']}")
    st.info(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Data Management
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Data Management")
    
    data_retention = st.slider(
        "Data Retention Period (days)",
        min_value=30,
        max_value=365,
        value=90
    )
    
    backup_frequency = st.select_slider(
        "Backup Frequency",
        options=["Daily", "Weekly", "Monthly"]
    )
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Export Configuration
    st.markdown("<div class='settings-card'>", unsafe_allow_html=True)
    st.markdown("#### Configuration Management")
    
    if st.button("Export Settings"):
        settings_json = json.dumps(st.session_state.settings, indent=2)
        st.download_button(
            label="Download Settings File",
            data=settings_json,
            file_name=f"settings_{datetime.now().strftime('%Y%m%d')}.json",
            mime="application/json"
        )
    
    if st.button("Reset to Defaults"):
        st.session_state.settings = DEFAULT_SETTINGS.copy()
        st.success("Settings reset to defaults successfully!")
    st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Quick Actions")
    
    if st.button("Backup Settings"):
        st.success("Settings backed up successfully!")
    
    st.markdown("### Support")
    st.markdown("""
        <div class='settings-card'>
            Need help? Contact support:
            - 📧 support@diplocyber.com
            - 📞 +254 XXX XXX XXX
        </div>
    """, unsafe_allow_html=True)
