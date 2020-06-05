from spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Lutokozima')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Lutokozima'), Usuario(nome='Renzo')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
