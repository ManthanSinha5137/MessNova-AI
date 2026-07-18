import json
import os


class RememberMeService:

    FILE_NAME = "remember_me.json"

    def save_user(self, user_data):

        with open(self.FILE_NAME, "w") as file:
            json.dump(user_data, file)

    def load_user(self):

        if not os.path.exists(self.FILE_NAME):
            return None

        try:
            with open(self.FILE_NAME, "r") as file:
                return json.load(file)

        except Exception:
            return None

    def clear(self):

        if os.path.exists(self.FILE_NAME):
            os.remove(self.FILE_NAME)


remember_me = RememberMeService()