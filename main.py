from scripts.server import *
from scripts.server.user.handler import Handler

class App(BaseApp, Index):
    def __init__(self):
        super().__init__(__name__)
        
        user_handler = Handler()
        # user_handler.migrate()

    
    def pages(self):
        self.index()

if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=True)