## Esse arquivo é responsável pela conexão do sistema com o banco de dados

import sqlite3

from pathlib import Path
import sqlite3


def conectar():
    caminho_banco = (
        Path(__file__).parent.parent.parent
        / "db"
        / "gerencia_tarefas_bancodedados.db"
    )

    print(caminho_banco)  # teste temporário

    return sqlite3.connect(caminho_banco)