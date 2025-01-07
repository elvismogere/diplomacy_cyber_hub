import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta
import hashlib
import sqlite3
import os

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
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    /* Main Layout */
    .main {
        background-color: #1E1E1E;
        color: #FFFFFF;
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
    
    /* Rest of your existing styles */
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
    
    # Toggle between login and signup
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Switch to {}".format("Login" if st.session_state.signup_mode else "Sign Up")):
            st.session_state.signup_mode = not st.session_state.signup_mode
    
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

else:
    # Your existing dashboard code here
    [Rest of your existing dashboard code...]

    # Add logout button to sidebar
    with st.sidebar:
        if st.button("Logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()
