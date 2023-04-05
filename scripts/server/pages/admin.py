from flask import render_template, request, redirect


class Admin:
    def _check_admin(self):
        user = self.handler.get(request.cookies.get('key'))
        if user != None and user['permission-level'] > 0:
            return True
        else:
            return False
    def admin(self):
        @self.app.route('/admin/dashboard')
        def admin_dashboard():
            if self._check_admin():
                return render_template('admin/dashboard.html', user=self.handler.get(request.cookies.get('key')))
            else:
                return redirect('/')
            
        @self.app.route('/admin/users')
        def admin_users():
            if self._check_admin():
                return render_template(
                    'admin/users.html',
                    user=self.handler.get(request.cookies.get('key')),
                    users=self.handler.db.data['users']
                    )
            else:
                return redirect('/')
        
        @self.app.route('/admin/users/<username>')
        def admin_user(username):
            if self._check_admin():
                return render_template(
                    'admin/user.html',
                    user=self.handler.get(request.cookies.get('key')),
                    open_user=self.handler.get_name(username)
                    )
            else:
                return redirect('/')
            
        @self.app.route('/admin/users/<username>/update', methods=['POST'])
        def admin_user_update(username):
            if self._check_admin():
                updated_user = {}
                for i in self.handler.default_user:
                    if i == 'permission-level':
                        updated_user[i] = int(request.form.get(i))
                    else:
                        updated_user[i] = request.form.get(i)

                self.handler.remove(updated_user['key'])
                self.handler.add_raw(updated_user)

                return redirect('/admin/users/' + username)
            else:
                return redirect('/')
            
        @self.app.route('/admin/users/<username>/remove')
        def admin_user_remove(username):
            if self._check_admin():
                user = self.handler.get_name(username)

                self.handler.remove(user['key'])


                return redirect('/admin/users')
            else:
                return redirect('/')
                    

