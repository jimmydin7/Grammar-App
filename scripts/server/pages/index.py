from flask import render_template, request


class Index:
    def index(self):
        @self.app.route('/about')
        def about():
            return render_template('about.html', user=self.handler.get(request.cookies.get('key')))

        @self.app.route('/')
        def index():
            return render_template('index.html', user=self.handler.get(request.cookies.get('key')))

        @self.app.errorhandler(404)
        def page_not_found(e):
            return render_template('user/404.html'), 404









