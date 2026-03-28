# 🤖 Conversational AI Chatbot

A fully conversational AI chatbot built with **LangChain**, **Groq API**, and **Streamlit** — featuring persistent memory, custom personas, and a clean web interface.

---

## ✨ Features

- 💬 **Conversational Memory** — AI remembers full chat history across multiple turns
- 🎭 **Custom Persona** — System prompt gives AI a focused personality and behavior
- 🌐 **Web Interface** — Clean, WhatsApp-style chat UI built with Streamlit
- ⚡ **Fast Responses** — Powered by Groq's ultra-fast Llama 3.3 70B model
- 🔒 **Secure API Handling** — API keys protected using `.env` and `python-dotenv`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| LangChain | LLM framework for conversation management |
| Groq API | Fast LLM inference (Llama 3.3 70B) |
| Streamlit | Web interface |
| python-dotenv | Secure API key management |

---

## 📁 Project Structure

```
ai-chatbot/
├── app.py          
├── .env            
├── .gitignore     
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/knabeels/ai-chatbot.git
cd ai-chatbot
```

### 2. Install dependencies
```bash
pip install streamlit langchain langchain-groq langchain-core python-dotenv
```

### 3. Set up your API key
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your-groq-api-key-here
```
Get your free API key at: [console.groq.com](https://console.groq.com)

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 💻 Code Overview

```python
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, BaseMessage

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# System prompt gives AI its personality
system_prompt = SystemMessage(content="You are best and friendly AI Assistant for teaching AI Engineering")

# Conversation memory — stores full chat history
conversation_history: list[BaseMessage] = [system_prompt]

# Send message and get response
response = llm.invoke(conversation_history)
```

---

## 🧠 How Memory Works

```
User: "My name is Nabeel"     → added to history
AI:   "Nice to meet you!"     → added to history
User: "What is my name?"      → full history sent to AI
AI:   "Your name is Nabeel!"  → remembers! ✅
```

Every message is stored in `conversation_history` and sent to the LLM on each call — giving the AI full context of the conversation.

---

## 🖥️ Screenshots

> Add a screenshot of your running app here
> `![Chatbot Screenshot](screenshot.png)`

---

## 📦 Dependencies

```
streamlit
langchain
langchain-groq
langchain-core
python-dotenv
```

Install all at once:
```bash
pip install streamlit langchain langchain-groq langchain-core python-dotenv
```

---

## 🔮 Future Improvements

- [ ] Add RAG — AI reads uploaded PDF documents
- [ ] Add conversation export feature
- [ ] Deploy to Streamlit Cloud (public URL)
- [ ] Add multiple AI personas to choose from

---

## 👨‍💻 Author

**Khan Nabeel Shahid**
- LinkedIn: [https://www.linkedin.com/in/k-nabeel-s/]
- GitHub: [https://github.com/knabeels]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
