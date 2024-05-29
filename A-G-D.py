# import sqlite3
# import tkinter as tk
# from tkinter import messagebox

# # Função para criar ou atualizar a tabela no banco de dados
# def create_or_update_table():
#     conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
#     c = conn.cursor()  # Cria um cursor para executar comandos SQL
    
#     # Verifica se a tabela existe e se a coluna 'email' está presente
#     c.execute('''CREATE TABLE IF NOT EXISTS desempregados
#                  (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER, telefone TEXT, formacao TEXT)''')
    
#     # Adiciona a coluna 'email' se ela não existir
#     c.execute("PRAGMA table_info(desempregados)")
#     columns = [column[1] for column in c.fetchall()]
#     if 'email' not in columns:
#         c.execute("ALTER TABLE desempregados ADD COLUMN email TEXT")
    
#     conn.commit()  # Salva (commita) as alterações
#     conn.close()  # Fecha a conexão com o banco de dados

# # Chama a função para garantir que a tabela existe e está atualizada
# create_or_update_table()

# # Função para adicionar um novo desempregado ao banco de dados
# def add_desempregado():
#     nome = entry_nome.get()
#     idade = entry_idade.get()
#     telefone = entry_telefone.get()
#     formacao = entry_formacao.get()
#     email = entry_email.get()
    
#     # Verifica se todos os campos estão preenchidos
#     if not (nome and idade and telefone and formacao and email):
#         messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
#         return
    
#     conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
#     c = conn.cursor()  # Cria um cursor
#     c.execute("INSERT INTO desempregados (nome, idade, telefone, formacao, email) VALUES (?, ?, ?, ?, ?)", 
#               (nome, idade, telefone, formacao, email))
#     conn.commit()  # Salva as alterações
#     conn.close()  # Fecha a conexão
    
#     messagebox.showinfo("Sucesso", "Desempregado adicionado com sucesso!")
#     entry_nome.delete(0, tk.END)
#     entry_idade.delete(0, tk.END)
#     entry_telefone.delete(0, tk.END)
#     entry_formacao.delete(0, tk.END)
#     entry_email.delete(0, tk.END)
    
#     refresh_table()  # Atualiza a tabela

# # Função para deletar um desempregado do banco de dados pelo ID
# def delete_desempregado():
#     id = entry_id.get()  # Obtém o ID da entrada
    
#     if not id:
#         messagebox.showerror("Erro", "O campo de ID deve ser preenchido!")
#         return
    
#     conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
#     c = conn.cursor()  # Cria um cursor
#     c.execute("DELETE FROM desempregados WHERE id=?", (id,))
#     conn.commit()  # Salva as alterações
#     conn.close()  # Fecha a conexão
    
#     messagebox.showinfo("Sucesso", "Desempregado deletado com sucesso!")
#     entry_id.delete(0, tk.END)
    
#     refresh_table()  # Atualiza a tabela

# # Função para visualizar todos os desempregados no banco de dados
# def refresh_table():
#     for widget in frame.winfo_children():
#         widget.destroy()
    
#     conn = sqlite3.connect('desempregados.db')  # Conecta ao banco de dados
#     c = conn.cursor()  # Cria um cursor
#     c.execute("SELECT * FROM desempregados")
#     rows = c.fetchall()  # Obtém todos os registros
#     conn.close()  # Fecha a conexão
    
#     for row in rows:
#         tk.Label(frame, text=row).pack()

# # Cria a janela principal da aplicação
# root = tk.Tk()
# root.title("Gerenciamento de Desempregados")

# # Adiciona os rótulos e entradas para nome, idade, telefone, formação e email
# tk.Label(root, text="Nome").grid(row=0)
# tk.Label(root, text="Idade").grid(row=1)
# tk.Label(root, text="Telefone").grid(row=2)
# tk.Label(root, text="Formação").grid(row=3)
# tk.Label(root, text="Email").grid(row=4)

# entry_nome = tk.Entry(root)
# entry_idade = tk.Entry(root)
# entry_telefone = tk.Entry(root)
# entry_formacao = tk.Entry(root)
# entry_email = tk.Entry(root)

# entry_nome.grid(row=0, column=1)
# entry_idade.grid(row=1, column=1)
# entry_telefone.grid(row=2, column=1)
# entry_formacao.grid(row=3, column=1)
# entry_email.grid(row=4, column=1)

# # Adiciona botões para adicionar e verificar desempregados
# tk.Button(root, text="Adicionar", command=add_desempregado).grid(row=5, column=0)
# tk.Button(root, text="Verificar", command=refresh_table).grid(row=5, column=1)

# # Adiciona rótulo e entrada para deletar desempregado pelo ID
# tk.Label(root, text="ID para Deletar").grid(row=6)
# entry_id = tk.Entry(root)
# entry_id.grid(row=6, column=1)
# tk.Button(root, text="Deletar", command=delete_desempregado).grid(row=7, column=1)

# # Frame para exibir a tabela de desempregados
# frame = tk.Frame(root)
# frame.grid(row=8, column=0, columnspan=2)

# # Atualiza a tabela na inicialização
# refresh_table()

# # Inicia o loop principal da interface gráfica
# root.mainloop()
