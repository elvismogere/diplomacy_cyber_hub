import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Risk Assessment | DiploCyber Hub",
    page_icon="🎯",
    layout="wide"
)

# Custom styling
st.markdown("""
    <style>
    .risk-card {
        background-color: #FFFFFF;
        border: 1px solid #90EE90;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .high-risk {
        border-left: 4px solid #FFD700;
    }
    .medium-risk {
        border-left: 4px solid #90EE90;
    }
    .low-risk {
        border-left: 4px solid #000000;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🎯 Cybersecurity Risk Assessment")
st.markdown("### Evaluate and monitor security risks for your organization")

# Main content
tab1, tab2, tab3 = st.tabs(["Quick Assessment", "Detailed Analysis", "Risk Matrix"])

with tab1:
    st.markdown("### Quick Risk Assessment")
    
    # Organization Info
    col1, col2 = st.columns(2)
    with col1:
        org_name = st.text_input("Organization Name")
        dept_name = st.text_input("Department")
    with col2:
        assessment_date = st.date_input("Assessment Date")
        assessor_name = st.text_input("Assessor Name")

    # Risk Categories
    st.markdown("### Risk Categories")
    
    # Data Security
    st.markdown("#### 1. Data Security")
    data_encryption = st.select_slider(
        "Data Encryption Level",
        options=["None", "Basic", "Standard", "Advanced", "Military-Grade"],
        value="Standard"
    )
    
    data_access = st.select_slider(
        "Access Control Measures",
        options=["Minimal", "Basic", "Standard", "Strong", "Very Strong"],
        value="Standard"
    )

    # Network Security
    st.markdown("#### 2. Network Security")
    firewall_status = st.select_slider(
        "Firewall Protection",
        options=["None", "Basic", "Standard", "Advanced", "Enterprise"],
        value="Standard"
    )
    
    vpn_usage = st.select_slider(
        "VPN Implementation",
        options=["None", "Partial", "Standard", "Full", "Advanced"],
        value="Standard"
    )

    # Calculate Risk Score
    if st.button("Calculate Risk Score"):
        # Convert responses to numerical values
        encryption_score = {"None": 1, "Basic": 2, "Standard": 3, "Advanced": 4, "Military-Grade": 5}
        access_score = {"Minimal": 1, "Basic": 2, "Standard": 3, "Strong": 4, "Very Strong": 5}
        firewall_score = {"None": 1, "Basic": 2, "Standard": 3, "Advanced": 4, "Enterprise": 5}
        vpn_score = {"None": 1, "Partial": 2, "Standard": 3, "Full": 4, "Advanced": 5}

        # Calculate total score
        total_score = (encryption_score[data_encryption] + access_score[data_access] + 
                      firewall_score[firewall_status] + vpn_score[vpn_usage]) / 4

        # Display results
        st.markdown("### Assessment Results")
        
        # Risk level determination
        if total_score >= 4:
            risk_level = "Low Risk"
            color = "#90EE90"
        elif total_score >= 3:
            risk_level = "Medium Risk"
            color = "#FFD700"
        else:
            risk_level = "High Risk"
            color = "#FF0000"

        # Display score and recommendations
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
                <div class="risk-card">
                    <h2 style="color: {color};">{risk_level}</h2>
                    <h3>Score: {total_score:.2f}/5.00</h3>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="risk-card">
                    <h3>Key Recommendations:</h3>
                    <ul>
                        <li>Enhance data encryption measures</li>
                        <li>Strengthen access controls</li>
                        <li>Update firewall configurations</li>
                        <li>Implement comprehensive VPN solution</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Detailed Risk Analysis")
    st.info("This section provides in-depth analysis tools for comprehensive risk assessment.")
    # Detailed analysis content will be added in next iteration

with tab3:
    st.markdown("### Risk Matrix")
    # Create sample risk matrix using plotly
    fig = go.Figure()

    # Add risk zones
    fig.add_trace(go.Scatter(
        x=[1, 2, 3, 4, 5],
        y=[1, 2, 3, 4, 5],
        mode='markers',
        marker=dict(
            size=30,
            color=['#90EE90', '#90EE90', '#FFD700', '#FFD700', '#FF0000'],
            symbol='square'
        ),
        name='Risk Zones'
    ))

    fig.update_layout(
        title='Risk Assessment Matrix',
        xaxis_title='Impact',
        yaxis_title='Likelihood',
        showlegend=False,
        width=600,
        height=600
    )

    st.plotly_chart(fig)

# Download Report Option
st.download_button(
    label="Download Risk Assessment Report",
    data="Risk Assessment Report Content",  # This would be replaced with actual report content
    file_name=f"risk_assessment_{datetime.now().strftime('%Y%m%d')}.pdf",
    mime="application/pdf"
)
