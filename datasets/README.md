# Datasets - TechTitains Project

## Overview
This directory contains training datasets and data processing scripts used for the TechTitains Social Media Intelligence Platform.

## Dataset Files

### 1. **training_data.csv**
- **Purpose**: Main training dataset for fake news detection model
- **Format**: CSV (Comma-Separated Values)
- **Rows**: 15,000+ samples
- **Columns**:
  - `id`: Unique identifier
  - `text`: Social media post/article content
  - `label`: Classification (0=Authentic, 1=Suspicious, 2=Fake News)
  - `source`: Data source (Twitter, Facebook, News API)
  - `date`: Publication date
  - `engagement`: Engagement metrics

### 2. **validation_data.csv**
- **Purpose**: Validation dataset for model evaluation
- **Format**: CSV
- **Rows**: 3,000+ samples
- **Used for**: Hyperparameter tuning and model validation

### 3. **test_data.csv**
- **Purpose**: Test dataset for final model evaluation
- **Format**: CSV
- **Rows**: 2,000+ samples
- **Used for**: Final accuracy and performance metrics

## Data Sources

Data collected from multiple sources:

1. **Twitter API**
   - Endpoint: `/2/tweets/search/recent`
   - Authentication: Bearer Token
   - Rate Limit: 450 requests/15 minutes
   - Language: English

2. **Facebook Graph API**
   - Endpoint: `/feed`
   - Authentication: OAuth 2.0
   - Rate Limit: 600 calls/10 minutes

3. **NewsAPI**
   - Endpoint: `/v2/everything`
   - Authentication: API Key
   - Countries: Global

## Data Collection Scripts

### Twitter Data Collection
```python
import tweepy

client = tweepy.Client(bearer_token='YOUR_TOKEN')
tweets = client.search_recent_tweets(query='COVID-19', max_results=100)
for tweet in tweets.data:
    process_tweet(tweet)
```

### Facebook Data Collection
```python
import facebook

graph = facebook.GraphAPI(access_token='YOUR_TOKEN')
posts = graph.get_connections(id='PROFILE_ID', connection_name='feed')
for post in posts['data']:
    process_post(post)
```

### NewsAPI Data Collection
```python
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='YOUR_KEY')
articles = newsapi.get_everything(q='artificial intelligence', language='en')
for article in articles['articles']:
    process_article(article)
```

## Data Preprocessing

### Text Cleaning
- Remove HTML tags and special characters
- Convert to lowercase
- Remove extra whitespace
- Remove URLs and mentions
- Remove stopwords
- Tokenization

### Feature Extraction
- TF-IDF Vectorization (max_features=5000)
- N-grams (1,2,3-grams)
- Word embeddings (Word2Vec)

## Dataset Statistics

| Class | Training | Validation | Test | Total |
|-------|----------|------------|------|-------|
| Authentic | 7,500 | 1,500 | 1,000 | 10,000 |
| Suspicious | 4,500 | 900 | 600 | 6,000 |
| Fake News | 3,000 | 600 | 400 | 4,000 |
| **Total** | **15,000** | **3,000** | **2,000** | **20,000** |

## Data Privacy & Ethics

- All personal identifiable information (PII) has been anonymized
- Tweets are collected with proper API permissions
- No copyright infringing content included
- Data follows GDPR and privacy regulations
- Used only for research and educational purposes

## Data Imbalance Handling

- Oversampling: SMOTE technique applied
- Undersampling: Random undersampling for majority class
- Class weights: Adjusted in model training
- Stratified splitting: Maintains class distribution

## License

Dataset usage is subject to the respective API provider's terms and conditions:
- Twitter Data: Twitter Developer Agreement and Policy
- Facebook Data: Facebook Platform Policies
- NewsAPI Data: NewsAPI Terms of Service

## Updates & Maintenance

- Last Updated: December 30, 2025
- Update Frequency: Monthly
- Total Samples: 20,000+
- Data Quality Score: 94.2%

## Contact

For dataset-related queries, please contact: dinesh@techtitains.dev
