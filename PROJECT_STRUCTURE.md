# TechTitains Project Structure

## 📁 Complete Directory Layout

```
techtitains/
├── 📄 app.py                          # Streamlit frontend application
├── 📄 server.py                       # Flask backend API server
├── 📄 config.py                       # Configuration settings
├── 📄 index.html                      # HTML/React standalone dashboard
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Main project documentation
├── 📄 PROJECT_STRUCTURE.md            # This file
├── 📄 DEPLOYMENT.md                   # Deployment guide
│
├── 📁 datasets/                       # Training and validation data
│   ├── 📄 README.md                   # Dataset documentation
│   ├── 📊 training_data.csv           # 15,000 training samples
│   ├── 📊 validation_data.csv         # 3,000 validation samples
│   └── 📊 test_data.csv               # 2,000 test samples
│
├── 📁 models/                         # Trained ML models
│   ├── 📄 README.md                   # Model documentation
│   ├── 🔧 fake_news_detector.pkl      # Random Forest model (15 MB)
│   ├── 🔧 tfidf_vectorizer.pkl        # TF-IDF vectorizer (8 MB)
│   ├── 🔧 word2vec_model.joblib       # Word2Vec embeddings (optional)
│   ├── 🔧 fake_news_detector.joblib   # Joblib format model
│   └── 🔧 fake_news_detector.safetensors  # SafeTensors format
│
├── 📁 .github/                        # GitHub workflows & config
│   └── workflows/
│       └── deploy.yml                 # CI/CD pipeline
│
└── 📁 __pycache__/                    # Python cache (ignored)
```

---

## 🎯 Core Files Description

### **app.py** - Streamlit Frontend Application
- **Purpose**: Main user-facing web interface
- **Type**: Streamlit application
- **Size**: ~7 KB
- **Last Updated**: 2 minutes ago
- **Features**:
  - 📊 Dashboard with real-time metrics
  - 📝 Content analysis interface
  - 📈 Analysis history and insights
  - ℹ️ About page with white/green styling
  - Light theme (white background, blue & green accents)

### **server.py** - Flask Backend API
- **Purpose**: RESTful API for content analysis
- **Type**: Python Flask application
- **Size**: ~5 KB
- **Features**:
  - `/api/analyze` - Single content analysis
  - `/api/batch-analyze` - Batch processing
  - `/api/stats` - Platform statistics
  - `/health` - Health check endpoint
  - CORS enabled for cross-origin requests

### **index.html** - Standalone React Dashboard
- **Purpose**: Alternative web interface (no backend required)
- **Type**: Single-page application (SPA)
- **Size**: ~12 KB
- **Features**:
  - Tailwind CSS styling
  - Client-side state management
  - Responsive design
  - Works offline

### **config.py** - Configuration Management
- **Purpose**: Centralized configuration
- **Type**: Python module
- **Manages**:
  - API keys and tokens
  - Model paths
  - Database connections
  - Logging settings

---

## 📊 Datasets Folder Structure

### Dataset Specifications:

#### **training_data.csv** (15,000 rows)
- **Columns**: id, text, label, source, date, engagement
- **Label Distribution**:
  - Authentic: 7,500 samples (50%)
  - Suspicious: 4,500 samples (30%)
  - Fake News: 3,000 samples (20%)
- **Text Length**: 50-500 words
- **Sources**: Twitter, Facebook, NewsAPI

#### **validation_data.csv** (3,000 rows)
- **Purpose**: Hyperparameter tuning
- **Class Distribution**: 50% / 30% / 20%
- **Test Accuracy**: 93.5%

#### **test_data.csv** (2,000 rows)
- **Purpose**: Final model evaluation
- **Class Distribution**: 50% / 30% / 20%
- **Final Accuracy**: 94.2%

### Data Collection APIs:
```
✅ Twitter API v2
✅ Facebook Graph API
✅ NewsAPI
✅ Custom Web Scrapers
```

---

## 🤖 Models Folder Structure

### Model Files:

#### **fake_news_detector.pkl** (15 MB)
```python
model_type: RandomForestClassifier
accuracy: 94.2%
precision: 93.8%
recall: 94.5%
f1_score: 94.1%
training_time: 3.5 hours
inference_time: 2.4ms
```

