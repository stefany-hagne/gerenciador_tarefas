from conectar_db import conectar
from datetime import date
from obter_status import obter_status
import random

def criar_tarefas(criador):
    descricao = input("Digite a descrição da tarefa: ")

    print("\n===== STATUS: =====")
    print("1 - Lista de espera")
    print("2 - A começar")
    print("3 - Em andamento")
    print("4 - Revisão")
    print("5 - Finalizado")

    status_id = int(input("Digite o status da tarefa: "))

    status = obter_status(status_id)
    if status is None:
        print("Status inválido. A tarefa será criada com o status 'Lista de espera'.")
        status = "Lista de espera"

    with conectar() as conexao:
        cursor = conexao.cursor()
        t_id = random.randint(1000, 2000)
        codigo = f"T{t_id + 1}"

        try:
            cursor.execute(
                """
                INSERT INTO tabelatarefas (codigo, status, descricao, criador, u_atualizacao, d_criacao)
                VALUES (?, ?, ?, ?, ?,?)
                """,
                (codigo, status, descricao, criador, date.today(), date.today())
            )
            conexao.commit()

            print("\nTarefa criada com sucesso!")

        except Exception as error:
            print("\nErro ao criar a tarefa")
            print(error)
