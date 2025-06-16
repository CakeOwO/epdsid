from jsonrpclib import ServerProxy

#server = ServerProxy("http://localhost:8000")
server = ServerProxy("http://192.168.15.4:8000")

def ChamadaVazio():
    return server.chamada_vazio()


def ValorAbsolutoLong(valor):
    return server.valor_absoluto_long(valor)


def SomaListaLong(valores):
    return server.soma_lista_long(*valores)


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
