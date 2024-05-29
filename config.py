import firebase_admin
from firebase_admin import credentials, firestore, auth

def init_firebase():
    cred = credentials.Certificate('/home/jbrito/Documentos/pi1/python/crosta-crocante.json')
    firebase_admin.initialize_app(cred)
    return firestore.client()

db = init_firebase()
