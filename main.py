from scripts.server import *

class App(BaseApp, Index):
    def __init__(self):
        super().__init__(__name__)
    
    def pages(self):
        self.index()

if __name__ == '__main__':
    app = App()
    app.pages()
    app.run(debug=True)