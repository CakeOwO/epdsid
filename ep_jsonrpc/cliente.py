from jsonrpclib import Server

server = Server("http://localhost:8000")


def ChamadaVazio():
    return server.chamada_vazio()


def ValorAbsolutoLong(valor):
    return server.valor_absoluto_long(valor)


def SomaListaLong(*valores):
    return server.soma_lista_longs(*valores)


def InverteString(texto):
    return server.inverte_string(texto)


def AdicionaContato(**contato):
    return server.adiciona_contato(**contato)


def PegaContato(id):
    return server.pega_contato(id)


def AtualizaContato(**contato):
    return server.atualiza_contato(**contato)


def RemoveContato(id):
    return server.remove_contato(id)


def ListaContatos():
    return server.lista_contatos()
