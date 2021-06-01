from credentials import Credentials
from user import User
import random

#user create account#

def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user

#save the user#

