import pytest
from spam.enviador_de_email import Enviador
from spam.enviador_de_email import EmailInvalido

def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'lutokozima@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'lucy_tk@live.com',
        'Cursos Python Pro',
        'Turma 10 aberta'
    )
    assert destinatario in resultado

@pytest.mark.parametrize(
    'remetente',
    ['', 'lutokozima']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'lucy_tk@live.com',
            'Cursos Python Pro',
            'Turma 10 aberta'
        )

