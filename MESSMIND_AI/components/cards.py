import streamlit as st


def show_quick_actions():

    st.subheader("⚡ Quick Actions")
    st.write("Frequently used admin actions")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Student", use_container_width=True):
            st.info("Student Module will be added in Phase 3.")

        if st.button("➕ Add Coordinator", use_container_width=True):
            st.info("Coordinator Module will be added in Phase 3.")

    with col2:
        if st.button("👨‍💼 Add Manager", use_container_width=True):
            st.info("Manager Module will be added in Phase 3.")

        if st.button("📊 View Reports", use_container_width=True):
            st.info("Reports Module will be added in Phase 6.")

def show_recent_activity():

    st.subheader("📋 Recent Activity")

    activities = [
        "👑 Super Admin logged in",
        "🎓 Student module initialized",
        "👨‍💼 Manager module ready",
        "📊 Dashboard loaded successfully",
    ]

    for activity in activities:
        st.success(activity)