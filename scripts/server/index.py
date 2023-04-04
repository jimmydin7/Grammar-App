from flask import render_template, request
from gingerit.gingerit import GingerIt

class Index:
    def index(self):
        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            txt = request.form.get('txt')

            if txt != None:
                parser = GingerIt()
                txt = parser.parse(txt)['result']
                

                # This will return the grammaticly changed code, keep in mind that this is not the final module. It is just a demonstration
            return render_template('index.html', txt=txt)
