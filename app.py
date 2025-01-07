import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import hashlib
import sqlite3
import os
from config import UI_CONFIG, APP_CONFIG

# Initialize database
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, 
                  password TEXT,
                  organization TEXT,
                  email TEXT,
                  created_date TEXT)''')
    conn.commit()
    conn.close()

# Hash password
def make_hashed_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Check password
def check_password(password, hashed_password):
    if make_hashed_password(password) == hashed_password:
        return True
    return False

# Add user to database
def add_user(username, password, organization, email):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    hashed_password = make_hashed_password(password)
    try:
        c.execute("INSERT INTO users VALUES (?,?,?,?,?)", 
                 (username, hashed_password, organization, email, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Verify user
def verify_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    if result is not None:
        return check_password(password, result[0])
    return False

# Initialize database
init_db()

# Page configuration
st.set_page_config(
    page_title="DiploCyber Hub | Home",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': 'DiploCyber Hub - Home'
    }
)
# Hide default menu and rename app to Home
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* Rename app to Home in navigation */
    section[data-testid="stSidebar"] .css-1d391kg .css-1oe5cao {visibility: hidden;}
    section[data-testid="stSidebar"] .css-1d391kg .css-1oe5cao::before {
        content: "🏠 Home";
        visibility: visible;
        color: white;
        margin-left: 20px;
    }
    
    /* Main Layout */
    .main {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }
    
    /* Auth Forms */
    .auth-form {
        background-color: #2D2D2D;
        padding: 30px;
        border-radius: 10px;
        border: 1px solid #90EE90;
        margin: 20px 0;
    }
    
    .auth-header {
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Cards */
    .metric-card {
        background-color: #2D2D2D;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
        color: #FFFFFF;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Status Indicators */
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
    
    /* Buttons */
    .stButton>button {
        background-color: #2E8B57;  /* Darker green */
        color: #FFFFFF;
        border-radius: 5px;
        padding: 8px 16px;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #3CB371;
        transform: translateY(-2px);
    }
    
    /* Auth toggle button */
    .auth-toggle-button>button {
        background-color: transparent !important;
        color: #90EE90 !important;
        border: none;
        text-decoration: underline;
        width: auto;
        padding: 0;
    }
    
    .auth-toggle-button>button:hover {
        background-color: transparent !important;
        transform: none;
        color: #7BC47B !important;
    }
    
    /* Inputs */
    .stTextInput>div>div>input {
        background-color: #2D2D2D;
        color: #FFFFFF;
        border-color: #404040;
    }
    
    /* Selectbox */
    .stSelectbox>div>div {
        background-color: #2D2D2D;
        color: #FFFFFF;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #1E1E1E;
    }
    
    /* Charts */
    .js-plotly-plot .plotly .main-svg {
        background-color: transparent !important;
    }
    
    /* Links */
    a {
        color: #90EE90 !important;
    }
    
    /* Text */
    p, li, span {
        color: #FFFFFF;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        border: none;
        color: #FFFFFF;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #90EE90 !important;
        color: #000000 !important;
        border-radius: 5px 5px 0 0;
    }
    </style>
""", unsafe_allow_html=True)

# Session state initialization
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = None
if 'signup_mode' not in st.session_state:
    st.session_state.signup_mode = False
# Authentication section
if not st.session_state.authenticated:
    st.markdown("<h1 style='text-align: center; color: #FFFFFF;'>🔒 DiploCyber Hub</h1>", unsafe_allow_html=True)
    
    if st.session_state.signup_mode:
        # Signup Form
        with st.form("signup_form"):
            st.markdown("<h2 class='auth-header'>Create Account</h2>", unsafe_allow_html=True)
            new_username = st.text_input("Username")
            new_password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            organization = st.text_input("Organization")
            email = st.text_input("Email")
            
            signup_submitted = st.form_submit_button("Sign Up")
            
            if signup_submitted:
                if new_password != confirm_password:
                    st.error("Passwords do not match!")
                elif not new_username or not new_password or not organization or not email:
                    st.error("All fields are required!")
                else:
                    if add_user(new_username, new_password, organization, email):
                        st.success("Account created successfully! Please log in.")
                        st.session_state.signup_mode = False
                        st.rerun()
                    else:
                        st.error("Username already exists!")
        
        # Toggle to login
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<div class='auth-toggle-button'>", unsafe_allow_html=True)
            if st.button("Already have an account? Login"):
                st.session_state.signup_mode = False
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        # Login Form
        with st.form("login_form"):
            st.markdown("<h2 class='auth-header'>Login</h2>", unsafe_allow_html=True)
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            login_submitted = st.form_submit_button("Login")
            
            if login_submitted:
                if verify_user(username, password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid username or password")
        
        # Toggle to signup
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.markdown("<div class='auth-toggle-button'>", unsafe_allow_html=True)
            if st.button("Don't have an account? Sign Up"):
                st.session_state.signup_mode = True
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

else:
    # Main Dashboard content (the rest of your dashboard code remains the same)
    [Previous dashboard code continues here...]
