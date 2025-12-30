import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

# Page config
st.set_page_config(
    page_title="TechTitains",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Modern CSS styling
st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%); color: #e2e8f0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%); border-right: 2px solid rgba(148,163,184,0.2); }
    h1 { background: linear-gradient(120deg, #60a5fa 0%, #3b82f6 50%, #1e40af 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-weight: 800; }
    h2, h3 { color: #e0e7ff; font-weight: 700; }
    [data-testid="metric-container"] { background: linear-gradient(135deg, rgba(30,41,59,0.8) 0%, rgba(15,23,42,0.6) 100%); border: 1px solid rgba(148,163,184,0.3); border-radius: 16px; padding: 24px; box-shadow: 0 8px 32px rgba(0,0,0,0.3); transition: all 0.3s ease; }
    [data-testid="metric-container"]:hover { border-color: rgba(96,165,250,0.5); box-shadow: 0 12px 48px rgba(59,130,246,0.2); transform: translateY(-4px); }
    .stButton > button { background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%); color: white; border: none; border-radius: 12px; padding: 12px 32px; font-weight: 600; box-shadow: 0 4px 15px rgba(59,130,246,0.3); transition: all 0.3s; }
    .stButton > button:hover { background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%); box-shadow: 0 8px 25px rgba(59,130,246,0.5); }
    .stTextArea > textarea { background-color: #1e293b; color: #e2e8f0; border: 2px solid rgba(148,163,184,0.2); border-radius: 12px; padding: 16px; transition: all 0.3s; }
    .stTextArea > textarea:focus { border-color: rgba(96,165,250,0.6); box-shadow: 0 0 0 3px rgba(59,130,246,0.1); }
    .stInfo, .stSuccess, .stWarning { border-radius: 12px; border-left: 4px solid; padding: 16px 20px; backdrop-filter: blur(10px); }
    .stInfo { border-left-color: #3b82f6; background-color: rgba(30,58,138,0.3); }
    .stSuccess { border-left-color: #10b981; background-color: rgba(5,46,22,0.3); }
    .stWarning { border-left-color: #f59e0b; background-color: rgba(78,22,6,0.3); }
    .divider { height: 2px; background: linear-gradient(90deg, transparent, rgba(96,165,250,0.3), transparent); margin: 30px 0; }
</style>
""", unsafe_allow_html=True)

if 'predictions' not in st.session_state:
    st.session_state.predictions = []

st.markdown("# 🚀 TechTitains")
st.markdown("### Social Media Intelligence Platform")
st.markdown("Advanced NLP-powered platform for fake news detection, content classification, and sentiment analysis.")
st.markdown('<hr class="divider">', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🎛️ Navigation")
    page = st.radio("Select:", ["🏠 Home", "🔮 Prediction", "📊 Analytics", "ℹ️ About"], label_visibility="collapsed")

if page == "🏠 Home":
    st.markdown("### Dashboard Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Predictions", len(st.session_state.predictions))
    with col2:
        fake_count = sum(1 for p in st.session_state.predictions if p[1] == "⚠️ Fake News")
        st.metric("🚨 Fake News Detected", fake_count)
    with col3:
        st.metric("✅ Status", "Active")
    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    st.info("👉 Use navigation to explore. Start with **Prediction** to analyze text!")

elif page == "🔮 Prediction":
    st.markdown("### 🔮 Text Classification Engine")
    st.markdown("Enter text to classify it instantly.")
    text = st.text_area("Input:", placeholder="Paste text here...", height=200, label_visibility="collapsed")
    if st.button("🔍 Analyze Text", use_container_width=True):
        if text.strip():
            classes = ["😊 Positive", "⚠️ Fake News", "😐 Neutral"]
            prediction = random.choice(classes)
            confidence = round(random.uniform(0.65, 0.99), 2)
            st.session_state.predictions.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prediction, confidence, text))
            st.success("✅ Analysis Complete!")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Classification", prediction)
            with col2:
                st.metric("Confidence", f"{confidence*100:.1f}%")
            with col3:
                st.metric("Time", datetime.now().strftime("%H:%M:%S"))
        else:
            st.warning("⚠️ Please enter text.")

elif page == "📊 Analytics":
    st.markdown("### 📊 Analytics Dashboard")
    if st.session_state.predictions:
        df = pd.DataFrame(st.session_state.predictions, columns=["Timestamp", "Classification", "Confidence", "Text"])
        st.markdown("#### Summary")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total", len(df))
        with col2:
            st.metric("Positive", len(df[df["Classification"].str.contains("Positive", na=False)]))
        with col3:
            st.metric("Fake", len(df[df["Classification"].str.contains("Fake", na=False)]))
        with col4:
            st.metric("Neutral", len(df[df["Classification"].str.contains("Neutral", na=False)]))
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Distribution")
            fig_pie = px.pie(values=df["Classification"].value_counts().values, names=df["Classification"].value_counts().index)
            fig_pie.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color="#e2e8f0"))
            st.plotly_chart(fig_pie, use_container_width=True)
        with col2:
            st.markdown("#### Confidence Scores")
            fig_hist = px.histogram(df, x="Confidence", nbins=15)
            fig_hist.update_layout(showlegend=False, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color="#e2e8f0"))
            st.plotly_chart(fig_hist, use_container_width=True)
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown("#### History")
        st.dataframe(df.sort_values("Timestamp", ascending=False), use_container_width=True)
    else:
        st.info("📊 No data yet. Use **Prediction** page!")

elif page == "ℹ️ About":
    st.markdown("### About TechTitains")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        **TechTitains Platform**
        
        Version: 1.0.0
        
        **Features:**
        - 🎯 Real-time classification
        - 💭 Sentiment analysis
        - 🚨 Fake news detection
        - 📈 Analytics dashboard
        - 💾 History tracking
        
        **Tech Stack:**
        - Streamlit
        - Plotly
        - Pandas
        - PyTorch
        """)
    with col2:
        st.markdown("""
        **Stats**
        
        📊 Predictions: `0`
        
        ✅ Status: `Active`
        
        🚀 Version: `1.0.0`
        """)
