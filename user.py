###User class###
class User:
    '''
    class that generates new instances of user
    '''
    user_list = [] #list of user to be stored here

    def _init_(self, username, password):
        '''
        saving user credentials into user_list for login code
        '''