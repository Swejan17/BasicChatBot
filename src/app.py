import os

import streamlit as st

from langchain_core.messages import HumanMessage,AIMessage

from dotenv import load_dotenv
load_dotenv()
from utils.backend import get_reponse



if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.set_page_config(page_title="Finacial Wellbeing Chatbot", page_icon="🧊", layout="centered")

st.title("Mind Your Finace Chatbot")



# chat history

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("human"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("ai"):
            st.markdown(message.content)

# user input
user_query = st.chat_input("Your message")

if user_query!="" and user_query is not None:
    
    with st.chat_message("human"):
        st.markdown(user_query)
        
    with st.chat_message('ai'):
        ai_responce = get_reponse(user_query,st.session_state.chat_history)
        ai_responce=st.write_stream(ai_responce)
        
        st.session_state.chat_history.append(HumanMessage(user_query))
        st.session_state.chat_history.append(AIMessage(ai_responce))

