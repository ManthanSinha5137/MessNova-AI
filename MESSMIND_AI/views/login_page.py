import streamlit as st

from services.auth_service import auth
from services.session_service import session
from services.remember_me_service import remember_me


def show_login():
    """Display the Login Page"""

    st.title("🍽️ MessNova AI")
    st.subheader("Welcome Back 👋")

    # Login Form
    with st.form("login_form"):

        email = st.text_input(
            "📧 Email",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter your password"
        )

        remember = st.checkbox("Remember Me")

        login_button = st.form_submit_button("🚀 Login")

    # Handle Login
    if login_button:

        if not email or not password:
            st.warning("Please enter both email and password.")
            return

        success, message = auth.login_user(
            email=email,
            password=password,
            remember=remember
        )

        if success:

            st.success("✅ Login Successful!")

            st.rerun()

        else:
            st.error(message)