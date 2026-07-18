import streamlit as st

from components.theme import load_theme
from views.login_page import show_login

from services.session_service import session
from services.router_service import router

# Dashboard imports
from dashboards.super_admin_dashboard import show_super_admin_dashboard
from dashboards.manager_dashboard import show_manager_dashboard
from dashboards.coordinator_dashboard import show_coordinator_dashboard
from dashboards.student_dashboard import show_student_dashboard


# ----------------------------------
# Streamlit Config
# ----------------------------------

st.set_page_config(
    page_title="MessNova AI",
    page_icon="🍽️",
    layout="wide"
)

load_theme()

# ----------------------------------
# Check Login
# ----------------------------------

if not session.is_logged_in():

    show_login()

else:

    user = session.get_session()

    role = user["role"]

    if role == "Super Admin":
        show_super_admin_dashboard()

    elif role == "Manager":
        show_manager_dashboard()

    elif role == "Coordinator":
        show_coordinator_dashboard()

    elif role == "Student":
        show_student_dashboard()

    else:
        st.error("Unknown user role.")