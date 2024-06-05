from flask import Flask, render_template_string, request, jsonify
import sqlite3
import requests

app = Flask(__name__)

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

# Chama as funções para garantir que as tabelas existem e estão atualizadas
create_or_update_table()
create_or_update_login_table()

# Substitua pelo endereço IP do computador do seu colaborador
REMOTE_HTML_SERVER = 'http://192.168.30.82:8000'

@app.route('/')
def index():
    response = requests.get(f'{REMOTE_HTML_SERVER}/index.html')
    return render_template_string(response.text)

@app.route('/add_desempregado', methods=['POST'])
def add_desempregado():
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
            return jsonify({"success": "Login bem-sucedido!"})
        else:
            return jsonify({"error": "Credenciais inválidas!"})
    return render_template_string(requests.get(f'{REMOTE_HTML_SERVER}/login.html').text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
