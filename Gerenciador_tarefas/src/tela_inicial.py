from conectar_db import conectar
from datetime import date
from criar_tarefa import criar_tarefas
from listar_tarefas import menu_pesquisa as listar_tarefas
from atualizar_excluir_tarefas import menu_atualizacoes as atualizar_excluir_tarefas
import random

def tela_inicial(nome, codigo_usuario):

    while True:
        print(f"\nBem-vindo(a), {nome}!")
        print(f"Código: {codigo_usuario}")

        print("\n1 - Criar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar/Excluir tarefas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefas(codigo_usuario)

        elif opcao == "2":
            listar_tarefas(codigo_usuario)

        elif opcao == "3":
            atualizar_excluir_tarefas(codigo_usuario)

        elif opcao == "4":
            break