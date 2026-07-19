import streamlit as st


def show_metric_cards(students, managers, coordinators, admins):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🎓 Students",
            value=students,
            help="Total Registered Students"
        )

    with col2:
        st.metric(
            label="👨‍💼 Managers",
            value=managers,
            help="Total Registered Managers"
        )

    with col3:
        st.metric(
            label="🧑‍🤝‍🧑 Coordinators",
            value=coordinators,
            help="Total Registered Coordinators"
        )

    with col4:
        st.metric(
            label="👑 Super Admin",
            value=admins,
            help="Total Super Admins"
        )