import os 

import streamlit as st

from sotopia.ui.socialstream.utils import initialize_session_state, reset_database


def update_database_callback() -> None:
    new_database_url = st.session_state.new_database_url
    updated_url = (
        new_database_url if new_database_url != "" else st.session_state.DEFAULT_DB_URL
    )
    try:
        reset_database(updated_url)
    except Exception as e:
        st.error(f"Error occurred while updating database: {e}, please try again.")

    st.session_state.current_database_url = updated_url
    initialize_session_state(force_reload=True)

    print("Updated DB URL: ", st.session_state.current_database_url)

# Page Configuration
st.set_page_config(page_title="SocialStream_Demo", page_icon="🧊", layout="wide")

display_intro = st.Page("./pages/intro.py", title="Introduction", icon=":material/home:")
display_episodes = st.Page("./pages/display_episodes.py", title="Episode", icon=":material/photo_library:")
display_scenarios = st.Page("./pages/display_scenarios.py", title="Scenarios", icon=":material/insert_drive_file:")
display_simple_chat = st.Page("./pages/simple_chat.py", title="Simple Chat", icon=":material/chat:")
display_omniscent_chat = st.Page("./pages/omniscient_chat.py", title="Omniscient Chat and Editing", icon=":material/add:")
# st.logo("./figs/haicosys.svg", icon_image="./figs/haicosys.svg", size="large", link="https://haicosystem.org")

pg = st.navigation([display_intro, display_scenarios, display_episodes, display_simple_chat, display_omniscent_chat])

# Reset active agent when switching modes across pages
if "mode" not in st.session_state or pg.title != st.session_state.get("mode", None):
    if "active" in st.session_state:
        del st.session_state["active"]
        # print("Active agent reset.")
    
    st.session_state.mode = pg.title


# DB URL Configuration
if "DEFAULT_DB_URL" not in st.session_state:
    st.session_state.DEFAULT_DB_URL = os.environ.get("REDIS_OM_URL", "")
    st.session_state.current_database_url = st.session_state.DEFAULT_DB_URL
    print("Default DB URL: ", st.session_state.DEFAULT_DB_URL)

# impl 2: popup update URL
with st.sidebar.popover("(Optional) Enter Database URL"):
    new_database_url = st.text_input(
    "URL: (starting in redis://)",
    value="",
    on_change=update_database_callback,
    key="new_database_url",
)


pg.run()
