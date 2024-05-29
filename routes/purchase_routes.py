from flask import request, jsonify, Blueprint
from models import Purchase
from config import db


purchase_bp = Blueprint('purchase', __name__)

def register_purchase_routes(purchase_bp):
    @purchase_bp.route('/purchases', methods=['GET'])
    def get_purchases():
        purchases_ref = db.collection('purchases')
        purchases = purchases_ref.stream()
        purchase_list = [purchase.to_dict() for purchase in purchases]
        return jsonify(purchase_list), 200

    @purchase_bp.route('/purchase', methods=['POST'])
    def add_purchase():
        data = request.get_json()
        purchase = Purchase(data['product_id'], data['quantity'])
        db.collection('purchases').add(purchase.to_dict())
        return jsonify({"success": True}), 201


""" from flask import request, jsonify
from . import purchase_bp
from models import Purchase
from config import db

@purchase_bp.route('/purchases', methods=['GET'])
def get_purchases():
    purchases_ref = db.collection('purchases')
    purchases = purchases_ref.stream()

    purchase_list = [purchase.to_dict() for purchase in purchases]
    return jsonify(purchase_list), 200

@purchase_bp.route('/purchase', methods=['POST'])
def add_purchase():
    data = request.get_json()
    purchase = Purchase(data['product_id'], data['quantity'])
    db.collection('purchases').add(purchase.to_dict())
    return jsonify({"success": True}), 201
 """