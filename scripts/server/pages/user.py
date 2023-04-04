from flask import render_template, request, make_response, redirect

class User:
    def _check_proper_login(self, name, password):
        null_list = ['', None]
        error = None
        if name in null_list or password in null_list:
            error = 'Both username and password must be provided!'
        elif len(name) < 5 or len(name) > 20:
            error = 'Username is either too short or too long! Usernames must be between 5 and 20 characters.'
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
            return render_template('user/login.html', error=None)
        @self.app.route('/loginp', methods=['POST'])
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

            res = make_response(render_template('user/login.html', error=error))
            if key != None:
                res.set_cookie('key', key, max_age=63072000) # Sets a cookie with the key for 2 years

            return res
