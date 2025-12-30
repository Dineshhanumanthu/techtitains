import streamlit as st
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import re
import os

# Page configuration
st.set_page_config(
    page_title="TechTitains - Social Media Intelligence",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'predictions' not in st.session_state:
    st.session_state.predictions = []
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False

# Model loading with caching
@st.cache_resource
def load_model():
    model_name = "roberta-base"
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=3
        )
        return tokenizer, model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

def preprocess_text(text):
    """Clean and preprocess text"""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # Remove special characters but keep basic punctuation
    text = re.sub(r'[^a-zA-Z0-9\s\.!?\-]', '', text)
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.lower()

def predict_sentiment(text, tokenizer, model):
    """Predict sentiment and classification"""
    if not tokenizer or not model:
        return None, None, None
    
    # Preprocess
    processed_text = preprocess_text(text)
    
    # Tokenize
    inputs = tokenizer(
        processed_text,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=512
    )
    
    # Get predictions
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=1)[0]
        prediction = torch.argmax(logits, dim=1)[0].item()
    
    # Class mapping
    classes = {0: "😊 Positive", 1: "⚠️ Fake News", 2: "😐 Neutral"}
    
    return classes[prediction], probabilities.cpu().numpy(), processed_text

# Main app
def main():
    # Sidebar
    with st.sidebar:
        st.header("🎛️ Configuration")
        page = st.radio(
            "Select Page:",
            ["🏠 Home", "🔮 Prediction", "📊 Analytics", "⚙️ Settings"]
        )
    
    # Load model
    if not st.session_state.model_loaded:
        with st.spinner("Loading model..."):
            tokenizer, model = load_model()
            st.session_state.tokenizer = tokenizer
            st.session_state.model = model
            st.session_state.model_loaded = True
    else:
        tokenizer = st.session_state.tokenizer
        model = st.session_state.model
    
    # Home Page
    if page == "🏠 Home":
        st.title("🚀 TechTitains - Social Media Intelligence Platform")
        st.markdown("""
        ### Welcome to TechTitains!
        
        A state-of-the-art platform powered by RoBERTa for:
        - 🎯 **Fake News Detection**
        - 📊 **Content Classification**
        - 💭 **Sentiment Analysis**
        - 📈 **Real-time Analytics**
        
        ---
        """)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Predictions", len(st.session_state.predictions))
        with col2:
            if st.session_state.predictions:
                fake_count = sum(1 for p in st.session_state.predictions if "Fake" in p[1])
                st.metric("Fake News Detected", fake_count)
            else:
                st.metric("Fake News Detected", 0)
        with col3:
            st.metric("Platform Status", "Active ✅")
        
        st.info("👉 Use the sidebar to navigate to different sections of the platform.")
    
    # Prediction Page
    elif page == "🔮 Prediction":
        st.title("🔮 Text Classification & Analysis")
        
        text_input = st.text_area(
            "Enter text to analyze:",
            height=200,
            placeholder="Paste your social media post, news article, or any text here..."
        )
        
        if st.button("🔍 Analyze", use_container_width=True):
            if text_input.strip():
                prediction, probabilities, processed = predict_sentiment(
                    text_input,
                    tokenizer,
                    model
                )
                
                # Store in session
                st.session_state.predictions.append((
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    prediction,
                    max(probabilities),
                    text_input
                ))
                
                # Display results
                st.success("✅ Analysis Complete!")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Classification", prediction)
                with col2:
                    confidence = max(probabilities) * 100
                    st.metric("Confidence", f"{confidence:.2f}%")
                with col3:
                    st.metric("Timestamp", datetime.now().strftime("%H:%M:%S"))
                
                # Probabilities
                st.subheader("📊 Probability Distribution")
                prob_df = pd.DataFrame({
                    "Class": ["Positive", "Fake News", "Neutral"],
                    "Probability": probabilities * 100
                })
                
                fig = px.bar(
                    prob_df,
                    x="Class",
                    y="Probability",
                    title="Classification Probabilities",
                    color="Probability",
                    color_continuous_scale="Viridis"
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Processed text
                with st.expander("📝 Processed Text Preview"):
                    st.code(processed)
            else:
                st.warning("⚠️ Please enter some text to analyze.")
    
    # Analytics Page
    elif page == "📊 Analytics":
        st.title("📊 Analytics Dashboard")
        
        if st.session_state.predictions:
            # Convert to DataFrame
            df = pd.DataFrame(
                st.session_state.predictions,
                columns=["Timestamp", "Classification", "Confidence", "Text"]
            )
            
            # Metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Total Predictions", len(df))
            with col2:
                st.metric("Positive", ("Positive" in df["Classification"]).sum())
            with col3:
                st.metric("Fake News", ("Fake" in df["Classification"]).sum())
            with col4:
                st.metric("Neutral", ("Neutral" in df["Classification"]).sum())
            
            # Charts
            st.subheader("📈 Classification Distribution")
            class_counts = df["Classification"].value_counts()
            fig1 = px.pie(
                values=class_counts.values,
                names=class_counts.index,
                title="Classification Distribution"
            )
            st.plotly_chart(fig1, use_container_width=True)
            
            # Confidence trends
            st.subheader("📉 Confidence Scores Over Time")
            fig2 = px.line(
                df,
                x="Timestamp",
                y="Confidence",
                title="Confidence Trend",
                markers=True
            )
            st.plotly_chart(fig2, use_container_width=True)
            
            # History table
            st.subheader("📋 Prediction History")
            st.dataframe(
                df[["Timestamp", "Classification", "Confidence"]].rename(
                    columns={"Confidence": "Confidence Score"}
                ),
                use_container_width=True
            )
            
            # Export
            csv = df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="predictions.csv",
                mime="text/csv"
            )
        else:
            st.info("📊 No predictions yet. Go to the Prediction page to get started!")
    
    # Settings Page
    elif page == "⚙️ Settings":
        st.title("⚙️ Settings & Configuration")
        
        st.subheader("🔧 Model Configuration")
        col1, col2 = st.columns(2)
        with col1:
            st.info("**Model**: RoBERTa-Base")
        with col2:
            st.info("**Classes**: 3 (Positive, Fake News, Neutral)")
        
        st.subheader("📁 Data Management")
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.predictions = []
            st.success("✅ History cleared!")
        
        st.subheader("ℹ️ About")
        st.markdown("""
        **TechTitains Social Media Intelligence Platform**
        
        Version: 1.0.0
        - Built with Streamlit
        - Powered by Hugging Face Transformers
        - ML Model: RoBERTa
        
        **Features:**
        - Real-time text classification
        - Sentiment analysis
        - Fake news detection
        - Interactive analytics
        - Prediction history
        """)

if __name__ == "__main__":
    main()
