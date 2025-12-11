# Setup Guide: Custom OpenAI Chatbot by Shivam

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

## Step-by-Step Setup

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/llm-openai-chatbot.git
cd llm-openai-chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

**Activate virtual environment:**
- **macOS/Linux**: `source venv/bin/activate`
- **Windows**: `venv\Scripts\activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get API Keys

**OpenAI API Key:**
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in
3. Create new secret key
4. Copy the key (you won't see it again)

**LangChain API Key (Optional):**
1. Go to https://smith.langchain.com/
2. Sign up
3. Create API key
4. Copy the key

### 5. Configure Environment
```bash
cp .env.example .env
```

Edit `.env` file and paste your keys:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxx
LANGCHAIN_API_KEY=ls-xxxxxxxxxxxxxxx
```

### 6. Run Application
```bash
streamlit run app.py
```

The app will automatically open in your browser!

## Troubleshooting

**Module not found error:**
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

**API Key error:**
- Check `.env` file exists
- Verify key format is correct
- Keys shouldn't have quotes around them

**Port already in use:**
- Run on different port: `streamlit run app.py --server.port 8502`
