import os

import streamlit as st

from sotopia.ui.socialstream.rendering import rendering_demo

st.title("Episode")
# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebar"][aria-expanded="true"]{
#         max-width: 2500px;
#     }
#     """,
#     unsafe_allow_html=True,
# )  # set the sidebar width to be wider

st.write("Here are some instructions about using the episode renderer.")
rendering_demo()