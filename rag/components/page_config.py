import streamlit as st


def set_page_config():
    st.set_page_config(
        page_title="Local RAG",
        page_icon="📚",
        layout="wide",
        initial_sidebar_state=st.session_state["sidebar_state"],
        menu_items={
            "Get Help": "https://github.com/jonfairbanks/local-rag/discussions",
            "Report a bug": "https://github.com/jonfairbanks/local-rag/issues",
        },
    )

    # Remove the Streamlit `Deploy` button from the Header
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .stAppDeployButton {
            visibility: hidden;
        }
        </style>
        """

    st.markdown(hide_menu_style, unsafe_allow_html=True)
