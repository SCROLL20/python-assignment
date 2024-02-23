# models/user.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_db(self):
        # Database insertion logic
        pass

    @classmethod
    def get_all_users(cls):
        # Fetch all users from the database
        pass
