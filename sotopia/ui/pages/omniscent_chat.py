# pages/omniscient_chat.py
import streamlit as st
from sotopia.ui.socialstream.chat import chat_demo_omniscient
from sotopia.ui.socialstream.utils import initialize_session_state, reset_database

st.title("Omniscient Chat & Editable Scenario")

# Optional Database URL Popup
if st.button("Enter Database URL"):
    with st.modal("Database URL Configuration"):
        st.text_input("Enter Database URL (starting with redis://)", key="new_database_url")
        if st.button("Update Database URL"):
            update_database_callback()

# Display Omniscient Chat Functionality
st.write("This is the omniscient chat interface with editing capabilities.")
chat_demo_omniscient()
