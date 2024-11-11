# pages/omniscient_chat.py
import streamlit as st
from sotopia.ui.socialstream.chat import chat_demo_omniscient
from sotopia.ui.socialstream.utils import initialize_session_state, reset_database

st.title("Omniscient Chat & Editable Scenario")

# Display Omniscient Chat Functionality
st.write("This is the omniscient chat interface with editing capabilities.")
chat_demo_omniscient()
