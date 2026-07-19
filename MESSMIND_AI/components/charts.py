import streamlit as st
import pandas as pd


def show_user_distribution(students, managers, coordinators, admins):

    st.subheader("📊 User Distribution")

    data = pd.DataFrame(
        {
            "Role": [
                "Students",
                "Managers",
                "Coordinators",
                "Super Admin"
            ],
            "Users": [
                students,
                managers,
                coordinators,
                admins
            ]
        }
    )

    st.bar_chart(
        data.set_index("Role")
    )