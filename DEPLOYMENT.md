# 🚀 Deployment Guide - TechTitains

## Live Deployment Links

### GitHub Repository
**📌 Main Repository**: https://github.com/Dineshhanumanthu/techtitains

---

## 🌐 Deploy to Streamlit Cloud

### Step 1: Connect GitHub to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Sign in with GitHub
4. Select repository: `Dineshhanumanthu/techtitains`
5. Select branch: `main`
6. Select main file: `app.py`
7. Click "Deploy"

### Step 2: Streamlit Cloud Deployment Features
- ✅ Free hosting
- ✅ Automatic deployments on push
- ✅ Custom domain support
- ✅ Always-on app
- ✅ Automatic SSL/TLS

### Streamlit Cloud Deployment URL
**Expected URL Format**: `https://share.streamlit.io/dineshhanumanthu/techtitains/main/app.py`

---

## 🎯 Deploy to Render

### Step 1: Prepare Deployment Files

Create a `render.yaml` file in the repository root:
```yaml
services:
  - type: web
    name: techtitains
    env: python
    plan: starter
    pythonVersion: 3.8
    startCommand: "streamlit run app.py --server.port=10000 --server.address=0.0.0.0"
    envVars:
      - key: PYTHONUNBUFFERED
        value: true
```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "+ New +" → "Web Service"
4. Select `Dineshhanumanthu/techtitains` repository
5. Configure:
   - **Name**: techtitains
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=10000 --server.address=0.0.0.0`
6. Click "Create Web Service"

### Render Deployment Features
- ✅ Free tier available
- ✅ Automatic deployments
- ✅ Custom domains
- ✅ Environment variables
- ✅ SSL certificates

### Expected Render URL
**Format**: `https://techtitains-xyz.onrender.com`

---

## 🐳 Deploy with Docker

### Create Dockerfile
```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run Locally
```bash
docker build -t techtitains .
docker run -p 8501:8501 techtitains
```

---

## ☁️ Deploy to Heroku

### Step 1: Create Procfile
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
```

### Step 2: Deploy
```bash
heroku login
heroku create techtitains
git push heroku main
```

---

## ⚙️ Environment Variables Setup

For all cloud deployments, ensure these are configured:

```bash
PYTHONUNBUFFEREDundefined=1
PORT=8501
```

---

## 📊 Deployment Comparison

| Platform | Cost | Setup Difficulty | Cold Start | Custom Domain |
|----------|------|------------------|-----------|----------------|
| Streamlit Cloud | Free | Very Easy | < 1s | ✅ Yes |
| Render | Free/Paid | Easy | 30-60s | ✅ Yes |
| Heroku | Free/Paid | Easy | 30-60s | ✅ Yes |
| Docker | Varies | Medium | Instant | ✅ Depends |

---

## 🔧 Troubleshooting

### App won't deploy
- Check `requirements.txt` is in root directory
- Verify `app.py` exists and runs locally
- Check for syntax errors: `python -m py_compile app.py`

### Memory issues
- Reduce model size or use quantization
- Add `--memory=512M` to deployment config
- Implement caching for model inference

### Slow startup
- Model download takes time on first run
- Implement lazy loading
- Use cached model files

---

## 📝 Next Steps

1. Choose your preferred deployment platform
2. Follow the steps above
3. Test the deployed application
4. Share your live URL!

---

## 🤝 Support

For deployment issues:
- Check platform-specific documentation
- Review GitHub Issues
- Contact the maintainers

**Happy Deploying! 🎉**
