from unittest.mock import MagicMock
import services.login as login


def test_criar_login(monkeypatch):

    entradas = iter([
        "Stefany",
        "Hagne",
        "shagne1234",
        "senha123"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    cursor_mock = MagicMock()
    conexao_mock = MagicMock()

    conexao_mock.cursor.return_value = cursor_mock

    class ConexaoFake:

        def __enter__(self):
            return conexao_mock

        def __exit__(self, *args):
            pass

    monkeypatch.setattr(
        login,
        "conectar",
        lambda: ConexaoFake()
    )

    monkeypatch.setattr(
        login,
        "tela_inicial",
        lambda *args, **kwargs: None
    )

    login.criar_login()

    cursor_mock.execute.assert_called_once()


def test_entrar(monkeypatch):

    entradas = iter([
        "stefany123",
        "senha123"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    cursor_mock = MagicMock()

    cursor_mock.fetchone.return_value = (
        "U1001",
        "Stefany"
    )

    conexao_mock = MagicMock()
    conexao_mock.cursor.return_value = cursor_mock

    class ConexaoFake:

        def __enter__(self):
            return conexao_mock

        def __exit__(self, *args):
            pass

    monkeypatch.setattr(
        login,
        "conectar",
        lambda: ConexaoFake()
    )

    tela_mock = MagicMock()

    monkeypatch.setattr(
        login,
        "tela_inicial",
        tela_mock
    )

    login.entrar()

    tela_mock.assert_called_once_with(
        "Stefany",
        "U1001"
    )


def test_entrar_usuario_invalido(monkeypatch, capsys):

    entradas = iter([
        "usuario",
        "senha_errada"
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(entradas)
    )

    cursor_mock = MagicMock()
    cursor_mock.fetchone.return_value = None

    conexao_mock = MagicMock()
    conexao_mock.cursor.return_value = cursor_mock

    class ConexaoFake:

        def __enter__(self):
            return conexao_mock

        def __exit__(self, *args):
            pass

    monkeypatch.setattr(
        login,
        "conectar",
        lambda: ConexaoFake()
    )

    login.entrar()

    saida = capsys.readouterr()

    assert "Perfil não encontrado" in saida.out

def test_menu_sair(monkeypatch, capsys):

    monkeypatch.setattr(
        "builtins.input",
        lambda _: "3"
    )

    login.menu()

    saida = capsys.readouterr()

    assert "Encerrando o sistema" in saida.out