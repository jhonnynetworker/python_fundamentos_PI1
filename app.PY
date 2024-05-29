from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def create_or_update_table():
    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS desempregados
                 (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, telefone TEXT, formacao TEXT, email TEXT)''')
    conn.commit()
    conn.close()

create_or_update_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/desempregados', methods=['GET'])
def get_desempregados():
    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute("SELECT * FROM desempregados")
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/adicionar_desempregado', methods=['POST'])
def adicionar_desempregado():
    nome = request.form['nome']
    idade = request.form['idade']
    telefone = request.form['telefone']
    formacao = request.form['formacao']
    email = request.form['email']
    
    if not (nome and idade and telefone and formacao and email):
        return "Todos os campos devem ser preenchidos!", 400
    
    conn = sqlite3.connect('desempregados.db')
    c = conn.cursor()
    c.execute("INSERT INTO desempregados (nome, idade, telefone, formacao, email) VALUES (?, ?, ?, ?, ?)",
              (nome, idade, telefone, formacao, email))
    conn.commit()
    conn.close()
    
    return "Desempregado adicionado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
