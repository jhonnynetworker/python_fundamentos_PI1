# from flask import Flask, send_file

# app = Flask(_name_)

# @app.route('/')
# def form():
#     return send_file('form.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#     # Aqui você colocaria a lógica para processar o formulário
#     pass

# @app.route('/style.css')
# def style():
#     return send_file('style.css')

# if _name_ == '_main_':
#     app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)  # Inicializar o Flask

# Função para criar ou atualizar a tabela no banco de dados
def create_or_update_table():
    conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
    c = conn.cursor()  # Cria um cursor para executar comandos SQL
    
    # Cria a tabela se não existir
    c.execute('''CREATE TABLE IF NOT EXISTS desempregados
                 (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, telefone TEXT, formacao TEXT, email TEXT)''')
    
    conn.commit()  # Salva (commita) as alterações
    conn.close()  # Fecha a conexão com o banco de dados

# # Chama a função para garantir que a tabela existe e está atualizada
# create_or_update_table()

# Rota para a página inicial
@app.route('/')
def home():
    conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
    c = conn.cursor()  # Cria um cursor
    c.execute("SELECT * FROM desempregados")
    rows = c.fetchall()  # Obtém todos os registros
    conn.close()  # Fecha a conexão
    
    return render_template('index.html', desempregados=rows)

# Função para adicionar um novo desempregado ao banco de dados
@app.route('/submit', methods=['POST'])
def add_desempregado():
    nome = request.form['nome']
    idade = request.form['idade']
    telefone = request.form['telefone']
    formacao = request.form['formacao']
    email = request.form['email']
    
    # Verifica se todos os campos estão preenchidos
    if not (nome and idade and telefone and formacao and email):
        return "Todos os campos devem ser preenchidos!", 400
    
    conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
    c = conn.cursor()  # Cria um cursor
    c.execute("INSERT INTO desempregados (nome, idade, telefone, formacao, email) VALUES (?, ?, ?, ?, ?)", 
              (nome, idade, telefone, formacao, email))
    conn.commit()  # Salva as alterações
    conn.close()  # Fecha a conexão
    
    return redirect('/')

# Função para deletar um desempregado do banco de dados pelo ID
@app.route('/delete', methods=['POST'])
def delete_desempregado():
    id = request.form['id']
    
    if not id:
        return "O campo de ID deve ser preenchido!", 400
    
    conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
    c = conn.cursor()  # Cria um cursor
    c.execute("DELETE FROM desempregados WHERE id=?", (id,))
    conn.commit()  # Salva as alterações
    conn.close()  # Fecha a conexão
    
    return redirect('/')

# Verificação de entrada principal
if __name__ == '__main__':
    app.run(debug=True)
