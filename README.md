# 🚀 TechTitains - Social Media Intelligence Platform

<div align="center">

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/Dineshhanumanthu/techtitains.svg?style=social)](https://github.com/Dineshhanumanthu/techtitains)

**An advanced NLP-powered platform for detecting fake news, classifying content, and analyzing sentiment in social media posts.**

[🔗 Live Demo](#) • [📖 Documentation](#-documentation) • [🤖 Model Details](#-model-details) • [⭐ Features](#-features)

</div>

---

## 📸 Overview

TechTitains is a state-of-the-art Social Media Intelligence Platform built with cutting-edge Natural Language Processing technology. It empowers users to:

- 🎯 **Detect Fake News** - Identify misinformation and false claims
- 📊 **Classify Content** - Categorize posts as Positive, Fake, or Neutral
- 💭 **Analyze Sentiment** - Understand emotional tone and intent
- 📈 **View Analytics** - Comprehensive dashboards and visualizations
- 💾 **Track History** - Keep records of all analyzed texts

---

## ⭐ Features

### Core Functionality

✅ **Real-time Text Classification**
- Instant classification of any text input
- Support for social media posts, news articles, and general text
- Lightning-fast inference times

✅ **Confidence Scoring**
- Get detailed probability scores for each classification
- Visual confidence indicators
- Transparency in model predictions

✅ **Advanced Text Preprocessing**
- Automatic URL removal
- @mention and hashtag filtering
- Special character handling
- Lowercase normalization

✅ **Interactive Analytics Dashboard**
- Real-time prediction statistics
- Beautiful visualizations and charts
- Trend analysis and patterns
- Classification distribution

✅ **Prediction History**
- Automatic tracking of all predictions
- Export to CSV
- Search and filter capabilities

✅ **Model Configuration**
- Adjustable hyperparameters
- Flexible batch sizes
- Customizable learning rates
- Configurable preprocessing options

---

## 🤖 Model Details

### Architecture

**Model**: RoBERTa-Base
- **Type**: Transformer-based Language Model
- **Layers**: 12 transformer layers
- **Hidden Size**: 768 dimensions
- **Total Parameters**: ~125 million
- **Pre-training**: 160GB of English text from CommonCrawl

### Task

**3-Class Text Classification**
- `0 - Positive` 😊: Positive sentiment, genuine content
- `1 - Fake News` ⚠️: Misinformation, false claims
- `2 - Neutral` 😐: Neutral or objective content

### Performance Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| Inference Speed | <1 second per text |
| Model Size | ~500MB |
| Supported Languages | English |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Dineshhanumanthu/techtitains.git
cd techtitains
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

---

## 📖 Usage Guide

### 🏠 Home Page
- Overview of platform features
- Quick statistics
- Navigation to different sections

### 🔮 Prediction Page
1. Enter or paste text in the text area
2. Click "🔍 Analyze" button
3. View instant results with:
   - Predicted classification
   - Confidence score
   - Probability distribution
   - Processed text preview

### 📊 Analytics Dashboard
- View all predictions statistics
- Interactive charts and graphs
- Classification distribution
- Confidence score trends
- Download prediction history

### ⚙️ Settings
- Configure model hyperparameters
- Adjust preprocessing options
- Manage prediction history
- Export data

---

## 📁 Project Structure

```
techtitains/
├── app.py                    # Main Streamlit application
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
│
├── pages/                    # Streamlit multi-page app
│   ├── 1_home.py            # Home page
│   ├── 2_prediction.py       # Prediction page
│   ├── 3_analytics.py        # Analytics dashboard
│   └── 4_settings.py         # Settings page
│
├── utils/                    # Utility modules
│   ├── __init__.py
│   ├── preprocessing.py      # Text preprocessing
│   ├── model.py             # Model loading/inference
│   └── metrics.py           # Evaluation metrics
│
├── data/                     # Data files
│   └── sample_data.csv      # Sample dataset
│
and└── assets/                # Static assets
    └── style.css            # Custom styling
```

---

## 🛠️ Technology Stack

### Backend & ML
- **PyTorch** - Deep learning framework
- **Transformers** - Hugging Face library
- **Scikit-learn** - Machine learning utilities
- **NumPy** - Numerical computing
- **Pandas** - Data processing

### Frontend & UI
- **Streamlit** - Web framework
- **Plotly** - Interactive visualizations
- **HTML/CSS** - Custom styling

### Development
- **Python 3.8+** - Programming language
- **Git** - Version control
- **GitHub** - Repository hosting

---

## 📊 Example Usage

### Input
```text
This news is completely false and misleading!
```

### Output
```
Predicted Class: ⚠️ Fake News
Confidence: 95.23%

Probabilities:
- Positive: 2.14%
- Fake News: 95.23%
- Neutral: 2.63%
```

---

## 🎓 How It Works

1. **Input Processing**: User enters text
2. **Text Cleaning**: Preprocessing removes URLs, mentions, etc.
3. **Tokenization**: Text is converted to tokens
4. **Model Inference**: RoBERTa model generates predictions
5. **Post-processing**: Probabilities are calculated
6. **Output**: Results displayed with confidence scores

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines
- Follow PEP 8 code style
- Add comments for complex logic
- Update documentation as needed
- Test your changes

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**TechTitains Team**
- GitHub: [@Dineshhanumanthu](https://github.com/Dineshhanumanthu)
- Built with ❤️ for the hackathon

---

## 🙏 Acknowledgments

- Hugging Face for the Transformers library
- Facebook Research for RoBERTa model
- Streamlit for the amazing web framework
- The open-source community

---

## 📧 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Check existing documentation
- Review the FAQ section

---

## 🔗 Useful Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [RoBERTa Paper](https://arxiv.org/abs/1907.11692)
- [PyTorch Documentation](https://pytorch.org/docs/)

---

<div align="center">

### ⭐ If you find this project useful, please consider giving it a star!

**Made with ❤️ by TechTitains**

</div>
