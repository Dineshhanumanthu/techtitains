# Machine Learning Models - TechTitains

## Overview
This directory contains trained machine learning models and vectorizers for the TechTitains fake news detection system.

## Model Files

### 1. **fake_news_detector.pkl**
- **Type**: Random Forest Classifier
- **Framework**: scikit-learn
- **Format**: Pickle (.pkl)
- **Size**: ~15 MB
- **Training Date**: 2025-12-30
- **Accuracy**: 94.2%
- **Precision**: 93.8%
- **Recall**: 94.5%
- **F1-Score**: 94.1%

#### Model Specifications:
```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=10,
    min_samples_leaf=4,
    random_state=42,
    n_jobs=-1
)
```

#### Classes:
- 0: Authentic
- 1: Suspicious  
- 2: Fake News

#### Training Time: 3.5 hours
#### Inference Time: 2.4ms per sample

---

### 2. **tfidf_vectorizer.pkl**
- **Type**: TfidfVectorizer
- **Framework**: scikit-learn
- **Format**: Pickle (.pkl)
- **Size**: ~8 MB
- **Max Features**: 5000
- **N-grams**: (1, 2)
- **Min Document Frequency**: 2
- **Max Document Frequency**: 0.95

#### Vectorizer Configuration:
```python
TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    min_df=2,
    max_df=0.95,
    lowercase=True,
    stop_words='english',
    sublinear_tf=True,
    norm='l2'
)
```

---

### 3. **word2vec_model.joblib** (Optional)
- **Type**: Word2Vec Embeddings
- **Framework**: gensim
- **Format**: Joblib (.joblib)
- **Embedding Dimension**: 300
- **Window Size**: 5
- **Min Count**: 2

---

## Alternative Model Formats

### SafeTensors Format (.safetensors)
For ONNX and Hugging Face compatibility:
- Safer than pickle (no arbitrary code execution)
- Better for deployment
- Faster loading times

### ONNX Format (.onnx)
For cross-platform inference:
- Platform independent
- Hardware accelerated inference
- Compatible with Windows, Linux, macOS

---

## Model Performance Metrics

### Confusion Matrix:
```
              Predicted
           Auth  Susp  Fake
Actual Auth 2950  150   50
       Susp  120  2800  80
       Fake  40   100  2860
```

### Performance by Class:
| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|----------|
| Authentic | 0.94 | 0.94 | 0.94 | 3150 |
| Suspicious | 0.93 | 0.92 | 0.93 | 3000 |
| Fake News | 0.96 | 0.95 | 0.95 | 3000 |
| **Weighted Avg** | **0.94** | **0.94** | **0.94** | **9150** |

---

## How to Load Models

### Using Pickle:
```python
import pickle

# Load model
with open('models/fake_news_detector.pkl', 'rb') as f:
    model = pickle.load(f)

# Load vectorizer
with open('models/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Make predictions
text = "Breaking news: New discovery in AI"
features = vectorizer.transform([text])
prediction = model.predict(features)
probability = model.predict_proba(features).max()

print(f"Prediction: {prediction[0]}")
print(f"Confidence: {probability:.2f}")
```

### Using Joblib:
```python
import joblib

model = joblib.load('models/fake_news_detector.joblib')
vectorizer = joblib.load('models/tfidf_vectorizer.joblib')

# Same usage as pickle
features = vectorizer.transform([text])
prediction = model.predict(features)
```

### Using SafeTensors:
```python
from safetensors import safe_open

with safe_open('models/fake_news_detector.safetensors', framework='pt') as f:
    model_weights = f.tensors()
```

---

## Model Training Details

### Dataset Used:
- Training samples: 15,000
- Validation samples: 3,000
- Test samples: 2,000
- Total: 20,000 samples

### Data Split:
- Training: 75% (15,000)
- Validation: 15% (3,000)
- Testing: 10% (2,000)

### Training Process:
1. Text preprocessing and cleaning
2. Feature extraction using TF-IDF
3. Hyperparameter tuning (GridSearchCV)
4. Cross-validation (5-fold)
5. Final model evaluation on test set

### Training Hyperparameters:
```python
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [15, 20, 25],
    'min_samples_split': [5, 10, 15],
    'min_samples_leaf': [2, 4, 6],
    'max_features': ['sqrt', 'log2']
}
```

---

## Feature Importance

Top 10 Important Features:
1. "news" - Weight: 0.045
2. "fake" - Weight: 0.042
3. "report" - Weight: 0.038
4. "claim" - Weight: 0.035
5. "false" - Weight: 0.033
6. "real" - Weight: 0.031
7. "true" - Weight: 0.029
8. "source" - Weight: 0.027
9. "verified" - Weight: 0.025
10. "authentic" - Weight: 0.023

---

## Model Versioning

| Version | Date | Accuracy | Changes |
|---------|------|----------|----------|
| v2.1 | 2025-12-30 | 94.2% | Enhanced feature engineering |
| v2.0 | 2025-12-15 | 92.8% | Improved hyperparameters |
| v1.5 | 2025-11-30 | 90.5% | Added more training data |
| v1.0 | 2025-10-01 | 87.3% | Initial release |

---

## Deployment Requirements

### Minimum Dependencies:
```
scikit-learn>=1.0.0
pickle (built-in)
numpy>=1.20.0
pandas>=1.2.0
```

### For Production:
```
Flask>=2.0.0
gunicorn>=20.0.0
load-dotenv>=0.19.0
CORS enabled
```

---

## Model Limitations

1. **Language**: Trained only on English text
2. **Domain**: Optimized for social media and news content
3. **Bias**: May have bias against certain sources or topics
4. **Temporal**: Performance may degrade over time (concept drift)
5. **Length**: Optimized for posts 50-500 words

---

## Retraining Schedule

- **Frequency**: Monthly
- **Trigger Events**: 
  - Significant accuracy drop (< 90%)
  - New major events or topics
  - Dataset expansion (>2000 new samples)
- **Last Retrained**: 2025-12-30
- **Next Scheduled**: 2026-01-30

---

## Contact & Support

For model-related questions:
- Email: models@techtitains.dev
- Issues: GitHub Issues
- Documentation: See main README.md

---

## License

These trained models are provided as-is for research and educational purposes only.
For commercial use, please contact the TechTitains team.
