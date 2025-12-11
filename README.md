# Custom OpenAI Chatbot by Shivam

A powerful, user-friendly chatbot application powered by OpenAI's GPT-4 and built with Streamlit. Get instant, intelligent responses to your queries with a modern web interface.

## ✨ Features

- **GPT-4 Powered**: Leverages OpenAI's advanced language model for accurate and contextual responses
- **Real-time Interaction**: Instant responses to user queries through an intuitive web interface
- **Streamlit Framework**: Beautiful, responsive UI built with minimal code
- **LangChain Integration**: Robust prompt management and LLM orchestration
- **LangSmith Monitoring**: Track and analyze model performance and API usage
- **Customizable Temperature**: Fine-tune response creativity and consistency

## 🎯 Use Cases

- Customer support automation
- Quick research and information retrieval
- Content generation assistance
- Educational tutoring and explanation
- Brainstorming and idea generation
- Technical problem-solving

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- LangChain API key (optional, for monitoring)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llm-openai-chatbot.git
   cd llm-openai-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   LANGCHAIN_API_KEY=your_langchain_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your default browser at `http://localhost:8501`

## 📋 Configuration

### Model Parameters

You can customize the LLM behavior in `config.py`:

- **Model**: `gpt-4` (or `gpt-3.5-turbo` for faster responses)
- **Temperature**: Range 0.0-1.0 (lower = more focused, higher = more creative)
- **Max Tokens**: Limit response length

### System Prompt

Modify the system prompt in `utils/llm_chain.py` to change chatbot behavior:

```python
"I am a helpful chatbot designed to assist you with any questions."
```

## 🏗️ Project Structure

```
llm-openai-chatbot/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration settings
├── utils/
│   └── llm_chain.py       # LLM chain initialization
├── requirements.txt       # Project dependencies
├── .env.example          # Template for environment variables
└── .gitignore            # Git ignore rules
```

## 🔌 API Requirements

### OpenAI API
- Free tier available with $5 credit
- Pay-as-you-go pricing after free tier
- See [pricing details](https://openai.com/pricing)

### LangChain (Optional)
- Free tier for development
- Enhanced monitoring and debugging
- [Sign up here](https://smith.langchain.com/)

## 🛡️ Security

- **Never commit API keys** to version control
- Always use `.env` files for sensitive data
- API keys are kept in environment variables
- Use `.gitignore` to prevent accidental commits

## 🤝 How to Use

1. Start the application
2. Type your question or query in the input field
3. Press Enter or click outside the input box
4. Receive instant response from GPT-4

Example queries:
- "Explain quantum computing in simple terms"
- "Write a Python function to reverse a string"
- "What are the benefits of renewable energy?"

## 📊 Performance & Monitoring

With LangSmith enabled, monitor:
- API response times
- Token usage
- Cost analysis
- Error tracking

Access your LangSmith dashboard to view detailed metrics.

## ⚙️ Troubleshooting

**Q: "API key not found" error**
- Ensure `.env` file exists in root directory
- Verify keys are correctly set

**Q: Slow responses**
- Check internet connection
- Consider using `gpt-3.5-turbo` for faster responses
- Check OpenAI API status page

**Q: Port already in use**
- Run: `streamlit run app.py --server.port 8502`

## 🚀 Future Enhancements

- [ ] Memory/chat history functionality
- [ ] Multiple model support
- [ ] Custom knowledge base integration
- [ ] Rate limiting and usage analytics
- [ ] Docker containerization
- [ ] Deployment to cloud platforms

## 📚 Documentation

For detailed setup instructions, see [SETUP.md](docs/SETUP.md)

## 🤓 Technologies Used

- **Streamlit**: Web framework
- **LangChain**: LLM orchestration
- **OpenAI GPT-4**: Language model
- **Python**: Programming language

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 💬 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📞 Support

For issues and questions:
- Open a GitHub issue
- Check existing documentation
- Review LangChain and Streamlit docs

## ⭐ Show Your Support

If this project helps you, please give it a star! It motivates further development.

---

**Made with ❤️ by Shivam**
