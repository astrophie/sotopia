import streamlit as st

st.set_page_config(page_title="SocialStream_Demo", page_icon="🧊", layout="wide")

# st.set_page_config(page_title="Sotopia", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "Xuhui Zhou from CMU LTI: https://xuhuiz.com/"})

display_intro = st.Page("./pages/intro.py", title="Introduction", icon=":material/home:")
display_episodes = st.Page("./pages/display_episodes.py", title="Scenarios", icon=":material/photo_library:")
display_simple_chat = st.Page("./pages/simple_chat.py", title="Simple Chat", icon=":material/chat:")
display_omniscent_chat = st.Page("./pages/omniscent_chat.py", title="Omniscent Chat and Editing", icon=":material/add:")
# st.logo("./figs/haicosys.svg", icon_image="./figs/haicosys.svg", size="large", link="https://haicosystem.org")

pg = st.navigation([display_intro, display_episodes, display_simple_chat, display_omniscent_chat])
pg.run()