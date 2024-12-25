import streamlit as st

def apply_custom_theme():
    """Apply custom theme to the application"""
    # Primary Theme Colors
    primary_colors = {
        "background": "#FFFFFF",
        "text": "#000000",
        "accent": "#90EE90",
        "highlight": "#FFD700"
    }
    
    # Custom Theme CSS
    st.markdown("""
        <style>
        /* Main Layout */
        .main {
            background-color: #FFFFFF;
            padding: 2rem;
        }
        
        /* Navigation */
        .sidebar .sidebar-content {
            background-color: #000000;
            color: #FFFFFF;
            padding: 2rem 1rem;
        }
        
        /* Cards and Containers */
        .stCard {
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        
        .stCard:hover {
            transform: translateY(-5px);
        }
        
        /* Typography */
        h1, h2, h3 {
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 600;
            color: #000000;
        }
        
        /* Interactive Elements */
        .stButton>button {
            background-color: #000000;
            color: #FFFFFF;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        
        .stButton>button:hover {
            background-color: #90EE90;
            color: #000000;
        }
        
        /* Data Visualization */
        .plot-container {
            background-color: #FFFFFF;
            border-radius: 10px;
            padding: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        
        /* Alerts and Notifications */
        .alert {
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .alert-success {
            background-color: rgba(144, 238, 144, 0.1);
            border-left: 4px solid #90EE90;
        }
        
        .alert-warning {
            background-color: rgba(255, 215, 0, 0.1);
            border-left: 4px solid #FFD700;
        }
        
        /* Forms and Inputs */
        .stTextInput>div>div>input {
            border-radius: 5px;
            border: 1px solid #E0E0E0;
        }
        
        .stTextInput>div>div>input:focus {
            border-color: #90EE90;
            box-shadow: 0 0 0 2px rgba(144, 238, 144, 0.2);
        }
        
        /* Tables */
        .dataframe {
            border: none !important;
            border-radius: 10px;
            overflow: hidden;
        }
        
        .dataframe th {
            background-color: #000000;
            color: #FFFFFF;
            padding: 12px;
        }
        
        /* Loading States */
        .stProgress > div > div > div > div {
            background-color: #90EE90;
        }
        </style>
    """, unsafe_allow_html=True)
