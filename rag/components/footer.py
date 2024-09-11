import streamlit as st


def set_page_footer():
    st.caption(
        "Upload your py file"
    )

    st.file_uploader("Upload your py file", type=["py"])
