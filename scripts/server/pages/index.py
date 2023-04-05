from flask import render_template, request, redirect
import re
from textblob import TextBlob


class Index:

    def index(self):
        @self.app.route('/about')
        def about():
            return render_template('about.html', user=self.handler.get(request.cookies.get('key')))

        @self.app.route('/', methods=['GET', 'POST'])
        def index():

            # Layer 1 - Text Processing
            txt = request.form.get('txt')

            if txt != None:
                key = request.cookies.get('key')
                if key != None and self.handler.get(key) != None:  # This will be None if the user is not logged in.
                    
                    # Layers 1-3 - handles some misspellings
                    txt = self.ai.layers1_3(txt)
                    
                    # Layer 4 - Parse with gingerit for final and accurate result
                    txt = self.ai.layer4(txt)

                    return render_template('index.html', txt=txt, user=self.handler.get(request.cookies.get('key')))
                else:
                    return redirect('/signup')
            else:
                return render_template('index.html', txt=txt, user=self.handler.get(request.cookies.get('key')))






