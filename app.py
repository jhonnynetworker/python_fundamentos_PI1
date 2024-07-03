from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Função para conectar ao banco de dados específico
def get_db_connection(db_name):
    conn = sqlite3.connect(f'{db_name}.db')
    conn.row_factory = sqlite3.Row
    return conn

# Função para criar tabelas nas bases de dados
def create_tables():
    # Base de dados 1: Desempregados
    conn = get_db_connection('desempregados')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS desempregados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            formacao TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    # Base de dados 2: Empresas
    conn = get_db_connection('empresas')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_empresa TEXT NOT NULL,
            nome_responsavel TEXT NOT NULL,
            endereco TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL,
            data_fundacao TEXT NOT NULL,
            setor TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    # Base de dados 3: Usuários
    conn = get_db_connection('usuarios')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Chamada para criar as tabelas
create_tables()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = get_db_connection('usuarios')
    conn.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/add_desempregado', methods=['POST'])
def add_desempregado():
    nome = request.form['nome']
    idade = request.form['idade']
    formacao = request.form['formacao']
    email = request.form['email']
    
    conn = get_db_connection('desempregados')
    conn.execute('INSERT INTO desempregados (nome, idade, formacao, email) VALUES (?, ?, ?, ?)', (nome, idade, formacao, email))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/add_empresa', methods=['POST'])
def add_empresa():
    nome_empresa = request.form['nome_empresa']
    nome_responsavel = request.form['nome_responsavel']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    data_fundacao = request.form['data_fundacao']
    setor = request.form['setor']
    
    conn = get_db_connection('empresas')
    conn.execute('INSERT INTO empresas (nome_empresa, nome_responsavel, endereco, telefone, email, data_fundacao, setor) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                 (nome_empresa, nome_responsavel, endereco, telefone, email, data_fundacao, setor))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
