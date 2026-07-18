import streamlit as st

from components.sidebar import show_sidebar
from services.session_service import session
from database import db


def show_super_admin_dashboard():

    show_sidebar()

    user = session.get_session()

    st.title("👑 Super Admin Dashboard")
    st.caption(f"Welcome back, {user['name']}!")

    st.divider()

    # -------- Dashboard Statistics --------

    students = db.fetchone(
        "SELECT COUNT(*) FROM users WHERE role='Student'"
    )[0]

    managers = db.fetchone(
        "SELECT COUNT(*) FROM users WHERE role='Manager'"
    )[0]

    coordinators = db.fetchone(
        "SELECT COUNT(*) FROM users WHERE role='Coordinator'"
    )[0]

    admins = db.fetchone(
        "SELECT COUNT(*) FROM users WHERE role='Super Admin'"
    )[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("🎓 Students", students)
    col2.metric("👨‍💼 Managers", managers)
    col3.metric("🧑‍🤝‍🧑 Coordinators", coordinators)
    col4.metric("👑 Super Admins", admins)