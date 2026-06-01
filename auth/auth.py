import validators.validators as validators
import sqlite3
import time
import ui.ui as ui
import database.db as db

def cadastro():
    ui.titulo_criar_conta()

    #verificar se o email já existe no banco de dados.
    while True:
        nome = validators.nome()
        if db.buscar_nome(nome):
            print(f"\033[1;31mERRO:\033[0;0m O nome '{nome}' já está em uso. Informe outro.")
        else:
            break
    #verificar se o email já exite no banco de dados.
    while True:
        email = validators.email()
        if db.buscar_email(email): #retorna a buscar e se achar algo mostra o "print" de erro.
            print(f"\033[1;31mERRO:\033[0;0m O email '{email}' já está em uso. Informe outro.")
        else:
            break
    # verificar se telefone já existe no banco de dados.
    while True:
        telefone = validators.telefone()
        if db.buscar_telefone(telefone):
            print(f"\033[1;31mERRO:\033[0m O telefone '{telefone}' já está em uso. Digite outro.")
        else:
            break

    #salvar o cadastro.
    db.salvar_cadastro(nome, email, telefone)
    print("\033[1;32mCriando conta...\033[0m")
    time.sleep(4)
    ui.clear_terminal()
    ui.titulo_conta_criada()
def buscar_usuario():
    while True:
        ui.titulo_buscar_usuario()
        opcao = ui.menu_buscar_usuario()
        ui.clear_terminal()
        #id
        if opcao == '1':
            ui.titulo_buscar_id()
            id = validators.id()
            ui.clear_terminal()
            db.buscar_por_id(id)
            input("\033[1;32mPressione Enter para voltar ao menu...\033[0;0m")
            ui.clear_terminal()
            break
        #email
        elif opcao == '2':
            ui.titulo_buscar_email()
            email = validators.email()
            ui.clear_terminal()
            db.buscar_por_email(email)
            input("\033[1;32mPressione Enter para voltar ao menu...\033[0;0m")
            ui.clear_terminal()
            break
        #nome
        elif opcao == '3':
            ui.titulo_buscar_nome()
            nome = validators.nome()
            ui.clear_terminal()
            db.buscar_por_nome(nome)
            input("\033[1;32mPressione Enter para voltar ao menu...\033[0;0m")
            ui.clear_terminal()
            break
        #telefone
        elif opcao == '4':
            ui.titulo_buscar_telefone()
            telefone = validators.telefone()
            ui.clear_terminal()
            db.buscar_por_telefone(telefone)
            input("\033[1;32mPressione Enter para voltar ao menu...\033[0;0m")
            ui.clear_terminal()
            break
        #sair / voltar p menu
        elif opcao == '0':
            ui.clear_terminal()
            break
        else:
            ui.clear_terminal()
            ui.erro_opcao_invalida_buscar_usuario()
            continue
            
def listar_todos_usuarios():
    ui.clear_terminal()
    ui.titulo_listar_usuarios()
    print("\033[1;32mCarregando dados...\033[0m")
    time.sleep(5)
    ui.clear_terminal()
    ui.titulo_usuarios_listados()
    print()
    db.listar_usuarios()
    print()
    input("\033[1;32mPressione Enter para voltar ao menu...\033[0;0m")
    ui.clear_terminal() 
