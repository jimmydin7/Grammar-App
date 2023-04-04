from random import choice

from .db import Database

class Handler:
    def __init__(self):
        '''Initializes the User Handler and the Database.'''
        self.default_user = {
            'name':None,
            'password':None,
            'permission-level':0
        }
        self.db = Database('db.json')
    
    def generate_key(self, length):
        '''Generates a random key from the given length'''
        chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        key = ''
        for i in range(length): key += choice(chars)
        return key

    def get(self, key):
        '''Get's a user's data using their key.'''
        try:
            return self.db.data['users'][key]
        except KeyError:
            return None
    
    def get_name(self, name):
        '''Get's a user's data using their name.'''
        user = None
        for key in self.db.data['users']:
            if name.lower() == self.db.data['users'][key]['name'].lower():
                user = self.db.data['users'][key]
        return user
    
    def add(self, name, password):
        '''
        Checks for name duplicates, and if the
        coast is clear: add user and save to database.
        '''
        if self.get_name(name) == None:
            key = self.generate_key(length=16)
            user = self.default_user.copy()

            user['name'] = name
            user['password'] = password

            self.db.data['users'][key] = user
            self.db.save()
            return True
        else:
            return False
    
    def migrate(self):
        '''
        Migrates the user database to the current user version.
        "self.default_user" defines what the current user stores and "self.migrate()"
        will update all users to be like "self.default_user."
        '''
        new_users = {}
        for key in self.db.data['users']:
            old_user = self.db.data['users'][key]
            new_user = self.default_user.copy()
            for k in old_user:
                if k in new_user:
                    new_user[k] = old_user[k]

            new_users[key] = new_user
        self.db.data['users'] = new_users
        self.db.save()
    
    def remove(self, key):
        '''Removes a user from the database using the given key.'''
        try:
            del self.db.data['users'][key]
            self.db.save()
            return True
        except KeyError:
            return False
