# Importa as bibliotecas necessárias
from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import auth, firestore, credentials
from flask_cors import CORS
from config import init_firebase

# Ggarantiza que el firebase sea iniciado solo una vez 
if not firebase_admin._apps:
    init_firebase()

# Cria um Blueprint 'auth' para agrupar rutas relacionadas à autenticação
auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)  # Permite pedidos de origenes diferentes (CORS)

# Definir ruta para login com Google
@auth_bp.route('/google-login', methods=['POST'])
def google_login():
    try:
        # Obtém o email a partir do pedido
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "Email is required"}), 400  # Retorna um erro se o email não for fornecido

        # Consulta o Firestore
        db = firestore.client()
        users_ref = db.collection('Usuario')
        query = users_ref.where('email', '==', email).limit(1).stream()

        # Verifica se o usuário existe
        user_data = None
        for doc in query:
            user_data = doc.to_dict()
            break
        
        if user_data:
            # Verifica se  existem os dados necessários ( nome, idade) 
            if 'nome' in user_data and 'idade' in user_data:
                return jsonify({"message": "User found", "user": user_data}), 200  # Retorna os dados do usuário
            else:
                return '', 206  # Retorna um status indicando que os dados estão incompletos
        else:
            return jsonify({"error": "User not found"}), 404  # Retorna um erro se o usuário não for encontrado

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção

# Define uma rota para preencher os dados do usuário
@auth_bp.route('/fill-data', methods=['POST'])
def fill_data():
    try:
        # Obtém os dados do pedido
        data = request.json
        nome = data.get('name')
        idade = data.get('age')
        email = data.get('email')

        if not nome or not idade or not email:
            return jsonify({"error": "Name, age, and email are required"}), 400  # Retorna um erro se algum dado estiver faltando

        # Salva os dados no firebase
        db = firestore.client()
        users_ref = db.collection('Usuario')
        users_ref.add({
            'nome': nome,
            'idade': idade,
            'email': email
        })

        return jsonify({"message": "User data saved successfully"}), 201  # Retorna uma mensagem de sucesso (salvo os dados)

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna um erro genérico em caso de exceção