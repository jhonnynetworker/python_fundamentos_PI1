from flask import Flask, render_template, request, redirect, url_for
import pyrebase

app = Flask(__name__)

# Configuração do Firebase
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

# Rota principal - Página Inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de adicionar desempregado
@app.route('/adiciona_desempregado', methods=['GET', 'POST'])
def adiciona_desempregado():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        telefone = request.form['telefone']
        formacao = request.form['formacao']
        email = request.form['email']
        
        # Lógica para salvar os dados no banco de dados do Firebase
        db = firebase.database()
        db.child("desempregados").push({
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
            "formacao": formacao,
            "email": email
        })
        
        return redirect(url_for('index'))
    
    return render_template('adiciona_desempregado.html')

# Rota para a página de cadastrar empresas
@app.route('/cadastra_empresas', methods=['GET', 'POST'])
def cadastra_empresas():
    if request.method == 'POST':
        nome_empresa = request.form['nome_empresa']
        nome_responsavel = request.form['nome_responsavel']
        endereco = request.form['endereco']
        telefone = request.form['telefone']
        email = request.form['email']
        data_fundacao = request.form['data_fundacao']
        setor = request.form['setor']
        
        # Lógica para salvar os dados no banco de dados do Firebase
        db = firebase.database()
        db.child("empresas").push({
            "nome_empresa": nome_empresa,
            "nome_responsavel": nome_responsavel,
            "endereco": endereco,
            "telefone": telefone,
            "email": email,
            "data_fundacao": data_fundacao,
            "setor": setor
        })
        
        return redirect(url_for('index'))
    
    return render_template('cadastra_empresas.html')

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            message = 'Login efetuado com sucesso.'
        except:
            message = 'Login falhou. Verifique suas credenciais e tente novamente.'
        return render_template('login.html', message=message)
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
