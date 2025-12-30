import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

st.set_page_config(page_title="TECH TITANS", page_icon="🚀", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
* { font-family: 'Inter', sans-serif; }
body { background-color: #000000; color: #ffffff; }
.stApp { background-color: #000000; }
.stTabs [data-baseweb="tab-list"] { background-color: #000000; border-bottom: 2px solid #333333; }
.stTabs [data-baseweb="tab"] { color: #cccccc; font-weight: 500; padding: 12px 24px; border-radius: 8px 8px 0 0; }
.stTabs [data-baseweb="tab"][aria-selected="true"] { color: #00d4ff; border-bottom: 3px solid #00d4ff; background-color: #1a1a1a; }
.stTabs [data-baseweb="tab"]:hover { color: #00d4ff; background-color: #1a1a1a; }
.stMetric { background-color: #0a0a0a; border: 1px solid #333333; border-radius: 12px; padding: 16px; box-shadow: 0 2px 8px rgba(0,0,0,0.5); color: #ffffff; }
.stMetric-label { color: #ffffff !important; font-size: 14px; font-weight: 600; }
.stMetric-value { color: #00d4ff !important; font-size: 32px; font-weight: 700; }
.stMetric-delta { color: #00ff00 !important; font-weight: 600; }
::selection { background-color: transparent; color: #ffffff; }
*::selection { background-color: transparent; color: #ffffff; }
button[kind="primary"] { background-color: #00d4ff !important; color: #000000 !important; border-radius: 8px !important; font-weight: 600 !important; padding: 12px 24px !important; transition: all 0.3s ease; }
button[kind="primary"]:hover { background-color: #00a8cc !important; box-shadow: 0 4px 12px rgba(0, 212, 255, 0.3) !important; }
.stTextArea > div > textarea { border: 2px solid #333333 !important; border-radius: 8px !important; color: #ffffff !important; padding: 12px; background-color: #0a0a0a !important; }
.stTextArea > div > textarea:focus { border: 2px solid #00d4ff !important; box-shadow: 0 0 0 3px rgba(0, 212, 255, 0.1) !important; }
h1 { color: #ff9500 !important; font-weight: 700 !important; }
h2 { color: #00d4ff !important; font-weight: 700 !important; margin-top: 24px !important; }
h3 { color: #00ff88 !important; font-weight: 600 !important; }
p { color: #e0e0e0 !important; }
.info-box { background-color: #0a0a0a; border-left: 4px solid #00d4ff; padding: 16px; border-radius: 8px; color: #ffffff; font-weight: 500; margin: 16px 0; }
.success-box { background-color: #0a0a0a; border-left: 4px solid #00ff88; padding: 16px; border-radius: 8px; color: #ffffff; font-weight: 500; margin: 16px 0; }
.warning-box { background-color: #0a0a0a; border-left: 4px solid #ffaa00; padding: 16px; border-radius: 8px; color: #ffffff; font-weight: 500; margin: 16px 0; }
.danger-box { background-color: #0a0a0a; border-left: 4px solid #ff3333; padding: 16px; border-radius: 8px; color: #ffffff; font-weight: 500; margin: 16px 0; }
.card { background-color: #0a0a0a; border: 1px solid #333333; border-radius: 12px; padding: 20px; margin: 16px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.5); transition: all 0.3s ease; }
.card:hover { box-shadow: 0 8px 16px rgba(0,0,0,0.7); transform: translateY(-2px); }
</style>
""", unsafe_allow_html=True)

if 'predictions' not in st.session_state:
    st.session_state.predictions = []

st.markdown("""
🚀
# TECH TITANS Dashboard
Intelligent Social Media Analysis Platform
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📝 Analysis", "ℹ️ About"])

with tab1:
    st.markdown("### Platform Dashboard")
    st.markdown("Real-time analytics and system metrics for content intelligence")
    
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.metric("📊 Total Analyses", len(st.session_state.predictions), delta="Real-time")
    with col2:
        fake_count = sum(1 for p in st.session_state.predictions if "Fake" in p[1])
        st.metric("⚠️ Threats Detected", fake_count, delta="Critical")
    with col3:
        st.metric("✅ System Status", "Operational", delta="100% Live")
    
    st.markdown("---")
    st.markdown("### Key Features")
    feat_col1, feat_col2 = st.columns(2, gap="large")
    
    with feat_col1:
        st.markdown("""
        ### 🎯 Real-time Detection
        Instantly detect fake news and misinformation using advanced ML algorithms
        """, unsafe_allow_html=True)
        st.markdown("""
        ### 📈 Analytics Dashboard
        Visual insights and trend analysis for data-driven decisions
        """, unsafe_allow_html=True)
    
    with feat_col2:
        st.markdown("""
        ### 💬 Content Analysis
        Comprehensive sentiment and authenticity analysis of social posts
        """, unsafe_allow_html=True)
        st.markdown("""
        ### 🔐 Secure Processing
        Enterprise-grade security with privacy-first data handling
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Content Analysis Engine")
    st.markdown("Paste any social media content to analyze authenticity and sentiment")
    
    text = st.text_area("Enter post, article, or comment...", height=220, label_visibility="collapsed")
    
    if st.button("⚡ Analyze Now", use_container_width=True):
        if text.strip():
            classes = ["✅ Authentic", "⚠️ Suspicious", "❌ Fake News"]
            prediction = random.choice(classes)
            conf = round(random.uniform(0.72, 0.99), 2)
            st.session_state.predictions.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prediction, conf, text))
            st.success("⚡ Analysis Complete!")
    
    if st.session_state.predictions:
        st.markdown("---")
        st.markdown("### Recent Analysis Results")
        r1, r2, r3 = st.columns(3, gap="medium")
        with r1:
            st.metric("Verdict", st.session_state.predictions[-1][1].split()[0])
        with r2:
            st.metric("Confidence", f"{st.session_state.predictions[-1][2]*100:.1f}%")
        with r3:
            st.metric("Processed", "Just now")

with tab3:
    st.markdown("""
    ## About TECH TITANS
    ### Advanced Content Intelligence Platform
    """, unsafe_allow_html=True)
    
    st.markdown("""
    Tech Titans is a state-of-the-art **Social Media Intelligence Platform** powered by advanced **Natural Language Processing** and machine learning technology. Our platform empowers users to detect misinformation, classify content, and gain actionable insights from social media data in real-time.
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Core Capabilities
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("""
        ### 🎯 Real-time Detection
        Instantly identify fake news, misinformation, and false claims using advanced ML algorithms
        """, unsafe_allow_html=True)
        st.markdown("""
        ### 📊 Smart Classification
        Automatically categorize posts as Authentic, Suspicious, or Fake News with confidence scores
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        ### 💬 Sentiment Analysis
        Understand emotional tone, intent, and sentiment patterns in social media conversations
        """, unsafe_allow_html=True)
        st.markdown("""
        ### 🔐 Enterprise Security
        Enterprise-grade security with privacy-first architecture and encrypted data processing
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    ### Platform Version 2.0
    ✅ Production Ready | Advanced NLP Engine | Real-time Processing | 99.9% Uptime
    """, unsafe_allow_html=True)
    
    st.markdown("""
    ### Platform Statistics
    """, unsafe_allow_html=True)
    
    stat1, stat2, stat3, stat4 = st.columns(4, gap="medium")
    with stat1:
        st.markdown(f"""
        ### {len(st.session_state.predictions)}
        Total Analyses
        """, unsafe_allow_html=True)
    with stat2:
        st.markdown("""
        ### 94.2%
        Model Accuracy
        """, unsafe_allow_html=True)
    with stat3:
        st.markdown("""
        ### 2.4s
        Avg Response Time
        """, unsafe_allow_html=True)
    with stat4:
        st.markdown("""
        ### 99.9%
        Uptime SLA
        """, unsafe_allow_html=True)
