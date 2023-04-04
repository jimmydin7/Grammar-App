from scripts.server import *
from scripts.ai import *
from scripts.server.user.handler import Handler

class App(BaseApp, Index, User):
    def __init__(self):
        super().__init__(__name__)
        
        self.ai = Ai()

        self.user_handler = Handler()
        # self.user_handler.migrate()

    
    def pages(self):
        self.index()
        self.login()

if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=True)