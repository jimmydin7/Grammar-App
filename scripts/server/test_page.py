from flask import render_template, request, redirect # play with redirect

class TestPage:
    def test_page(self):
        @self.app.route('/test')
        def test():
            return 'Test worked!'
    def test_page_name(self):
        @self.app.route('/test/name/<name>')
        def test_name(name):
            if name == 'redir':
                return self.redirect('/test')
            else:
                return f'Hello {name}!'
    
    def test_input(self):
        @self.app.route('/test/input')
        def test_input():
            return render_template('server-test.html')
    
    def test_process(self):
        @self.app.route('/test/process', methods=['POST'])
        def test_process():
            test = request.form.get('test')
            return self.redirect('/test/name/' + test)