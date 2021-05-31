import unittest  #Import unittest module
from user import user # importing the contact class
class TestUser(unittest.TestCase):

     def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("Robert", "Robert11") #new User created
