import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Resource Library | DiploCyber Hub",
    page_icon="📚",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .resource-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .category-header {
        color: #000000;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    .search-box {
        border: 2px solid #90EE90;
        border-radius: 5px;
        padding: 10px;
    }
    .document-link {
        color: #000000;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .document-link:hover {
        background-color: #90EE90;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📚 Resource Library")
st.markdown("### Comprehensive Cybersecurity Resources for IGOs")

# Search functionality
st.markdown("<div class='search-box'>", unsafe_allow_html=True)
search_term = st.text_input("Search Resources", placeholder="Enter keywords...")
st.markdown("</div>", unsafe_allow_html=True)

# Tabs for different resource categories
tab1, tab2, tab3, tab4 = st.tabs([
    "Policy Templates", 
    "Best Practices", 
    "Training Materials",
    "Emergency Procedures"
])

# Sample resource data
policy_documents = [
    {
        "title": "Cybersecurity Policy Template for IGOs",
        "type": "PDF",
        "date": "2024-01-15",
        "description": "Comprehensive policy template aligned with international standards",
        "tags": ["policy", "template", "governance"]
    },
    {
        "title": "Data Protection Guidelines",
        "type": "PDF",
        "date": "2024-01-10",
        "description": "Guidelines for protecting sensitive diplomatic data",
        "tags": ["data protection", "privacy", "guidelines"]
    },
    {
        "title": "Incident Response Protocol",
        "type": "DOCX",
        "date": "2024-01-05",
        "description": "Standard operating procedures for cyber incident response",
        "tags": ["incident response", "protocol", "emergency"]
    }
]

best_practices = [
    {
        "title": "Digital Diplomacy Security Guide",
        "type": "PDF",
        "date": "2024-01-20",
        "description": "Best practices for securing diplomatic communications",
        "tags": ["diplomacy", "security", "communications"]
    },
    {
        "title": "Zero Trust Architecture Implementation",
        "type": "PDF",
        "date": "2024-01-18",
        "description": "Guide to implementing zero trust security model",
        "tags": ["zero trust", "architecture", "implementation"]
    }
]

with tab1:
    st.markdown("<h3 class='category-header'>Policy Templates</h3>", unsafe_allow_html=True)
    
    for doc in policy_documents:
        if not search_term or any(term.lower() in doc['title'].lower() or term.lower() in doc['description'].lower() 
                                 for term in search_term.split()):
            st.markdown(f"""
                <div class='resource-card'>
                    <h4>{doc['title']} <span style='color: #90EE90'>({doc['type']})</span></h4>
                    <p>{doc['description']}</p>
                    <p><small>Last updated: {doc['date']}</small></p>
                    <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                            border-radius: 5px; cursor: pointer;'>Download</button>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h3 class='category-header'>Best Practices</h3>", unsafe_allow_html=True)
    
    for practice in best_practices:
        if not search_term or any(term.lower() in practice['title'].lower() or term.lower() in practice['description'].lower() 
                                 for term in search_term.split()):
            st.markdown(f"""
                <div class='resource-card'>
                    <h4>{practice['title']} <span style='color: #90EE90'>({practice['type']})</span></h4>
                    <p>{practice['description']}</p>
                    <p><small>Last updated: {practice['date']}</small></p>
                    <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                            border-radius: 5px; cursor: pointer;'>View Guide</button>
                </div>
            """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 class='category-header'>Training Materials</h3>", unsafe_allow_html=True)
    
    # Interactive Training Modules
    st.markdown("""
        <div class='resource-card'>
            <h4>Cybersecurity Fundamentals for Diplomatic Staff</h4>
            <p>Interactive training module covering basic cybersecurity concepts</p>
            <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0;'>
                <p>Module Progress: 60%</p>
                <div style='background-color: #90EE90; width: 60%; height: 10px; border-radius: 5px;'></div>
            </div>
            <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                    border-radius: 5px; cursor: pointer;'>Continue Training</button>
        </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("<h3 class='category-header'>Emergency Procedures</h3>", unsafe_allow_html=True)
    
    # Emergency Response Procedures
    st.markdown("""
        <div class='resource-card'>
            <h4>Emergency Response Playbook</h4>
            <p>Step-by-step procedures for handling cyber incidents</p>
            <ul>
                <li>Incident Classification Guidelines</li>
                <li>Communication Templates</li>
                <li>Response Team Contact Information</li>
                <li>Recovery Procedures</li>
            </ul>
            <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                    border-radius: 5px; cursor: pointer;'>Access Playbook</button>
        </div>
    """, unsafe_allow_html=True)

# Quick Access Section
st.sidebar.markdown("### Quick Access")
st.sidebar.markdown("""
- 📋 Latest Policies
- 📊 Security Guidelines
- 📚 Training Modules
- 🚨 Emergency Contacts
""")

# Resource Statistics
st.sidebar.markdown("### Resource Statistics")
st.sidebar.markdown("""
- Total Documents: 45
- Updated this month: 12
- Most accessed: Security Guidelines
""")

# Download All Resources Option
st.sidebar.markdown("### Bulk Download")
if st.sidebar.button("Download All Resources"):
    st.sidebar.success("Preparing download package...")
