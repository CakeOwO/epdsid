from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(("localhost", 8000))


def chamada_vazio():
    return None


def valor_absoluto_long(valor):
    return abs(valor)


def soma_oito_longs(a, b, c, d, e, f, g, h):
    return a + b + c + d + e + f + g + h


def inverte_string(texto):
    return texto[::-1]


def chamada_complexo(id, name, *tags):
    return {"status": f"Recebido {name} com id {id} e número de tags {len(tags)}"}


server.register_function(chamada_vazio)
server.register_function(valor_absoluto_long)
server.register_function(soma_oito_longs)
server.register_function(inverte_string)
server.register_function(chamada_complexo)

print("JSON-RPC server listening on port 8000...")
server.serve_forever()
