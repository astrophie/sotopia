import streamlit as st
from sotopia.ui.socialstream.chat import chat_demo_omniscient
from sotopia.ui.socialstream.utils import initialize_session_state, reset_database

st.title("Omniscient Chat & Editable Scenario")

st.write("Here are some instructions about using the omniscient chat.")
chat_demo_omniscient()