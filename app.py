from flask import Flask, render_template

import firebase_admin
from routes.auth_routes import auth_bp
from routes.product_routes import product_bp
from routes.purchase_routes import purchase_bp
from config import init_firebase

def create_app():
    if not firebase_admin._apps:
        init_firebase()

    app = Flask(__name__)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(purchase_bp, url_prefix='/purchase')

    # Configuración de la política de seguridad de contenido (CSP)
    @app.after_request
    def add_security_headers(response):
        response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self' 'unsafe-inline' *.googleapis.com heapanalytics.com vercel.com *.vercel.com *.vercel.sh vercel.live *.stripe.com twitter.com *.twitter.com *.github.com *.codesandbox.io wss://*.vercel.com localhost:* chrome-extension://* https://www.gstatic.com;"
        return response

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/produtos')
    def produtos():
        return render_template('produtos.html')

    @app.route('/pedirmenu')
    def pedirmenu():
        return render_template('pedirmenu.html')

    @app.route('/UML')
    def UML():
        return render_template('UML.html')

    @app.route('/form')
    def form():
        return render_template('form.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
