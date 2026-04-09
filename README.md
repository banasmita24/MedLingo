# 🩺 MedLingo — Medical Discharge Instruction Assistant

MedLingo is an AI-powered medical translation tool that simplifies complex discharge instructions and translates them into 80+ languages.

## ✨ Features

- **ML Safety Analysis**: Validates medical instructions using a Restricted Boltzmann Machine
- **LLM Simplification**: Rewrites complex clinical language into plain English
- **80+ Languages**: Supports Indian, European, Asian, Middle Eastern, and African languages

## 🚀 Live Demo

[Try MedLingo on Streamlit Cloud](https://medlingo-ai-assistant.streamlit.app/)

## 📦 Local Installation

```bash
# Clone the repository
git clone https://github.com/banasmita24/MedLingo.git
cd medlingo

# Install dependencies
pip install -r requirements.txt

# Set up your Groq API key (for local testing)
mkdir -p .streamlit
echo 'GROQ_API_KEY = "your-api-key-here"' > .streamlit/secrets.toml

# Run the app
streamlit run app.py
