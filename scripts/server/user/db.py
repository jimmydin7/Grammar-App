from os import listdir
import json

class Database:
    def __init__(self, file):
        self.file = file
        if self.file not in listdir():
            file = open(self.file, 'w')
            file.write('{}')
            file.close()
            self.data = {}
        else:
            self.load()

    def load(self):
        file = open(self.file)
        self.data = json.load(file)
        file.close()

        # Check if the 'users' key exists, and create it if it doesn't
        if 'users' not in self.data:
            self.data['users'] = []

    def save(self):
        file = open(self.file, 'w')
        file.write(json.dumps(self.data))
        file.close()
