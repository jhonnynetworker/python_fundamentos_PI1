# product_routes.py
from flask import request, jsonify, Blueprint
from models import Product
from config import db

product_bp = Blueprint('product', __name__)

def register_product_routes(app):
    @app.route('/products', methods=['GET'])
    def get_products():
        products_ref = db.collection('products')
        products = products_ref.stream()
        product_list = [product.to_dict() for product in products]
        return jsonify(product_list), 200

    @app.route('/product', methods=['POST'])
    def add_product():
        data = request.get_json()
        product = Product(data['name'], data['price'])
        db.collection('products').add(product.to_dict())
        return jsonify({"success": True}), 201

    @app.route('/product/<product_id>', methods=['PUT'])
    def update_product(product_id):
        data = request.get_json()
        product_ref = db.collection('products').document(product_id)
        product_ref.update(data)
        return jsonify({"success": True}), 200

    @app.route('/product/<product_id>', methods=['DELETE'])
    def delete_product(product_id):
        db.collection('products').document(product_id).delete()
        return jsonify({"success": True}), 200


""" from flask import request, jsonify, Blueprint
from models import Product
from config import db

def register_routes(product_bp):
    @product_bp.route('/products', methods=['GET'])
    def get_products():
        products_ref = db.collection('products')
        products = products_ref.stream()

        product_list = [product.to_dict() for product in products]
        return jsonify(product_list), 200

    @product_bp.route('/product', methods=['POST'])
    def add_product():
        data = request.get_json()
        product = Product(data['name'], data['price'])
        db.collection('products').add(product.to_dict())
        return jsonify({"success": True}), 201

    @product_bp.route('/product/<product_id>', methods=['PUT'])
    def update_product(product_id):
        data = request.get_json()
        product_ref = db.collection('products').document(product_id)
        product_ref.update(data)
        return jsonify({"success": True}), 200

    @product_bp.route('/product/<product_id>', methods=['DELETE'])
    def delete_product(product_id):
        db.collection('products').document(product_id).delete()
        return jsonify({"success": True}), 200

 """


""" from flask import request, jsonify
from . import product_bp
from models import Product
from config import db

@product_bp.route('/products', methods=['GET'])
def get_products():
    products_ref = db.collection('products')
    products = products_ref.stream()

    product_list = [product.to_dict() for product in products]
    return jsonify(product_list), 200

@product_bp.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(data['name'], data['price'])
    db.collection('products').add(product.to_dict())
    return jsonify({"success": True}), 201

@product_bp.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product_ref = db.collection('products').document(product_id)
    product_ref.update(data)
    return jsonify({"success": True}), 200

@product_bp.route('/product/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    db.collection('products').document(product_id).delete()
    return jsonify({"success": True}), 200
 """