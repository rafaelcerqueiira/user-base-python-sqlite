import sqlite3
import uuid
import ui.ui as ui
import os 

#iniciar banco de dados.
# Pega o diretório onde db.py está (database), evita criar outras tabelas em raiz
B = os.path.join(os.path.dirname(__file__), "dados.db")
def total_usuarios():
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM dados")
    total = cursor.fetchone()[0]
    print(f"|      \033[1;32mTOTAL DE USUÁRIOS:\033[0;0m{total}     |")
    conn.close()
    return total
def verficar_numero_de_usuarios():
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM dados")
    total = cursor.fetchone()[0]
    conn.close()
    return total
def connect():
    conn = sqlite3.connect(B) #conectar ao banco dados.
    cursor = conn.cursor() #responsavel por executar os comandos para o banco.
    cursor.execute("""CREATE TABLE IF NOT EXISTS dados (id TEXT PRIMARY KEY, nome TEXT, email TEXT, telefone TEXT)""")#cria tabela para armazenar os dados.
    conn.commit()
    conn.close()
#verificar usuarios para adicionar.
def buscar_nome(nome):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM dados WHERE nome = ?", (nome,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado
def buscar_email(email):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM dados WHERE email = ?", (email,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado
def buscar_telefone(telefone):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT telefone FROM dados WHERE telefone = ?", (telefone,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado
#buscar usuarios.
def buscar_por_id(id_buscar):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE id = ?", (id_buscar,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        print("==========================")
        print("|      \033[1;32mEncontrado!\033[0;0m       |")
        print("==========================")
        print(f"\033[1;32mID\033[0;0m:{resultado[0]}")
        print(f"\033[1;32mNome\033[0;0m:{resultado[1]}")
        print(f"\033[1;32mEmail\033[0;0m:{resultado[2]}")
        print(f"\033[1;32mTelefone\033[0;0m:{resultado[3]}\n")
    else:
        ui.erro_id_nao_encontrado()
def buscar_por_email(email_buscar):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE email = ?", (email_buscar,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        print("==========================")
        print("|      \033[1;32mEncontrado!\033[0;0m       |")
        print("==========================")
        print(f"\033[1;32mID\033[0;0m:{resultado[0]}")
        print(f"\033[1;32mNome\033[0;0m:{resultado[1]}")
        print(f"\033[1;32mEmail\033[0;0m:{resultado[2]}")
        print(f"\033[1;32mTelefone\033[0;0m:{resultado[3]}\n")
    else:
        ui.erro_email_nao_encontrado()
def buscar_por_nome(nome_buscar):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE nome = ?", (nome_buscar,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        print("==========================")
        print("|      \033[1;32mEncontrado!\033[0;0m       |")
        print("==========================")
        print(f"\033[1;32mID\033[0;0m:{resultado[0]}")
        print(f"\033[1;32mNome\033[0;0m:{resultado[1]}")
        print(f"\033[1;32mEmail\033[0;0m:{resultado[2]}")
        print(f"\033[1;32mTelefone\033[0;0m:{resultado[3]}\n")
    else:
        ui.erro_nome_nao_encontrado()
def buscar_por_telefone(telefone_buscar):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados WHERE telefone = ?", (telefone_buscar,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        print("==========================")
        print("|      \033[1;32mEncontrado!\033[0;0m       |")
        print("==========================")
        print(f"\033[1;32mID\033[0;0m:{resultado[0]}")
        print(f"\033[1;32mNome\033[0;0m:{resultado[1]}")
        print(f"\033[1;32mEmail\033[0;0m:{resultado[2]}")
        print(f"\033[1;32mTelefone\033[0;0m:{resultado[3]}\n")
    else:
        ui.erro_telefone_nao_encontrado()
#salvar o cadastro no banco de dados.
def salvar_cadastro(nome, email, telefone):
    id_cadastro = str(uuid.uuid4())[:8]  # gera o ID de cadastro
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dados VALUES (?, ?, ?, ?)", (id_cadastro, nome, email, telefone))
    conn.commit()
    conn.close()
#listar usuários.
def listar_usuarios():
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados")
    for resultado in cursor.fetchall():
        print(resultado)
    conn.close()
#editar usuario.
def editar_usuario_email(email, email_novo):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("UPDATE dados SET email = ? WHERE email = ?", (email_novo, email))
    #retorna valor se for alterado algum dado.
    if cursor.rowcount == 0:
        print("Erro: email não foi alterado")
    else:
        conn.commit()
    conn.close()
def editar_usuario_nome(nome, nome_novo):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("UPDATE dados SET nome = ? WHERE nome = ?", (nome_novo, nome))
    #retorna valor se for alterado algum dado.
    if cursor.rowcount == 0:
        print("Erro: nome não foi alterado")
    else:
        conn.commit()
    conn.close()
def editar_usuario_telefone(telefone, telefone_novo):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("UPDATE dados SET telefone = ? WHERE telefone = ?", (telefone_novo, telefone))
    #retorna valor se for alterado algum dado.
    if cursor.rowcount == 0:
        print("Erro: telefone não foi alterado")
    else:
        conn.commit()
    conn.close()
#excluir usuario.
def excluir_cadastro_nome(nome):
    conn = sqlite3.connect(B)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dados WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()