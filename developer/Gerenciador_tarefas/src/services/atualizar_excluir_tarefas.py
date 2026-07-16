## Nesse arquivo contém a funções necessárias para atualizar ou excluir os registros
## O usuário pode alterar os campos RESPONSÁVEL, STATUS e DESCRIÇÃO do registro escolhido

from database.conectar_db import conectar
from datetime import date
from utils.obter_status import obter_status

def excluir_tarefa(codigo_tarefa):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE 
            FROM tabelatarefas
            WHERE codigo = ?
            """,
            (codigo_tarefa,)
        )

        conexao.commit()
        
        if cursor.rowcount > 0:
            print("\nTarefa excluída com sucesso!")
        else:
            print("\nNenhuma tarefa encontrada com esse código.")

def atualizar_status_tarefa(codigo_tarefa):
    print("\n===== STATUS: =====")
    print("1 - Lista de espera")
    print("2 - A começar")
    print("3 - Em andamento")
    print("4 - Revisão")
    print("5 - Finalizado")

    status_id = int(input("Digite o novo status da tarefa: "))

    status = obter_status(status_id)
    if status is None:
        print("Status inválido.")
        return

    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE tabelatarefas
            SET status = ?, u_atualizacao = ?
            WHERE codigo = ?
            """,
            (status, date.today(), codigo_tarefa)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nStatus da tarefa atualizado com sucesso!")
        else:
            print("\nNenhuma tarefa encontrada com esse código.")

def atualizar_descricao_tarefa(codigo_tarefa):
    nova_descricao = input("Digite a nova descrição da tarefa: ")

    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE tabelatarefas
            SET descricao = ?, u_atualizacao = ?
            WHERE codigo = ?
            """,
            (nova_descricao, date.today(), codigo_tarefa)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nDescrição da tarefa atualizado com sucesso!")
        else:
            print("\nNenhuma tarefa encontrada com esse código.")

def atualizar_responsavel_tarefa(codigo_tarefa, novo_responsavel):
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE tabelatarefas
            SET criador = ?, u_atualizacao = ?
            WHERE codigo = ?
            """,
            (novo_responsavel, date.today(), codigo_tarefa)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("\nResponsável da tarefa atualizado com sucesso!")
        else:
            print("\nNenhuma tarefa encontrada com esse código.")

def menu_atualizacoes(codigo_tarefa):
    while True:

        print("\n===== GERENCIADOR DE TAREFAS =====")
        print("1 - Atualizar tarefa")
        print("2 - Excluir tarefa")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("1 - Atualizar status da tarefa")
            print("2 - Atualizar descrição da tarefa")
            print("3 - Atualizar usuário responsável pela tarefa")

            opcao2 = input("Escolha uma opção: ")

            if opcao2 == "1":
                codigo_tarefa = input("\nDigite o código da tarefa (ex.: T1001): ").upper()
                atualizar_status_tarefa(codigo_tarefa)
            elif opcao2 == "2":
                codigo_tarefa = input("\nDigite o código da tarefa (ex.: T1001): ").upper()
                atualizar_descricao_tarefa(codigo_tarefa)
            elif opcao2 == "3":
                codigo_tarefa = input("\nDigite o código da tarefa (ex.: T1001): ").upper()
                novo_responsavel = input("Digite o código do novo responsável (ex.: U1001): ")
                atualizar_responsavel_tarefa(codigo_tarefa, novo_responsavel)
            else:
                print("Opção inválida.")
                continue

        elif opcao == "2":
            codigo_tarefa = input("\nDigite o código da tarefa (ex.: T1001): ").upper()
            excluir_tarefa(codigo_tarefa)

        elif opcao == "3":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")

