from flask import Blueprint, request, jsonify
import firebase_admin
from firebase_admin import auth, firestore, credentials
from flask_cors import CORS
from config import init_firebase



# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    init_firebase()

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)  # Allow cross-origin requests

@auth_bp.route('/google-login', methods=['POST'])
def google_login():
    try:
        # Get Email from Request
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Query Firestore
        db = firestore.client()
        users_ref = db.collection('Usuario')
        query = users_ref.where('email', '==', email).limit(1).get()

        # Check if User Exists
        if query:
            user_data = query[0].to_dict()
            # Check if required data (e.g., name, age) exists
            if 'nome' in user_data and 'idade' in user_data:
                return jsonify({"message": "User found", "user": user_data}), 200
            else:
                return '', 206
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/fill-data', methods=['POST'])
def fill_data():
    try:
        # Get data from the request
        data = request.json
        nome = data.get('name')
        idade = data.get('age')
        email = data.get('email')

        if not nome or not idade or not email:
            return jsonify({"error": "Name, age, and email are required"}), 400

        # Save the data to Firestore
        db = firestore.client()
        users_ref = db.collection('Usuarios')
        users_ref.add({
            'nome': nome,
            'idade': idade,
            'email': email
        })

        return jsonify({"message": "User data saved successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


""" from flask import Blueprint, request, jsonify, redirect, url_for
import firebase_admin
from firebase_admin import auth, firestore, credentials
from flask_cors import CORS
from config import init_firebase

# Ensure Firebase is initialized only once
if not firebase_admin._apps:
    init_firebase()

auth_bp = Blueprint('auth', __name__)
CORS(auth_bp)  # Allow cross-origin requests

@auth_bp.route('/google-login', methods=['POST'])
def google_login():
    try:
        # Get Email from Request
        email = request.json.get('email')
        if not email:
            return jsonify({"error": "Email is required"}), 400

        # Query Firestore
        db = firestore.client()
        users_ref = db.collection('Usuarios')
        query = users_ref.where('email', '==', email).limit(1).get()

        # Check if User Exists
        if query:
            user_data = query[0].to_dict()
            # Check if required data (e.g., name, age) exists
            if 'nome' in user_data and 'idade' in user_data:
                return jsonify({"message": "User found", "user": user_data}), 200
            else:
                return '', 206
        else:
            return jsonify({"error": "User not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/fill-data', methods=['POST'])
def fill_data():
    try:
        # Get data from the request
        data = request.json
        nome = data.get('name')
        idade = data.get('age')
        email = data.get('email')

        if not nome or not idade or not email:
            return jsonify({"error": "Name, age, and email are required"}), 400

        # Save the data to Firestore
        db = firestore.client()
        users_ref = db.collection('Usuarios')
        users_ref.add({
            'nome': nome,
            'idade': idade,
            'email': email
        })

        return jsonify({"message": "User data saved successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

 """