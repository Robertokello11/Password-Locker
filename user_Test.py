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

     def test_save_user(self):
        '''
        confirm if the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

         # 3rd test ## saving users ##

     def test_save_mutliple_users(self):
        '''
        check whether you can store more than one user
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

        #4th test## Delete user ##

     def test_delete_user(self):
        '''
        check whether one can delete a user account
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)


     ##5th test#

     def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("Robert")
        self.assertEqual(found_user.username, self.new_user.username)



if __name__ == '__main__':
  unittest.main()  
   