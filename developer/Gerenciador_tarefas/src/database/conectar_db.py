## Esse arquivo é responsável pela conexão do sistema com o banco de dados

import sqlite3

from pathlib import Path

def conectar():
    caminho_banco = (
        Path(__file__).parent.parent
        / "db"
        / "gerencia_tarefas_bancodedados.db"
    )

    return sqlite3.connect(caminho_banco)

conexao = conectar()
print("Banco conectado com sucesso!")
conexao.close()
print("Conexão encerrada.")