from datetime import datetime
from services.remember_me_service import remember_me


class SessionManager:

    def __init__(self):
        self.current_user = None

    def create_session(self, user_data):

        self.current_user = {
            "id": user_data["id"],
            "name": user_data["name"],
            "email": user_data["email"],
            "role": user_data["role"],
            "login_time": datetime.now()
        }

    def get_session(self):
        return self.current_user

    def is_logged_in(self):
        return self.current_user is not None

    def logout(self, clear_remember=False):

        self.current_user = None

        if clear_remember:
            remember_me.clear()

        return True


session = SessionManager()