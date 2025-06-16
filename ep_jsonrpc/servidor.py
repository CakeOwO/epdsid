from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

porta = 8000
server = SimpleJSONRPCServer(("0.0.0.0", porta))

contatos = {}

def chamada_vazio():
    return None


def valor_absoluto_long(valor):
    return abs(valor)


def soma_lista_long(*valores):
    return sum(valores)


def inverte_string(texto):
    return texto[::-1]


def adiciona_contato(**contato):
    contatos[str(contato["id"])] = contato
    return dict(status=True, msgstatus="Contato adicionado com sucesso!")


def pega_contato(id):
    contato = contatos[str(id)]
    return contato if contato else None


def atualiza_contato(**contato):
    if str(contato["id"]) in contatos:
        contatos[str(contato["id"])] = contato
        return dict(status=True, msgstatus="Contato atualizado com sucesso!")
    else:
        return dict(status=False, msgstatus="Contato não encontrado!")


def remove_contato(id):
    return dict(status=True, msgstatus="Contato removido com sucesso!") if contatos.pop(id, None) else dict(status=False, msgstatus="Contato não encontrado!")


def lista_contatos():
    return contatos


server.register_function(chamada_vazio)
server.register_function(valor_absoluto_long)
server.register_function(soma_lista_long)
server.register_function(inverte_string)
server.register_function(adiciona_contato)
server.register_function(pega_contato)
server.register_function(atualiza_contato)
server.register_function(remove_contato)
server.register_function(lista_contatos)

print("JSON-RPC server listening on port ", porta, "...")
server.serve_forever()