from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'lutokozima@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantasticos'
    )
