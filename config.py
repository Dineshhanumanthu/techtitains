"""Configuration file for TechTitains Social Media Intelligence Platform"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories if they don't exist
for directory in [DATA_DIR, MODEL_DIR, LOGS_DIR]:
    directory.mkdir(exist_ok=True)

# Model configuration
MODEL_CONFIG = {
    "model_name": "roberta-base",
    "num_labels": 3,
    "max_length": 512,
    "device": "cpu"
}

# Classification classes
CLASS_LABELS = {
    0: "😊 Positive",
    1: "⚠️ Fake News",
    2: "😐 Neutral"
}

CLASS_NAMES = {
    "Positive": 0,
    "Fake": 1,
    "Neutral": 2
}

# Text preprocessing configuration
PREPROCESS_CONFIG = {
    "remove_urls": True,
    "remove_mentions": True,
    "remove_hashtags": True,
    "lowercase": True,
    "remove_special_chars": True
}

# Streamlit app configuration
APP_CONFIG = {
    "page_title": "TechTitains - Social Media Intelligence",
    "page_icon": "🚀",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Thresholds
CONFIDENCE_THRESHOLD = 0.5
FAKE_NEWS_ALERT_THRESHOLD = 0.7

# Colors for visualization
COLOR_PALETTE = {
    "positive": "#00CC96",
    "fake_news": "#EF553B",
    "neutral": "#636EFA",
    "background": "#f0f2f6"
}

# Logging configuration
LOGGING_CONFIG = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": LOGS_DIR / "app.log"
}

# Session state defaults
DEFAULT_SESSION_STATE = {
    "predictions": [],
    "model_loaded": False,
    "tokenizer": None,
    "model": None
}
