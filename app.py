# Importa as bibliotecas necessárias
from flask import Flask
import firebase_admin  # Importa o firebase_admin
from routes.auth_routes import auth_bp  # Importa o Blueprint auth_bp das rotas de autenticação
from routes.product_routes import product_bp  # Importa o Blueprint product_bp das rotas de produtos
from routes.purchase_routes import purchase_bp  # Importa o Blueprint purchase_bp das rotas de pedidos
from config import init_firebase  # Importa apenas a função init_firebase do módulo config

# Define a função para criar a aplicação Flask
def create_app():
    # Inicializa o Firebase apenas se ainda não estiver inicializado
    if not firebase_admin._apps:
        init_firebase()  # Chama a função init_firebase para inicializar o Firebase

    app = Flask(__name__)  # Cria uma instância da aplicação Flask

    # Registra os Blueprints para diferentes rotas, com prefixos de URL
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Registra o Blueprint de autenticação
    app.register_blueprint(product_bp, url_prefix='/product')  # Registra o Blueprint de produtos
    app.register_blueprint(purchase_bp, url_prefix='/purchase')  # Registra o Blueprint de pedidos

    return app  # Retorna a aplicação Flask configurada

# Executa a aplicação Flask se este arquivo for executado como script principal
if __name__ == '__main__':
    app = create_app()  # Cria a aplicação chamando a função create_app
    app.run(debug=True)  # Executa a aplicação em modo debug