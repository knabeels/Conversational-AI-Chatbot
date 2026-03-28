import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, BaseMessage
from langchain_groq import ChatGroq

# Loading Env File
load_dotenv()

st.set_page_config(page_title="Conversational AI Chatbot", page_icon="🤖")
st.title("🤖 Conversational AI Chatbot")

# Selecting the specific model
llm = ChatGroq(model="llama-3.3-70b-versatile")

# To make the chatbot specific for AI Engineering Learning
system_prompt = SystemMessage(content="You are best and friendly AI Assistant for teaching AI Engineering")

# Check for every rerun of app, if history is available or not
if "history" not in st.session_state:
    history: list[BaseMessage] = [system_prompt]
    st.session_state.history = history


for message in st.session_state.history:
    if isinstance(message, HumanMessage):
        with st.chat_message('user'):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message('assistant'):
            st.write(message.content)

user_input = st.chat_input("Type your Message...")

if user_input:
    # Here added the user input to the Human Object of langchain
    st.session_state.history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)
    # Loading spinner after user input
    with st.spinner("Thinking"):
        # Here invoking the llm model
        response = llm.invoke(st.session_state.history)
        # Getting the response from ai
        ai_reply = response.content
    # Here added the user input to the AI Object of langchain
    st.session_state.history.append(AIMessage(content=ai_reply))
    with st.chat_message("assistant"):
        # Showing to User using Streamlit
        st.write(ai_reply)