from flask import Flask, render_template, request, jsonify
import sqlite3

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_desempregado():
    data = request.get_json()
    nome = data.get('nome')
    idade = data.get('idade')
    telefone = data.get('telefone')
    formacao = data.get('formacao')
    email = data.get('email')
    
    if not (nome and idade and telefone and formacao and email):
        return jsonify({"error": "Todos os campos devem ser preenchidos!"})
    
    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute("INSERT INTO desempregados (nome, idade, telefone, formacao, email) VALUES (?, ?, ?, ?, ?)",
              (nome, idade, telefone, formacao, email))
    conn.commit()
    conn.close()
    
    return jsonify({"success": "Desempregado adicionado com sucesso!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('login.db')
    c = conn.cursor()
    c.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()

    if user:
        return jsonify({"success": "Login bem-sucedido!"})
    else:
        return jsonify({"error": "Credenciais inválidas!"})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)

