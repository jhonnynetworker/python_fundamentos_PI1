# Importando as bibliotecas necessárias
from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import firestore
from flask_cors import CORS
from config import init_firebase

# Inicializa o Firebase se ainda não estiver inicializado
if not firebase_admin._apps:
    init_firebase()

# Cria uma instância do cliente do Firestore
db = firestore.client()

# Cria um Blueprint chamado 'product_bp' para agrupar rotas relacionadas a produtos
product_bp = Blueprint('product_bp', __name__)
CORS(product_bp)  # Permite requisições de origens diferentes (CORS)

class Product:
    """Classe para representar um produto."""

    def __init__(self, name, price_6_slices, price_8_slices, price_12_slices):
        """Inicializa um produto com seu nome e preços."""
        self.name = name
        self.price_6_slices = price_6_slices
        self.price_8_slices = price_8_slices
        self.price_12_slices = price_12_slices

    def to_dict(self):
        """Converte os dados do produto em um dicionário."""
        return {
            'name': self.name,
            'price_6_slices': self.price_6_slices,
            'price_8_slices': self.price_8_slices,
            'price_12_slices': self.price_12_slices,
        }


# Definições de Rotas

@product_bp.route('/products', methods=['GET'])
def get_products():
    """Obtém a lista de todos os produtos."""
    try:
        products_ref = db.collection('Produtos').stream()
        product_list = []
        for product in products_ref:
            prod_dict = product.to_dict()
            prod_dict['id'] = product.id
            product_list.append(prod_dict)
        return jsonify(product_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route('/product', methods=['POST'])
def add_product():
    """Adiciona um novo produto."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        name = data.get('name')
        price_6_slices = data.get('price_6_slices')
        price_8_slices = data.get('price_8_slices')
        price_12_slices = data.get('price_12_slices')

        if not name or not price_6_slices or not price_8_slices or not price_12_slices:
            return jsonify({"error": "Missing required fields"}), 400

        product = Product(name, price_6_slices, price_8_slices, price_12_slices)
        db.collection('Produtos').add(product.to_dict())
        return jsonify({"success": True}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Atualiza um produto existente."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        product_ref = db.collection('Produtos').document(product_id)
        product_ref.update(data)
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@product_bp.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Exclui um produto existente."""
    try:
        db.collection('Produtos').document(product_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500