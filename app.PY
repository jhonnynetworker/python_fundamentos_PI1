from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for
import sqlite3
import requests

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Chave secreta para a sessão

# Função para criar ou atualizar a tabela de desempregados no banco de dados
def create_or_update_table():
    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS desempregados
                 (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, telefone TEXT, formacao TEXT, email TEXT)''')
    conn.commit()
    conn.close()

# Função para criar ou atualizar a tabela de login no banco de dados
def create_or_update_login_table():
    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS login
                 (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

# Função para criar ou atualizar a tabela de cadastro de empresas no banco de dados
def create_or_update_empresa_table():
    conn = sqlite3.connect('cadastro_empresa.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cadastro_empresa
                 (id INTEGER PRIMARY KEY, nome_empresa TEXT, nome_responsavel TEXT, endereco TEXT, telefone TEXT, email TEXT, data_fundacao TEXT, sector TEXT)''')
    conn.commit()
    conn.close()

# Chama as funções para garantir que as tabelas existem e estão atualizadas
create_or_update_table()
create_or_update_login_table()
create_or_update_empresa_table()

# Substitua pelo endereço IP do computador do seu colaborador
REMOTE_HTML_SERVER = 'http://192.168.30.82:8000'

@app.route('/')
def index():
    response = requests.get(f'{REMOTE_HTML_SERVER}/index.html')
    return render_template_string(response.text)

@app.route('/add_desempregado', methods=['POST'])
def add_desempregado():
    if 'logged_in' not in session:
        return jsonify({"error": "Login obrigatório!"}), 401

    nome = request.form['nome']
    idade = request.form['idade']
    telefone = request.form['telefone']
    formacao = request.form['formacao']
    email = request.form['email']

    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute("INSERT INTO desempregados (nome, idade, telefone, formacao, email) VALUES (?, ?, ?, ?, ?)",
              (nome, idade, telefone, formacao, email))
    conn.commit()
    conn.close()

    return jsonify({"success": "Desempregado adicionado com sucesso!"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('login.db')
        c = conn.cursor()
        c.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['logged_in'] = True
            return jsonify({"success": "Login bem-sucedido!"})
        else:
            return jsonify({"error": "Credenciais inválidas!"})
    return render_template_string(requests.get(f'{REMOTE_HTML_SERVER}/login.html').text)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({"success": "Logout bem-sucedido!"})

# Rota para adicionar uma nova empresa ao banco de dados
@app.route('/add_empresa', methods=['POST'])
def add_empresa():
    if 'logged_in' not in session:
        return jsonify({"error": "Login obrigatório!"}), 401

    nome_empresa = request.form['nome_empresa']
    nome_responsavel = request.form['nome_responsavel']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    data_fundacao = request.form['data_fundacao']
    sector = request.form['sector']

    conn = sqlite3.connect('cadastro_empresa.db')
    c = conn.cursor()
    c.execute("INSERT INTO cadastro_empresa (nome_empresa, nome_responsavel, endereco, telefone, email, data_fundacao, sector) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (nome_empresa, nome_responsavel, endereco, telefone, email, data_fundacao, sector))
    conn.commit()
    conn.close()

    return jsonify({"success": "Empresa adicionada com sucesso!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
