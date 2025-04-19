---
title: "Email Classification and PII Masking"
emoji: "📧"
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "1.0"
app_file: app.py
pinned: false
---

# Email Classification API

📧 Classifies support emails and masks any personally identifiable information (PII) using regex.  
🚀 Deployed using FastAPI & Docker on Hugging Face Spaces.

---

## 🔧 Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
