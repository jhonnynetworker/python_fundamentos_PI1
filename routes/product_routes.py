# Importa as bibliotecas necessárias
from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import firestore
from flask_cors import CORS
from config import init_firebase

# Inicializa o Firebase se ainda não estiver inicializado
if not firebase_admin._apps:
    init_firebase()

# Cria uma conexion do cliente do Firestore
db = firestore.client()

# Cria um Blueprint chamado 'product_bp' para agrupar rotas relacionadas a produtos
product_bp = Blueprint('product_bp', __name__)
CORS(product_bp)  # Permite pedidos de origens diferentes (CORS)

# Define a classe Product
class Product:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'size': self.size
        }

# Define a rota para obter a lista de produtos
@product_bp.route('/products', methods=['GET'])
def get_products():
    try:
        # Consulta a coleção 'Produtos' no Firestore
        products_ref = db.collection('Produtos')
        products = products_ref.stream()
        product_list = []
        for product in products:
            prod_dict = product.to_dict()
            prod_dict['id'] = product.id  # Inclui o ID do documento
            product_list.append(prod_dict)
        return jsonify(product_list), 200  # Retorna a lista de produtos
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção

# Define a rota para adicionar um novo produto
@product_bp.route('/product', methods=['POST'])
def add_product():
    try:
        # Obtém os dados da pedido
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400  # Retorna um erro se os dados forem inválidos

        name = data.get('name')
        price = data.get('price')
        size = data.get('size')

        if not name or not price or not size:
            return jsonify({"error": "Missing required fields"}), 400  # Retorna um erro se algum campo obrigatório estiver faltando

        # Cria uma instância da classe Product e salva no Firestore
        product = Product(name, price, size)
        db.collection('Produtos').add(product.to_dict())
        return jsonify({"success": True}), 201  # Retorna uma mensagem de sucesso
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção

# Define a rota para atualizar um produto existente
@product_bp.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    try:
        # Obtém os dados da requisição
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400  # Retorna um erro se os dados forem inválidos

        # Atualiza o documento do produto no Firestore com os novos dados
        product_ref = db.collection('Produtos').document(product_id)
        product_ref.update(data)
        return jsonify({"success": True}), 200  # Retorna uma mensagem de sucesso (se actualizo)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção

# Define a rota para deletar um produto existente
@product_bp.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        # Deleta o documento do produto no Firestore
        db.collection('Produtos').document(product_id).delete()
        return jsonify({"success": True}), 200  # Retorna uma mensagem de sucesso
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção