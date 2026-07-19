import streamlit as st

from components.sidebar import show_sidebar
from components.navbar import show_navbar
from components.metrics import show_metric_cards
from database import db
from components.cards import show_quick_actions
from components.cards import show_recent_activity
from components.charts import show_user_distribution

def show_super_admin_dashboard():

    show_sidebar()

    show_navbar()

    st.divider()

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

    show_metric_cards(
        students,
        managers,
        coordinators,
        admins
    )
    st.divider()

    show_quick_actions()

    st.divider()

    show_recent_activity()

    st.divider()

    show_user_distribution(
    students,
    managers,
    coordinators,
    admins
)