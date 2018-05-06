class User:
    user_createaccount= []

    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_account(self):
        User.user_createaccount.append(self)

    