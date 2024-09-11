import time

import streamlit as st

from components.chatbox import chatbox
from components.header import set_page_header
from components.footer import set_page_footer
from components.sidebar import sidebar

from components.page_config import set_page_config
from components.page_state import set_initial_state


def generate_welcome_message(msg):
    for char in msg:
        time.sleep(0.025)  # TODO: Find a better way -- This is blocking :(
        yield char


# Setup Initial State
set_initial_state()

# Page Setup
set_page_config()
set_page_header()
# set_page_footer()

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])
    # st.chat_message(msg["role"]).write_stream(generate_welcome_message(msg['content']))

# Sidebar
sidebar()

# Chat Box
chatbox()
