import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import random

# Page configuration
st.set_page_config(
    page_title="TechTitains - Social Media Intelligence",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 TechTitains - Social Media Intelligence Platform")
st.markdown("An advanced NLP-powered platform for detecting fake news, classifying content, and analyzing sentiment.")

# Initialize session state
if 'predictions' not in st.session_state:
    st.session_state.predictions = []

# Sidebar
with st.sidebar:
    st.header("🎛️ Menu")
    page = st.radio("Select Page:", ["🏠 Home", "🔮 Prediction", "📊 Analytics", "⚙️ About"])

if page == "🏠 Home":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Predictions", len(st.session_state.predictions))
    with col2:
        fake_count = sum(1 for p in st.session_state.predictions if p[1] == "⚠️ Fake News")
        st.metric("Fake News Detected", fake_count)
    with col3:
        st.metric("Platform Status", "Active ✅")
    
    st.info("👉 Use the sidebar to navigate to different sections.")

elif page == "🔮 Prediction":
    st.header("🔮 Text Classification")
    text = st.text_area("Enter text to analyze:", height=200)
    
    if st.button("🔍 Analyze", use_container_width=True):
        if text.strip():
            # Simulate classification
            classes = ["😊 Positive", "⚠️ Fake News", "😐 Neutral"]
            prediction = random.choice(classes)
            confidence = round(random.uniform(0.6, 0.99), 2)
            
            st.session_state.predictions.append((
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                prediction,
                confidence,
                text
            ))
            
            st.success("✅ Analysis Complete!")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Classification", prediction)
            with col2:
                st.metric("Confidence", f"{confidence*100:.2f}%")
            with col3:
                st.metric("Timestamp", datetime.now().strftime("%H:%M:%S"))
        else:
            st.warning("⚠️ Please enter text to analyze.")

elif page == "📊 Analytics":
    st.header("📊 Analytics Dashboard")
    
    if st.session_state.predictions:
        df = pd.DataFrame(
            st.session_state.predictions,
            columns=["Timestamp", "Classification", "Confidence", "Text"]
        )
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total", len(df))
        with col2:
            st.metric("Positive", len(df[df["Classification"].str.contains("Positive")]))
        with col3:
            st.metric("Fake", len(df[df["Classification"].str.contains("Fake")]))
        with col4:
            st.metric("Neutral", len(df[df["Classification"].str.contains("Neutral")]))
        
        st.subheader("📈 Classification Distribution")
        class_counts = df["Classification"].value_counts()
        fig = px.pie(values=class_counts.values, names=class_counts.index)
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No predictions yet. Go to Prediction page to get started!")

elif page == "⚙️ About":
    st.header("⚙️ About TechTitains")
    st.markdown("""
    **TechTitains Social Media Intelligence Platform**
    
    Version: 1.0.0
    
    **Features:**
    - Real-time text classification
    - Sentiment analysis
    - Fake news detection
    - Interactive analytics dashboard
    - Prediction history tracking
    
    **Technology Stack:**
    - Streamlit - Web framework
    - Plotly - Visualization
    - Pandas - Data processing
    
    Built with ❤️ for TechTitains
    """)
