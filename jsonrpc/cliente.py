from jsonrpclib import Server

server = Server("https://studious-fortnight-7jvwv6qjv473wxvj-8000.app.github.dev/")

print("chamada_vazio:", server.chamada_vazio())
print("valor_absoluto_long:", server.valor_absoluto_long(42))
print("soma_oito_longs:", server.soma_oito_longs(1,2,3,4,5,6,7,8))
print("inverte_string:", server.inverte_string("olá mundo!"))
print("chamada_complexo:", server.chamada_complexo(1, "Alice", ["a", "b", "c"]))
