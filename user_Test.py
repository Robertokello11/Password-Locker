import unittest  #Import unittest module
from user import user # importing the contact class
class TestUser(unittest.TestCase):

     def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("Robert", "Robert11") #new User created

     def tearDown(self):
        '''
        clean up to prevent errors
        '''
        User.user_list = []

     # Test 2 ##   

     def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "Robert")
        self.assertEqual(self.new_user.password, "Robert11")
 