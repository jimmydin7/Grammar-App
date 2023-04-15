from flask import Flask


class BaseApp:
    def __init__(self, name):
        self.app = Flask(name)

    
    
    def run(self, debug=False):
        self.app.run(debug=debug, host="0.0.0.0", port=5000)

if __name__ == '__main__':
    app = BaseApp()

    app.run(debug=True)