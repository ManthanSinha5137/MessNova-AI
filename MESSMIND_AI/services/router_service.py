class RouterService:

    def get_dashboard(self, role):

        routes = {
            "Super Admin": "dashboards/super_admin_dashboard.py",
            "Manager": "dashboards/manager_dashboard.py",
            "Coordinator": "dashboards/coordinator_dashboard.py",
            "Student": "dashboards/student_dashboard.py"
        }

        return routes.get(role, None)


router = RouterService()