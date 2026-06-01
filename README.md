# User Base

Sistema de gerenciamento de usuários via terminal, desenvolvido em Python com banco de dados SQLite.

---

## Sobre o projeto

O User Base permite cadastrar, buscar, editar, listar e excluir usuários diretamente pelo terminal, com validação de dados e armazenamento local em banco de dados SQLite.

---

## Funcionalidades

- Cadastrar usuário (nome, email, telefone)
- Buscar usuário por ID, email, nome ou telefone
- Listar todos os usuários cadastrados
- Editar email, nome ou telefone de um usuário
- Excluir usuário do sistema

---

## Estrutura do projeto

```
user-base/
│
├── main.py                  # Ponto de entrada do sistema
│
├── auth/
│   └── auth.py              # Funções de cadastro, busca, edição e exclusão
│
├── database/
│   └── db.py                # Conexão e operações com o banco de dados SQLite
│
├── validators/
│   └── validators.py        # Validação das entradas do usuário
│
└── ui/
    └── ui.py                # Menus, títulos e mensagens de erro
```