import ui.ui as ui

def id():
    while True:
        id = input("\033[1;32mID:\033[0;0m")
        if id == "":
            ui.erro_entrada_vazia()
            continue
        elif len(id) != 8:
            print("\033[1;31m" + "ERRO: " + "\033[0;37m" + "O ID deve conter 8 dígitos." + "\033[0m")
            continue
        else:
            return id.strip(" ")
def nome():
    while True:
        nome = input("\033[1;32mNome Completo:\033[0;0m")
        if nome == "":                  
            ui.erro_entrada_vazia()
            continue
        temp = ''.join(nome.split(' '))     #remove os espaços do nome informado. Ex: Pedro Mateus > PedroMateus
        for i in temp:                      #verifica se tem algum numero no nome.
            if i.isdigit():
                print("Digite um nome válido.")
                break
        else:                               #só entra no "else" se nao tiver nehuma quebra de loop.
            return nome.strip(" ") #retorna o nome sem espaços
def email():
    while True:
        email = input("\033[1;32mEmail:\033[0;0m")
        if email == "":
            ui.erro_entrada_vazia()
        elif "@" in email and ".com" in email: #verifica se o email informado tem "@" e ".com"
            return email.strip(" ")
        else:
            print('Email inválido! Deve conter \033[1;32m"@"\033[0;0m e \033[1;32m".com"\033[0;0m')
def telefone():
    while True:
        telefone = input("\033[1;32mTelefone:\033[0;0m")
        if telefone == '':
            ui.erro_entrada_vazia()
            continue
        if not telefone.isnumeric():
            print("Digite apenas números!")
            continue
        else:
            if 9 <= len(telefone) <= 11:
                return telefone
            else:
                print("O número deve ter entre \033[1;32m9 - 11\033[0;0m caracteres.")
#validar p| editar usuario.
def validar_atual_email():
    while True:
        email = input("\033[1;32mInforme o email cadastrado:\033[0;0m")
        if email == "":
            ui.erro_entrada_vazia()
        elif "@" in email and ".com" in email: #verifica se o email informado tem "@" e ".com"
            return email.strip(" ")
        else:
            ui.clear_terminal()
            print('Email inválido! Deve conter \033[1;32m"@"\033[0;0m e \033[1;32m".com"\033[0;0m')
def validar_novo_email():
    while True:
        email = input("\033[1;32mInforme o novo email:\033[0;0m")
        if email == "":
            ui.erro_entrada_vazia()
        elif "@" in email and ".com" in email: #verifica se o email informado tem "@" e ".com"
            return email.strip(" ")
        else:
            ui.clear_terminal()
            print('Email inválido! Deve conter \033[1;32m"@"\033[0;0m e \033[1;32m".com"\033[0;0m')
def validar_atual_nome():
    while True:
        nome = input("\033[1;32mInforme o nome cadastrado:\033[0;0m")
        if nome == "":                  
            ui.erro_entrada_vazia()
            continue
        temp = ''.join(nome.split(' '))    
        for i in temp:                      
            if i.isdigit():
                ui.clear_terminal()
                print("Digite um nome válido.")
                break
        else:            
            return nome.strip(" ")
def validar_novo_nome():
    while True:
        nome = input("\033[1;32mInforme o novo nome:\033[0;0m")
        if nome == "":                  
            ui.erro_entrada_vazia()
            continue
        temp = ''.join(nome.split(' '))    
        for i in temp:                      
            if i.isdigit():
                ui.clear_terminal()
                print("Digite um nome válido.")
                break
        else:            
            return nome.strip(" ")
def validar_atual_telefone():
    while True:
        telefone = input("\033[1;32mInforme o telefone cadastrado:\033[0;0m")
        if telefone == '':
            ui.erro_entrada_vazia()
            continue
        if not telefone.isnumeric():
            ui.clear_terminal()
            print("Digite apenas números!")
            continue
        else:
            if 9 <= len(telefone) <= 11:
                return telefone
            else:
                ui.clear_terminal()
                print("O número deve ter entre \033[1;32m9 - 11\033[0;0m caracteres.")
def validar_novo_telefone():
    while True:
        telefone = input("\033[1;32mInforme o novo telefone:\033[0;0m")
        if telefone == '':
            ui.erro_entrada_vazia()
            continue
        if not telefone.isnumeric():
            ui.clear_terminal()
            print("Digite apenas números!")
            continue
        else:
            if 9 <= len(telefone) <= 11:
                return telefone
            else:
                ui.clear_terminal()
                print("O número deve ter entre \033[1;32m9 - 11\033[0;0m caracteres.")