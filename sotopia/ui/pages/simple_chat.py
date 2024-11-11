import streamlit as st
from sotopia.ui.socialstream.chat import chat_demo_simple
from sotopia.ui.socialstream.utils import initialize_session_state, reset_database

st.title("Simple Chat")

st.write("Here are some instructions about using the chat.")
chat_demo_simple()
