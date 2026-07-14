from conectar_db import conectar
from datetime import date
from criar_tarefa import criar_tarefas
import random

def tela_inicial(nome, codigo_usuario):

    while True:
        print(f"\nBem-vindo(a), {nome}!")
        print(f"Código: {codigo_usuario}")

        print("\n1 - Criar tarefa")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_tarefas(codigo_usuario)

        elif opcao == "2":
            break