import auth.auth as auth
import ui.ui as ui
import database.db as db

db.connect()
ui.clear_terminal()
while True:
    escolha = ui.menu_principal()
    if escolha == '1':
        auth.cadastro()
    elif escolha == '2':
        total_usuarios_p_buscar = db.verficar_numero_de_usuarios()
        if total_usuarios_p_buscar > 0:
            ui.clear_terminal()
            auth.buscar_usuario()
        else:
            ui.clear_terminal()
            ui.titulo_verificar_usuarios_existente_para_acesso()
    elif escolha == '3':
        total_usuarios_p_listar = db.verficar_numero_de_usuarios()
        if total_usuarios_p_listar > 0: 
            auth.listar_todos_usuarios()
        else:
            ui.clear_terminal()
            ui.titulo_verificar_usuarios_existente_para_acesso()
    elif escolha == '4':
        total_usuarios_p_editar = db.verficar_numero_de_usuarios()
        if total_usuarios_p_editar > 0:
            auth.editar_usuario()
        else:
            ui.clear_terminal()
            ui.titulo_verificar_usuarios_existente_para_acesso()
    elif escolha == '5':
        total_usuarios_p_excluir = db.verficar_numero_de_usuarios()
        if total_usuarios_p_excluir > 0:
            auth.excluir_usuario()
        else:
            ui.clear_terminal()
            ui.titulo_verificar_usuarios_existente_para_acesso()
    elif escolha == '0':
        ui.clear_terminal()
        auth.sair()
        break
    else:
        ui.clear_terminal()
        ui.erro_opcao_invalida_menu_principal()
    