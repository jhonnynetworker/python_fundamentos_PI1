from flask import Flask, render_template, request
import pyrebase

app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyDCFW1yyGD1R0Jj2-m-J6jlrDxd94XE",
    "authDomain": "a-g-d-3a987.firebaseapp.com",
    "databaseURL": "https://a-g-d-3a987-default-rtdb.firebaseio.com",
    "projectId": "a-g-d-3a987",
    "storageBucket": "a-g-d-3a987.appspot.com",
    "messagingSenderId": "455566970921",
    "appId": "1:455566970921:web:9cf5c76a47ed5e81aa8c38",
    "measurementId": "G-0GHV224VWQ"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['username']
    password = request.form['password']
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        message = 'Login efetuado com sucesso.'
    except:
        message = 'Login falhou. Verifique suas credenciais e tente novamente.'
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
