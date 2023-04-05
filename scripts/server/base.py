from flask import Flask


class BaseApp:
    def __init__(self, name):
        self.app = Flask(name)

    
    
    def run(self, debug=False):
        if debug:
            self.app.run(debug=True, host="0.0.0.0", port=5000)
        else:
            self.app.run(debug=False, host="0.0.0.0", port=5000)

if __name__ == '__main__':
    app = BaseApp()

    app.run(debug=True)