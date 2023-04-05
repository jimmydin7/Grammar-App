from flask import render_template, request, make_response, redirect

class User:
    def _check_proper_login(self, name, password):
        null_list = ['', None]
        error = None
        if name in null_list or password in null_list:
            error = 'Both username and password must be provided!'
        elif len(name) < 4 or len(name) > 20:
            error = 'Username is either too short or too long! Usernames must be between 4 and 20 characters.'
        elif ' ' in name:
            error = 'Usernames cannot contain spaces!'
        elif len(password) < 8 or len(password) > 20:
            error = 'Password is either too short or too long! Passwords must be between 8 and 20 characters.'
        elif name == password:
            error = 'Usernames cannot equal passwords!'
        return error
    
    def login(self):
        @self.app.route('/login')
        def login():
            return render_template('user/login.html', error=None, user=self.user_handler.get(request.cookies.get('key')))
        
        @self.app.route('/login-p', methods=['POST'])
        def loginp():
            name = request.form.get('username')
            password = request.form.get('password')

            error = self._check_proper_login(name, password)

            # If our login details are proper, then let's check for the user in the database
            key = None
            if error == None:
                auth = self.user_handler.check_login(name, password)
                if auth == False:
                    error = 'Authentication failed! Wrong username or password.'
                else:
                    # Generate a new key for next session
                    key = self.user_handler.generate_key(length=16)
                    auth['key'] = key
                    self.user_handler.db.save()

            res = make_response(render_template('user/login.html', error=error, user=self.user_handler.get(request.cookies.get('key'))))
            if key != None:
                res.set_cookie('key', key, max_age=63072000) # Sets a cookie with the key for 2 years

            return res
    def signup(self):
        @self.app.route('/signup')
        def signup():
            return render_template('user/signup.html', error=None, user=self.user_handler.get(request.cookies.get('key')))
        
        @self.app.route('/signup-p', methods=['POST'])
        def signupp():
            name = request.form.get('username')
            password = request.form.get('password')

            error = self._check_proper_login(name, password)

            # If our login details are proper, then let's check for the user in the database
            key = None
            if error == None:
                auth = self.user_handler.add(name, password)
                if not auth:
                    error = f'Account creation failed! The name "{name}" already exists! Please pick a different name.'
                else:
                    key = self.user_handler.get_name(name)['key']
                    

            res = make_response(render_template('user/signup.html', error=error, user=self.user_handler.get(request.cookies.get('key'))))
            if key != None:
                res.set_cookie('key', key, max_age=63072000) # Sets a cookie with the key for 2 years

            return res
    
    def logout(self):
        @self.app.route('/logout')
        def logout():
            res = make_response(redirect('/'))
            res.set_cookie('key', '', max_age=0)
            return res