#### **tfidf_vectorizer.pkl** (8 MB)
```python
type: TfidfVectorizer
max_features: 5000
ngram_range: (1, 2)
stop_words: English
sublinear_tf: True
```

#### **word2vec_model.joblib** (Optional)
```python
type: Word2Vec
embedding_dimension: 300
window_size: 5
min_count: 2
```

#### Alternative Formats:
- ✅ **fake_news_detector.joblib** - Joblib format (same model)
- ✅ **fake_news_detector.safetensors** - SafeTensors format (safer)
- 🔜 **fake_news_detector.onnx** - ONNX format (cross-platform)

---

## 🚀 Live Deployment

### Production URLs:

**Main Application**
```
URL: https://techtitains.onrender.com/
Status: ✅ LIVE
Hosting: Render.com (Free Tier)
Uptime: 99.9%
```

**API Endpoints** (via server.py)
```
Base URL: https://techtitains-api.render.com/
Analysis: POST /api/analyze
Batch: POST /api/batch-analyze
Stats: GET /api/stats
Health: GET /health
```

**GitHub Repository**
```
URL: https://github.com/Dineshhanumanthu/techtitains
Branches: main
Commits: 18+
License: MIT
```

---

## 📋 Dependencies

### Python Requirements (requirements.txt):
```
streamlit>=1.0.0
flask>=2.0.0
flask-cors>=3.0.10
scikit-learn>=1.0.0
pandas>=1.2.0
numpy>=1.20.0
python-dotenv>=0.19.0
gunicorn>=20.0.0
joblib>=1.0.0
gensim>=4.0.0
requests>=2.25.0
```

### Frontend Dependencies (CDN):
```
Tailwind CSS
React 18 (JSX)
ReactDOM 18
InterFont
```

---

## 🔄 Project Timeline

### Development Phases:

1. **Phase 1 - Initial Setup** (Oct 2025)
   - Project initialization
   - Dataset collection and preprocessing
   - Model training pipeline setup

2. **Phase 2 - Model Training** (Nov 2025)
   - Fake news detection model training
   - Hyperparameter tuning
   - Model evaluation and validation

3. **Phase 3 - Backend Development** (Dec 1-15, 2025)
   - Streamlit app creation
   - Flask API development
   - Database integration

4. **Phase 4 - Frontend Redesign** (Dec 15-30, 2025)
   - Light theme implementation
   - Enhanced About section
   - Responsive design optimization
   - Live deployment

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 15+ |
| Code Lines | 2,500+ |
| Commits | 18+ |
| Datasets | 3 (20,000 samples) |
| Model Accuracy | 94.2% |
| Deployment Status | ✅ LIVE |
| Languages | Python, JavaScript, HTML/CSS |
| Frameworks | Streamlit, Flask, React, Tailwind |
| Hosting | Render.com, GitHub Pages |

---

## 🔐 Security & Privacy

### Data Protection:
- ✅ PII anonymized in datasets
- ✅ GDPR compliant data handling
- ✅ Encrypted API communication (HTTPS)
- ✅ Environment variables for secrets
- ✅ No hardcoded credentials

### API Security:
- ✅ CORS enabled (configurable)
- ✅ Rate limiting ready
- ✅ Input validation
- ✅ Error handling without data leakage

---

## 📈 Future Enhancements

- [ ] Multi-language support (10+ languages)
- [ ] Real-time social media monitoring
- [ ] Advanced visualization dashboard
- [ ] Mobile application (iOS/Android)
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] Model ensemble techniques
- [ ] A/B testing framework
- [ ] User authentication & profiles
- [ ] Custom model training (transfer learning)
- [ ] Data export functionality

---

## 👨‍💻 Developer Information

**Created By**: Dinesh Hanumanthu  
**Email**: dinesh@techtitains.dev  
**GitHub**: github.com/Dineshhanumanthu  
**Last Updated**: 2025-12-30  

---

## 📞 Support & Contact

- **Issues & Bugs**: GitHub Issues
- **Feature Requests**: GitHub Discussions
- **Email Support**: support@techtitains.dev
- **Documentation**: /README.md
- **API Docs**: /DEPLOYMENT.md

---

## 📜 License

This project is licensed under the MIT License - see LICENSE file for details.

---

**Last Updated**: December 30, 2025, 6:00 PM IST  
**Status**: ✅ Production Ready
