import streamlit as st

def show_navbar(user_name="Admin", role="Super Admin"):
    col1, col2 = st.columns([8, 2])

    with col1:
        st.title("🍽️ MessNova AI")

    with col2:
        st.markdown(f"""
        **👤 {user_name}**

        {role}
        """)