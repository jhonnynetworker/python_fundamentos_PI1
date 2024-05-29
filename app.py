# app.py
from flask import Flask
import firebase_admin
from config import init_firebase
from routes import auth_bp, product_bp, purchase_bp  

def create_app():
    if not firebase_admin._apps:
        init_firebase()

    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(product_bp, url_prefix='/product')
    app.register_blueprint(purchase_bp, url_prefix='/purchase')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
