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
    .library-header {
        font-size: 2rem;
        color: #000000;
        padding: 1rem 0;
        border-bottom: 2px solid #90EE90;
        margin-bottom: 2rem;
    }
    .resource-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
        transition: transform 0.3s ease;
    }
    .resource-card:hover {
        transform: translateY(-5px);
    }
    .search-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border: 1px solid #90EE90;
    }
    .category-header {
        color: #000000;
        border-bottom: 2px solid #FFD700;
        padding-bottom: 10px;
        margin: 20px 0;
    }
    .tag {
        background-color: rgba(144, 238, 144, 0.2);
        padding: 5px 10px;
        border-radius: 15px;
        margin: 2px;
        display: inline-block;
        font-size: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='library-header'>📚 Resource Library</h1>", unsafe_allow_html=True)
st.markdown("### Comprehensive Cybersecurity Resources for IGOs")

# Search and Filter Section
st.markdown("<div class='search-box'>", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    search_term = st.text_input("Search Resources", placeholder="Enter keywords...")
with col2:
    resource_type = st.selectbox(
        "Resource Type",
        ["All", "Policies", "Guidelines", "Templates", "Training"]
    )
st.markdown("</div>", unsafe_allow_html=True)

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "Security Policies", 
    "Best Practices", 
    "Training Materials",
    "Templates"
])

# Sample resource data
policies = [
    {
        "title": "Cybersecurity Policy Framework for IGOs",
        "type": "Policy",
        "date": "2024-02-15",
        "description": "Comprehensive policy framework aligned with international standards",
        "tags": ["policy", "framework", "compliance"],
        "format": "PDF"
    },
    {
        "title": "Data Protection Guidelines",
        "type": "Policy",
        "date": "2024-02-10",
        "description": "Guidelines for protecting sensitive diplomatic data",
        "tags": ["data protection", "privacy", "GDPR"],
        "format": "PDF"
    },
    {
        "title": "Incident Response Protocol",
        "type": "Policy",
        "date": "2024-02-05",
        "description": "Standard operating procedures for cyber incident response",
        "tags": ["incident response", "emergency", "procedures"],
        "format": "DOCX"
    }
]

best_practices = [
    {
        "title": "Secure Communication Guidelines",
        "type": "Guide",
        "date": "2024-02-20",
        "description": "Best practices for secure diplomatic communications",
        "tags": ["communication", "security", "encryption"],
        "format": "PDF"
    },
    {
        "title": "Remote Work Security Guide",
        "type": "Guide",
        "date": "2024-02-18",
        "description": "Security guidelines for remote diplomatic operations",
        "tags": ["remote work", "VPN", "security"],
        "format": "PDF"
    }
]

with tab1:
    st.markdown("<h3 class='category-header'>Security Policies</h3>", unsafe_allow_html=True)
    
    for policy in policies:
        if (search_term.lower() in policy['title'].lower() or 
            search_term.lower() in policy['description'].lower() or 
            any(search_term.lower() in tag for tag in policy['tags'])):
            
            st.markdown(f"""
                <div class='resource-card'>
                    <h4>{policy['title']} <span style='color: #90EE90'>({policy['format']})</span></h4>
                    <p>{policy['description']}</p>
                    <p><small>Last updated: {policy['date']}</small></p>
                    <p>
                        {' '.join([f"<span class='tag'>{tag}</span>" for tag in policy['tags']])}
                    </p>
                    <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                            border-radius: 5px; cursor: pointer;'>Download</button>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("<h3 class='category-header'>Best Practices</h3>", unsafe_allow_html=True)
    
    for practice in best_practices:
        if (search_term.lower() in practice['title'].lower() or 
            search_term.lower() in practice['description'].lower() or 
            any(search_term.lower() in tag for tag in practice['tags'])):
            
            st.markdown(f"""
                <div class='resource-card'>
                    <h4>{practice['title']} <span style='color: #90EE90'>({practice['format']})</span></h4>
                    <p>{practice['description']}</p>
                    <p><small>Last updated: {practice['date']}</small></p>
                    <p>
                        {' '.join([f"<span class='tag'>{tag}</span>" for tag in practice['tags']])}
                    </p>
                    <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                            border-radius: 5px; cursor: pointer;'>View Guide</button>
                </div>
            """, unsafe_allow_html=True)

with tab3:
    st.markdown("<h3 class='category-header'>Training Materials</h3>", unsafe_allow_html=True)
    
    # Training Modules Section
    st.markdown("""
        <div class='resource-card'>
            <h4>Cybersecurity Fundamentals for Diplomatic Staff</h4>
            <p>Interactive training module covering essential cybersecurity concepts</p>
            <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0;'>
                <p>Module Progress: 60%</p>
                <div style='background-color: #90EE90; width: 60%; height: 10px; border-radius: 5px;'></div>
            </div>
            <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                    border-radius: 5px; cursor: pointer;'>Continue Training</button>
        </div>
        
        <div class='resource-card'>
            <h4>Advanced Security Protocols</h4>
            <p>Comprehensive training on implementing security protocols</p>
            <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin: 10px 0;'>
                <p>Module Progress: 30%</p>
                <div style='background-color: #90EE90; width: 30%; height: 10px; border-radius: 5px;'></div>
            </div>
            <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                    border-radius: 5px; cursor: pointer;'>Start Module</button>
        </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("<h3 class='category-header'>Templates</h3>", unsafe_allow_html=True)
    
    templates = [
        {
            "title": "Incident Response Template",
            "description": "Standardized template for documenting and responding to security incidents",
            "format": "DOCX",
            "category": "Security"
        },
        {
            "title": "Risk Assessment Worksheet",
            "description": "Template for conducting comprehensive risk assessments",
            "format": "XLSX",
            "category": "Risk Management"
        },
        {
            "title": "Security Audit Checklist",
            "description": "Detailed checklist for security audits and assessments",
            "format": "PDF",
            "category": "Audit"
        }
    ]
    
    for template in templates:
        st.markdown(f"""
            <div class='resource-card'>
                <h4>{template['title']} <span style='color: #90EE90'>({template['format']})</span></h4>
                <p>{template['description']}</p>
                <p><span class='tag'>{template['category']}</span></p>
                <button style='background-color: #000000; color: white; border: none; padding: 5px 15px; 
                        border-radius: 5px; cursor: pointer;'>Download Template</button>
            </div>
        """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### Quick Access")
    st.markdown("""
        - 📋 Latest Policies
        - 📊 Security Guidelines
        - 📚 Training Modules
        - 🔍 Search All Resources
    """)
    
    st.markdown("### Resource Statistics")
    st.markdown("""
        <div style='padding: 10px; background-color: rgba(144, 238, 144, 0.1); border-radius: 5px;'>
            <p>Total Resources: 45</p>
            <p>Updated this month: 12</p>
            <p>Most accessed: Security Guidelines</p>
            <p>Last updated: {}</p>
        </div>
    """.format(datetime.now().strftime("%Y-%m-%d")), unsafe_allow_html=True)
    
    if st.button("Submit New Resource"):
        st.info("Resource submission form will open in a new window")
