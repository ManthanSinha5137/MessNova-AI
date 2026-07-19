import streamlit as st
from datetime import datetime
from services.session_service import session


def show_navbar():

    user = session.get_session()

    left, right = st.columns([8, 2])

    with left:
        st.title("🍽️ MessNova AI")
        st.caption(f"Welcome back, {user['name']} 👋")

    with right:
        st.write(f"📅 {datetime.now().strftime('%d %b %Y')}")
        st.write(f"🕒 {datetime.now().strftime('%I:%M %p')}")