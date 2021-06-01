import pyperclip


class Credentials:
    '''
    class that creates instaces of user accounts
    '''
    cred_list = []

    def __init__(self, account, email, passlock):

        self.account = account
        self.email = email
        self.passlock = passlock

      # save credentials


    def save_cred(self):
        '''
        self credentials in cred_list
        '''
        Credentials.cred_list.append(self)
