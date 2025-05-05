from jsonrpclib import Server

server = Server("http://localhost:8000")


def ChamadaVazio():
    return server.chamada_vazio()


def ValorAbsolutoLong(valor):
    return server.valor_absoluto_long(valor)


def SomaOitoLong(a, b, c, d, e, f, g, h):
    return server.soma_oito_longs(a, b, c, d, e, f, g, h)


def InverteString(texto):
    return server.inverte_string(texto)


def ChamadaComplexo(id, nome, tags):
    return server.chamada_complexo(id, nome, *tags)