def editar_usuario():
    ui.clear_terminal()
    ui.titulo_editar_usuario()
    while True:
        escolha = ui.menu_editar_usuario()
        #editar email
        if escolha == '1':
            while True:
                ui.titulo_editar_usuario_email()
                email = validators.validar_atual_email()
                if db.buscar_email(email):
                    print("\033[1;32mVerificando email...\033[0;0m")
                    time.sleep(3)
                    print("Email encontrado e validado com sucesso!")
                    ui.clear_terminal()
                    break
                else:
                    ui.clear_terminal()
                    print("\033[1;32mEmail não encontrado no banco de dados.\033[0;0m\n")
                    continue
            while True:
                email_novo = validators.validar_novo_email()
                if not db.buscar_email(email_novo):
                    print("\033[1;32mVerificando email...\033[0;0m")
                    time.sleep(3)
                    ui.clear_terminal()
                    ui.titulo_email_atualizado_sucesso()
                    break
                else:
                    print("O email já está em uso.")
                    continue
            db.editar_usuario_email(email, email_novo)
            break 
        #editar nome
        elif escolha == '2':
            while True:
                ui.titulo_editar_usuario_nome()
                nome = validators.validar_atual_nome()
                if db.buscar_nome(nome):
                    print("\033[1;32mVerificando nome...\033[0;0m")
                    time.sleep(3)
                    print("Nome encontrado e validado com sucesso!")
                    ui.clear_terminal()
                    break
                else:
                    ui.clear_terminal()
                    print("\033[1;32mNome não encontrado no banco de dados.\033[0;0m\n")
                    continue
            while True:
                nome_novo = validators.validar_novo_nome()
                if not db.buscar_nome(nome_novo):
                    print("\033[1;32mVerificando nome...\033[0;0m")
                    time.sleep(3)
                    ui.clear_terminal()
                    ui.titulo_nome_atulizado_sucesso()
                    break
                else:
                    print("O nome já está em uso.")
                    continue
            db.editar_usuario_nome(nome, nome_novo)
            break
        #editar telefone
        elif escolha == '3':
            while True:
                ui.titulo_editar_usuario_telefone()
                telefone = validators.validar_atual_telefone()
                if db.buscar_telefone(telefone):
                    print("\033[1;32mVerificando telefone...\033[0;0m")
                    time.sleep(3)
                    print("Telefone encontrado e validado com sucesso!")
                    ui.clear_terminal()
                    break
                else:
                    ui.clear_terminal()
                    print("\033[1;32mTelefone não encontrado no banco de dados.\033[0;0m\n")
                    continue
            while True:
                ui.titulo_editar_usuario_telefone()
                telefone_novo = validators.validar_novo_telefone()
                if not db.buscar_telefone(telefone_novo):
                    print("\033[1;32mVerificando telefone...\033[0;0m")
                    time.sleep(3)
                    ui.clear_terminal()
                    ui.titulo_telefone_atualizado_sucesso()
                    break
                else:
                    print("O telefone já está em uso.")
                    continue
            db.editar_usuario_telefone(telefone, telefone_novo)
            break
        # sair | voltar p menu
        elif escolha == '0':
            ui.clear_terminal()
            break
        else:
            ui.clear_terminal()
            ui.erro_opcao_invalida_editar_usuario()
            continue
def excluir_usuario():
        ui.clear_terminal()
        while True:
            ui.titulo_excluir_conta()
            nome = validators.nome()
            if db.buscar_nome(nome):
                ui.clear_terminal()
                ui.titulo_nome_encontrado()
                n = (input("\033[1;32mConfirmar e apagar?\033[0m Sim[\033[1;32m1\033[0m] Não[\033[1;31m2\033[0m] "))
                if not n.isnumeric():
                    print("Informe apenas números!")
                    continue
                n = int(n)
                if n == 1:
                    db.excluir_cadastro_nome(nome)
                    print("Excluindo usuário...")
                    time.sleep(3)
                    ui.clear_terminal()
                    ui.titulo_usuario_excluido()
                    break
                elif n == 2:
                    print("Cancelando...")
                    time.sleep(3)
                    ui.clear_terminal()
                    break
                else:
                    ui.clear_terminal()
                    ui.titulo_opcao_invalida_exluir_usuario()
                    continue
            else:
                ui.clear_terminal()
                ui.titulo_usuario_nao_encontrado()
                continue
def sair():
    print("\033[1;32mFechando sistema...\033[0;0m")
    time.sleep(5)
    ui.clear_terminal()