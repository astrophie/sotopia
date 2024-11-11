import streamlit as st
from sotopia.ui.socialstream.chat import chat_demo_simple
from sotopia.ui.socialstream.utils import initialize_session_state, reset_database

st.title("Simple Chat")

# Display Simple Chat Functionality
st.write("This is the basic chat interface.")
chat_demo_simple()
