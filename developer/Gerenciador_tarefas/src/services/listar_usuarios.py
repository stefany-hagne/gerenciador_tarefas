from database.conectar_db import conectar


def listar_usuarios():
    with conectar() as conexao:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT codigo, nome, sobrenome, login
            FROM tabelausers
        """)

        usuarios = cursor.fetchall()

        for usuario in usuarios:
            print(usuario)


listar_usuarios()