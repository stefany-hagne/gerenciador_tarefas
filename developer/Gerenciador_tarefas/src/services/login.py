## Nesse arquivo contém as funções que realizam a criação do usuário e a validação do seu registro no banco antes do acesso

from Gerenciador_tarefas.src.database.conectar_db import conectar
from Gerenciador_tarefas.src.views.tela_inicial import tela_inicial
import random


def criar_login():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    usuario = input("Crie um nome de usuário: ")
    senha = input("Crie uma senha: ")

    with conectar() as conexao:
        cursor = conexao.cursor()
        u_id = random.randint(1000, 2000)
        codigo = f"U{u_id + 1}"

        try:
            cursor.execute(
                """
                INSERT INTO tabelausers (codigo, nome, sobrenome, login, senha)
                VALUES (?, ?, ?, ?, ?)
                """,
                (codigo, nome, sobrenome, usuario, senha)
            )

            print("\nConta criada com sucesso!")
            tela_inicial(nome, codigo_usuario=codigo)

        except Exception as error:
            print("\nErro ao criar a conta.")
            print(error)


def entrar():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT codigo, nome
            FROM tabelausers
            WHERE login = ? AND senha = ?
            """,
            (usuario, senha)
        )

        resultado = cursor.fetchone()

    if resultado:
        codigo_usuario = resultado[0]
        nome = resultado[1]

        tela_inicial(nome, codigo_usuario)

    else:
        print("\nPerfil não encontrado.")

def menu():
    while True:

        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Entrar")
        print("2 - Criar login")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            entrar()

        elif opcao == "2":
            criar_login()

        elif opcao == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


menu()