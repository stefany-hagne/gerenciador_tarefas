from conectar_db import conectar


def criar_login():
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    usuario = input("Crie um nome de usuário: ")
    senha = input("Crie uma senha: ")

    with conectar() as conexao:
        cursor = conexao.cursor()
        u_id = 1000
        codigo = f"U{u_id + 1}"
        u_id = u_id + 1

        try:
            cursor.execute(
                """
                INSERT INTO tabelausers (codigo, nome, sobrenome, login, senha)
                VALUES (?, ?, ?, ?, ?)
                """,
                (codigo, nome, sobrenome, usuario, senha)
            )

            print("\nConta criada com sucesso!")
            tela_inicial(nome)

        except Exception:
            print("\nJá existe um usuário com esse login.")


def entrar():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT nome
            FROM tabelausers
            WHERE login = ? AND senha = ?
            """,
            (usuario, senha)
        )

        resultado = cursor.fetchone()

    if resultado:
        nome = resultado[0]

        print("\nLogin realizado com sucesso!")
        tela_inicial(nome)

    else:
        print("\nPerfil não encontrado.")


def tela_inicial(nome):
    print("\n========================")
    print(f"Bem-vindo(a), {nome}!")
    print("========================")


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