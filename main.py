from scripts.server import *
from scripts.ai import *
from scripts.server.database.handler import Handler

class App(BaseApp, Index, User, Admin):
    def __init__(self):
        super().__init__(__name__)
        
        self.ai = Ai(self)

        self.handler = Handler()
        # self.user_handler.migrate()

    def pages(self):
        self.index()

        self.login()
        self.signup()
        self.logout()

        self.admin()

if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=False)