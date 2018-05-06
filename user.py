class User:
    
    user_createaccount = []

    def __init__(self,first_name,last_name,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_account(self):
        User.user_createaccount.append(self)

    @classmethod
    def account_exists(cls, email, password):

        for account in cls.user_createaccount:
            if account.email == email and account.password == password:

                return True
        
        return False  

class Credentials:

    user_credentials = []

    def __init__(self, account_name, email, password):
        self.account_name = account_name
        self.email = email
        self.password = password

    def save_credentials(self):
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        Credentials.user_credentials.remove(self)

    @classmethod
    def display_credentials(cls):

        return cls.user_credentials

    @classmethod
    def find_by_account_name(cls,account_name):

        for account in cls.user_credentials:
            if account.account_name == account_name:
                return account