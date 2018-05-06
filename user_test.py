import unittest #importing the unittest module

#<---First Class User---->#
from user import User #import the class from your other file.

class TestUser(unittest.TestCase):
    '''
    TestUser is a subclass of the parent class.
    unittest.TestCase helps in creating tests cases
    '''

    def setUp(self):#Setup Method is for defining instructions that will be executed before each test method.
        self.create_account = User("Claudia", "Njeri", "claudianjeri04@gmail", "claudia")

