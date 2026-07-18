from services.auth_service import auth
from services.session_service import session
from services.router_service import router
from services.remember_me_service import remember_me
from dashboards import (
    super_admin_dashboard,
    manager_dashboard,
    coordinator_dashboard,
    student_dashboard
)

auth.create_default_super_admin()
saved_user = remember_me.load_user()

if saved_user:

    print("Welcome Back!")
    print(saved_user)

    session.create_session(saved_user)

    success = True
    message = saved_user
else:

    success, message = auth.login_user(
        "kanhaasinha9@gmail.com",
        "Admin@123",
        remember=True
    )
if success:

    role = message["role"]

    dashboard = router.get_dashboard(role)

    print("\nDashboard Route:", dashboard)

    if dashboard == "dashboards/super_admin_dashboard.py":
        super_admin_dashboard.show()

    elif dashboard == "dashboards/manager_dashboard.py":
        manager_dashboard.show()

    elif dashboard == "dashboards/coordinator_dashboard.py":
        coordinator_dashboard.show()

    elif dashboard == "dashboards/student_dashboard.py":
        student_dashboard.show()

else:

    print(message)

print("\nSession After Login")
print(session.get_session())

print("\nLogging Out...")
session.logout()

print("\nSession After Logout")
print(session.get_session())