from flask import render_template, request, redirect


class Index:
    def index(self):
        @self.app.route('/about', methods=['GET'])
        def about():
            return render_template('user/about.html')

        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            
            txt = request.form.get('txt')
            if txt != None:
                key = request.cookies.get('key')
                if key != None and self.user_handler.get(key) != None: # This will be None if the user is not logged in.
                    # This will return the grammaticly changed code, keep in mind that this is not the final module. It is just a demonstration
                    txt = self.ai.parser.parse(txt)['result']
                    return render_template('index.html', txt=txt, user=self.user_handler.get(request.cookies.get('key')))
                else:
                    return redirect('/signup')
            else:
                return render_template('index.html', txt=txt, user=self.user_handler.get(request.cookies.get('key')))



