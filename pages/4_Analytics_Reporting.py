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
