# Importa as bibliotecas necessárias
from flask import request, jsonify
from . import purchase_bp  # Importa o Blueprint 'purchase_bp' do pacote atual
from config import db  # Importa a instância do banco de dados Firestore do módulo config

# Define a rota para obter a lista de compras (pedidos)
@purchase_bp.route('/pedidos', methods=['GET'])
def get_purchases():
    # Consulta a coleção 'Pedidos' no Firestore
    purchases_ref = db.collection('Pedidos')
    purchases = purchases_ref.stream()

    # Converte os documentos em dicionários e adiciona à lista de compras
    purchase_list = [purchase.to_dict() for purchase in purchases]
    return jsonify(purchase_list), 200  # Retorna a lista de compras em formato JSON com status 200 (OK)

# Define a rota para adicionar uma nova compra (pedido)
@purchase_bp.route('/pedidos', methods=['POST'])
def add_purchase():
    # Obtém os dados da requisição
    data = request.get_json()
    # Cria uma instância da classe Purchase com os dados fornecidos
    purchase = Purchase(data['product_id'], data['quantity'])
    # Adiciona o novo pedido à coleção 'Pedidos' no Firestore
    db.collection('Pedidos').add(purchase.to_dict())
    return jsonify({"success": True}), 201  # Retorna uma mensagem de sucesso com status 201 (Criado)