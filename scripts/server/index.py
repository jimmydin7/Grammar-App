from flask import render_template, request

class Index:
    def index(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            txt = request.form.get('txt')

            if txt != None: txt = 'Corrected: ' + txt
            return render_template('index.html', txt=txt)