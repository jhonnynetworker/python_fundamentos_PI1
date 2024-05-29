# Importa as bibliotecas necessárias do Firebase Admin SDK
import firebase_admin
from firebase_admin import credentials, firestore, auth

# Define a função para inicializar o Firebase
def init_firebase():
    # Carrega as credenciais do Firebase a partir de um arquivo JSON
    cred = credentials.Certificate('/home/jbrito/Documentos/pi1/python/crosta-crocante.json')
    # Inicializa o aplicativo Firebase com as credenciais fornecidas
    firebase_admin.initialize_app(cred)
    # Retorna o cliente Firestore inicializado
    return firestore.client()

# Inicializa o Firebase e obtém o cliente Firestore
db = init_firebase()


