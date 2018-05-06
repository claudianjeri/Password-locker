import unittest #importing the unittest module

#<---First Class User---->#
from user import User #import the class from your other file.


class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class.
    unittest.TestCase helps in creating tests cases
    '''

    def setUp(self):#Setup Method is for defining instructions that will be executed before each test method.
        self.new_account = User("Claudia", "Njeri", "claudianjeri04@gmail.com", "claudia")

    def tearDown(self):#This code is executed before each test case.
                       #and its work is to clean up after each test case has run.
        User.user_createaccount = []

    def test_init(self):
        self.assertEqual(self.new_account.first_name, "Claudia")
        self.assertEqual(self.new_account.last_name, "Njeri")
        self.assertEqual(self.new_account.email, "claudianjeri04@gmail.com")
        self.assertEqual(self.new_account.password, "claudia")

    def test_save_account(self):
        self.new_account.save_account()
        self.assertEqual(len(User.user_createaccount), 1)

    # def test_first_name(self):
    #     self.new_account.save_account()
    #     self.assertEqual(len(User.user_createaccount),2)

    def test_log_in(self):
        self.new_account.save_account()
        log_in = User("Claudia", "Njeri", "claudianjeri04@gmail.com", "claudia")
        log_in.save_account()

        account_exists = User.account_exists("claudianjeri04@gmail.com", "claudia")
        self.assertTrue(account_exists)

#<---Second Class for credentials---->#
from user import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        
        self.user_credential = Credentials("claudianjeri", "claudianjeri04@gmail.com", "claudia04" )

    def tearDown(self):
            
        Credentials.user_credentials = []

    def test_init(self):
        self.assertEqual(self.user_credential.account_name, "claudianjeri")
        self.assertEqual(self.user_credential.email, "claudianjeri04@gmail.com")
        self.assertEqual(self.user_credential.password, "claudia04")
    
    def test_save_credentials(self):
        self.user_credential.save_credentials()
        self.assertEqual(len(Credentials.user_credentials), 1)

if __name__ == '__main__':
    unittest.main()
    
