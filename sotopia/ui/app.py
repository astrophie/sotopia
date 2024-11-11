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


def show_database_url_popup():
    """Reusable popup for entering and updating the Database URL."""
    with st.popover("(Optional) Database URL Configuration"):
        new_database_url = st.sidebar.text_input(
        "URL (starting in redis://)",
        value="",
        on_change=update_database_callback,
        key="new_database_url",
        )
        # db_url = st.text_input("Enter Database URL (starting with redis://)", key="new_database_url")
        # if st.button("Update Database URL"):
        #     update_database_callback()


# Page Configuration
st.set_page_config(page_title="SocialStream_Demo", page_icon="🧊", layout="wide")

display_intro = st.Page("./pages/intro.py", title="Introduction", icon=":material/home:")
display_episodes = st.Page("./pages/display_episodes.py", title="Episode", icon=":material/photo_library:")
display_scenarios = st.Page("./pages/display_scenarios.py", title="Scenarios", icon=":material/insert_drive_file:")
display_simple_chat = st.Page("./pages/simple_chat.py", title="Simple Chat", icon=":material/chat:")
display_omniscent_chat = st.Page("./pages/omniscient_chat.py", title="Omniscient Chat and Editing", icon=":material/add:")
# st.logo("./figs/haicosys.svg", icon_image="./figs/haicosys.svg", size="large", link="https://haicosystem.org")

pg = st.navigation([display_intro, display_scenarios, display_episodes, display_simple_chat, display_omniscent_chat])
pg.run()
