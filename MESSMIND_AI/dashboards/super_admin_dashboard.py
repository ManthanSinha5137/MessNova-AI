import streamlit as st

from components.sidebar import show_sidebar
from components.navbar import show_navbar
from components.metrics import show_metric_cards
from database import db


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