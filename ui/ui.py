import os
import database.db as db
#limpar terminal
def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')
#menus
def menu_principal():
    print('======= >>> \033[1;32mUser Base\033[0;0m ==========')
    print('|  [''\033[1;32m''1''\033[0;0m''] Cadastrar Usuário       |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Buscar Usuário          |')
    print('|  [''\033[1;32m''3''\033[0;0m''] Listar Todos Usuários   |')
    print('|  [''\033[1;32m''4''\033[0;0m''] Editar Usuário          |')
    print('|  [''\033[1;32m''5''\033[0;0m''] Excluir Usuário         |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Sair                    |')
    print('================================')
    db.total_usuarios()
    print('================================')
    op = input('\033[1;32m''Insira a opção: ''\033[0;0m')
    return op
def menu_buscar_usuario():
    print('================================')
    print('|  [''\033[1;32m''1''\033[0;0m''] Id de Cadastro          |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Email                   |')
    print('|  [''\033[1;32m''3''\033[0;0m''] Nome Completo           |')
    print('|  [''\033[1;32m''4''\033[0;0m''] Telefone                |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Menu Principal <<<      |')
    print('================================')
    opb = input("\033[1;32mSelecione uma opção de Busca: \033[0;0m")
    clear_terminal()
    return opb
def menu_editar_usuario():
    print('================================')
    print('|  [''\033[1;32m''1''\033[0;0m''] Email                   |')
    print('|  [''\033[1;32m''2''\033[0;0m''] Nome Completo           |')
    print('|  [''\033[1;32m''3''\033[0;0m''] Telefone                |')
    print('|  [''\033[1;32m''0''\033[0;0m''] Menu Principal <<<      |')
    print('================================')
    ope = input("\033[1;32mSelecione uma opção para editar: \033[0;0m")
    clear_terminal()
    return ope
#titulos
def titulo_buscar_id():
    print("================================")
    print("|          \033[1;32mBUSCAR ID\033[0;0m           |")
    print("================================")
def titulo_buscar_email():
    print("================================")
    print("|         \033[1;32mBUSCAR EMAIL\033[0;0m         |")
    print("================================")
def titulo_buscar_nome():
    print("================================")
    print("|         \033[1;32mBUSCAR NOME\033[0;0m          |")
    print("================================")
def titulo_buscar_telefone():
    print("================================")
    print("|        \033[1;32mBUSCAR TELEFONE\033[0;0m       |")
    print("================================")
def titulo_criar_conta():
    clear_terminal()
    print("=========================")
    print("|      \033[1;32mCRIAR CONTA\033[0;0m      |")
    print("=========================")
def titulo_buscar_usuario():
    print("================================")
    print("|       \033[1;32mBUSCAR USUÁRIO!\033[0;0m        |")
    print("================================")
def titulo_editar_usuario():
    print("================================")
    print("|       \033[1;32mEDITAR USUÁRIO!\033[0;0m        |")
    print("================================")
def titulo_conta_excluida():
    print("=================================")
    print("|         \033[1;32mCONTA EXCLUÍDA!\033[0;0m         |")
    print("=================================")
def titulo_excluir_conta():
    print("===================================")
    print("|         \033[1;32mEXCLUIR USUÁRIO!\033[0;0m        |")
    print("===================================")
def titulo_conta_criada():
    print("================================")
    print("|   \033[1;32mCONTA CRIADA COM SUCESSO!\033[0;0m  |")
    print("================================")
def titulo_listar_usuarios():
    print("================================")
    print("|       \033[1;32mLISTAR USUÁRIOS!\033[0;0m       |")
    print("================================")
def titulo_usuarios_listados():
    print("================================")
    print("|       \033[1;32mUSUÁRIOS LISTADOS!\033[0;0m     |")
    print("================================")
def titulo_editar_usuario_email():
    print("================================")
    print("|         \033[1;32mEDITAR EMAIL\033[0;0m         |")
    print("================================")
def titulo_email_atualizado_sucesso():
    print("==========================================")
    print("|\033[1;32mEMAIL VALIDADO E ATUALIZADO COM SUCESSO!\033[0;0m|")
    print("==========================================")
def titulo_editar_usuario_nome():
    print("================================")
    print("|         \033[1;32mEDITAR NOME\033[0;0m          |")
    print("================================")
def titulo_nome_atulizado_sucesso():
    print("=========================================")
    print("|\033[1;32mNOME VALIDADO E ATUALIZADO COM SUCESSO!\033[0;0m|")
    print("=========================================")
def titulo_editar_usuario_telefone():
    print("================================")
    print("|        \033[1;32mEDITAR TELEFONE\033[0;0m       |")
    print("================================")
def titulo_telefone_atualizado_sucesso():
    print("=============================================")
    print("|\033[1;32mTELEFONE VALIDADO E ATUALIZADO COM SUCESSO!\033[0;0m|")
    print("=============================================")
def titulo_usuario_nao_encontrado():
    print("===================================")
    print("|      \033[1;32mUSUÁRIO NÃO ENCONTRADO!\033[0;0m    |")
    print("===================================")
def titulo_opcao_invalida_exluir_usuario():
    print("===================================")
    print("|          \033[1;32mOPÇÃO INVÁLIDA!\033[0;0m        |")
    print("===================================")
def titulo_nome_encontrado():
    print("===================================")
    print("|   \033[1;32mNOME ENCONTRADO COM SUCESSO!\033[0;0m  |")
    print("===================================")
def titulo_usuario_excluido():
    print("===================================")
    print("|   \033[1;32mUSUÁRIO EXCLUÍDO DO SISTEMA!\033[0;0m  |")
    print("===================================")
def titulo_verificar_usuarios_existente_para_acesso():
    print("============================================================")
    print("| \033[1;31mNENHUM REGISTRO DE USUÁRIO ENCONTRADO NO BANCO DE DADOS.\033[0;0m |")
    print("|       \033[1;31mREALIZE O CADASTRO PARA ACESSAR O SISTEMA.\033[0;0m         |")
    print("============================================================")
#avisos de erro
def erro_id_nao_encontrado():
    print("================================")
    print("|\033[1;32mID NÃO ENCONTRADO.\033[0;0m |")
    print("================================")
def erro_email_nao_encontrado():
    print("================================")
    print("|     \033[1;32mEMAIL NÃO ENCONTRADO.\033[0;0m    |")
    print("================================")
def erro_nome_nao_encontrado():
    print("================================")
    print("|      \033[1;32mNOME NÃO ENCONTRADO.\033[0;0m    |")
    print("================================")
def erro_telefone_nao_encontrado():
    print("================================")
    print("|   \033[1;32mTELEFONE NÃO ENCONTRADO.\033[0;0m   |")
    print("================================")
def erro_opcao_invalida_buscar_usuario():
    print("================================")
    print('|\033[1;32m''   Insira uma opção válida!''\033[0;0m   |')
    print("================================")
def erro_entrada_vazia():
    print("\033[1;31m" + "ERRO: " + "\033[0;37m" + "Entrada vazia!" + "\033[0m")
def erro_opcao_invalida_menu_principal():
    clear_terminal()
    print("================================")
    print('|\033[1;32m''   Insira uma opção válida!''\033[0;0m   |')
    print("================================")
def erro_opcao_invalida_editar_usuario():
    print("================================")
    print('|\033[1;32m''   Insira uma opção válida!''\033[0;0m   |')
    print("================================")