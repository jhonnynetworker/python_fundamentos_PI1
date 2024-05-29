from flask import Blueprint

# Criação de Blueprints para diferentes seções da aplicação
# Blueprints ajudam a organizar o código em componentes menores e reutilizáveis
auth_bp = Blueprint('auth', __name__)      # Blueprint para rotas de autenticação
product_bp = Blueprint('product', __name__) # Blueprint para rotas de produtos
purchase_bp = Blueprint('purchase', __name__) # Blueprint para rotas de pedidos/compra

# Importação dos módulos de rotas
# Estas importações devem vir depois da criação dos Blueprints para evitar importação circular
# Cada um desses módulos (auth_routes, product_routes, purchase_routes) deve definir as rotas correspondentes
from . import auth_routes, product_routes, purchase_routes
