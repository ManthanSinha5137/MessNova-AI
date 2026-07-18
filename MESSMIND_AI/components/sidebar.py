import streamlit as st
from services.session_service import session

def show_sidebar():
    user = session.get_session()

    with st.sidebar:
        st.title("🍽️ MessNova AI")

        st.divider()

        st.markdown(f"### 👋 {user['name']}")
        st.caption(user["role"])

        st.divider()

        if st.button("🚪 Logout", use_container_width=True):
            session.logout(clear_remember=True)
            st.rerun()