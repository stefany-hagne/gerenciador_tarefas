from conectar_db import conectar
from obter_status import obter_status

def listar_usuarios():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT codigo, nome, sobrenome
            FROM tabelausers
        """)

        usuarios = cursor.fetchall()

        print("\n=== Usuários cadastrados ===")

        for usuario in usuarios:
            print(usuario)


def listar_todas_tarefas():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT 
                tt.codigo, 
                tt.status, 
                tt.descricao, 
                tu.nome 
            from tabelatarefas tt 
            inner join tabelausers tu 
                on tu.codigo = tt.criador
        """)

        tarefas = cursor.fetchall()

        for tarefa in tarefas:
            print(tarefa)

def listar_minhas_tarefas(codigo_usuario):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                tt.codigo,
                tt.status,
                tt.descricao,
                tu.nome
            FROM tabelatarefas tt
            INNER JOIN tabelausers tu
                ON tu.codigo = tt.criador
            WHERE tt.criador = ?
            """,
            (codigo_usuario,)
        )

        tarefas = cursor.fetchall()

        for tarefa in tarefas:
            print(tarefa)

def listar_tarefas_usuario():
    codigo_usuario = input(
        "Digite o código do usuário (ex.: U1001): "
    )

    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                tt.codigo,
                tt.status,
                tt.descricao,
                tu.nome
            FROM tabelatarefas tt
            INNER JOIN tabelausers tu
                ON tu.codigo = tt.criador
            WHERE tu.codigo = ?
            """,
            (codigo_usuario,)
        )

        tarefas = cursor.fetchall()

        if tarefas:
            print("\n=== Tarefas encontradas ===")

            for tarefa in tarefas:
                print(tarefa)

        else:
            print("\nNenhuma tarefa encontrada para esse usuário.")

def listar_tarefas_por_status(status):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                tt.codigo,
                tt.status,
                tt.descricao,
                tu.nome
            FROM tabelatarefas tt
            INNER JOIN tabelausers tu
                ON tu.codigo = tt.criador
            WHERE tt.status = ?
            """,
            (status,)
        )

        tarefas = cursor.fetchall()

        if tarefas:
            print(f"\n=== Tarefas com status '{status}' ===")

            for tarefa in tarefas:
                print(tarefa)

        else:
            print(f"\nNenhuma tarefa encontrada com status '{status}'.")

def tarefas_por_codigo(codigo_tarefa):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            SELECT
                tt.codigo,
                tt.status,
                tt.descricao,
                tu.nome
            FROM tabelatarefas tt
            INNER JOIN tabelausers tu
                ON tu.codigo = tt.criador
            WHERE tt.codigo = ?
            """,
            (codigo_tarefa,)
        )

        tarefas = cursor.fetchall()

        for tarefa in tarefas:
            print(tarefa)

def menu_pesquisa(codigo_usuario):
    while True:
        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Listar todas as tarefas")
        print("2 - Listar tarefas de um usuário específico")
        print("3 - Listar tarefas de um status específico")
        print("4 - Pesquisar tarefa por código")
        print("5 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_todas_tarefas()

        elif opcao == "2":
            print("0 - Listar usuários cadastrados")
            print("1 - Minhas tarefas")
            print("2 - Tarefas de outro usuário")

            opcao2 = input("Escolha uma opção: ")

            if opcao2 == "0":
                listar_usuarios()

            elif opcao2 == "1":
                listar_minhas_tarefas(codigo_usuario)
            
            elif opcao2 == "2":
                listar_tarefas_usuario()

            else:
                print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            print("\n===== STATUS: =====")
            print("1 - Lista de espera")
            print("2 - A começar")
            print("3 - Em andamento")
            print("4 - Revisão")
            print("5 - Finalizado")

            status_id = int(input("Digite o status da tarefa: "))

            status = obter_status(status_id)
            if status is None: 
                print("Status inválido.")
                continue

            listar_tarefas_por_status(status)
        
        elif opcao == "4":
            codigo_tarefa = input("Digite o código da tarefa (ex.: T1001): ")
            tarefas_por_codigo(codigo_tarefa)

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

