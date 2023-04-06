from flask import render_template, request, redirect


class Grammar:
    def grammar(self):
        @self.app.route('/grammar', methods=['GET', 'POST'])
        def grammar():

            # Layer 1 - Text Processing
            txt = request.form.get('txt')

            if txt != None:
                key = request.cookies.get('key')
                if key != None and self.handler.get(key) != None:  # This will be None if the user is not logged in.
                    
                    # Layers 1-3 - handles some misspellings
                    txt = self.ai.layers1_3(txt)
                    
                    # Layer 4 - Parse with gingerit for final and accurate result
                    txt = self.ai.layer4(txt)

                    return render_template('grammar.html', txt=txt, user=self.handler.get(request.cookies.get('key')))
                else:
                    return redirect('/signup')
            else:
                return render_template('grammar.html', txt=txt, user=self.handler.get(request.cookies.get('key')))






