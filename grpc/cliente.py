from time import perf_counter
import numpy as np

import grpc
import epdsid_pb2
import epdsid_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = epdsid_pb2_grpc.TestesStub(channel)

print("ChamadaVazio:", stub.ChamadaVazio(epdsid_pb2.Vazio()))
print("ValorAbsolutoLong:", stub.ValorAbsolutoLong(epdsid_pb2.Long(valor=-336721962620426358)))
print("SomaOitoLong:", stub.SomaOitoLong(epdsid_pb2.OitoLong(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)))
print("InverteString:", stub.InverteString(epdsid_pb2.String(texto="olá muundo!")))
print("ChamadaComplexo:", stub.ChamadaComplexo(epdsid_pb2.SolicitacaoComplexo(id=1, nome="Ana", tags=["a", "b", "c"])))

qtTestes = 10
arrTempos = [0] * qtTestes

for i in range(qtTestes):
    argumento = epdsid_pb2.Vazio()
    começo = perf_counter()
    resultado = stub.ChamadaVazio(argumento)
    término = perf_counter()
    arrTempos[i] = término - começo
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
print("ChamadaVazio", "\n", "Tempo Médio: ", média, "\n", "Desvio Padrão: ", desvio)

arrLong = [-6745436184021600282,3213420826097711078,8882416611680843605,933260006861483163,5337830554114930269,-2327841631299803011,3509734561335164606,2376314678599160760,-5868783255512587062,-4665431211468056768]
sum = 0
for i in range(qtTestes):
    argumento = epdsid_pb2.Long(valor=arrLong[i%10])
    começo = perf_counter()
    resultado = stub.ValorAbsolutoLong(argumento)
    término = perf_counter()
    arrTempos[i] = término - começo
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
print("ValorAbsolutoLong", "\n", "Tempo Médio: ", média, "\n", "Desvio Padrão: ", desvio)

sum = 0
for i in range(qtTestes):
    argumento = epdsid_pb2.OitoLong(a=1+i, b=2+i, c=3+i, d=4+i, e=5+i, f=6+i, g=7+i, h=8+i)
    começo = perf_counter()
    resultado = stub.SomaOitoLong(argumento)
    término = perf_counter()
    arrTempos[i] = término - começo
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
print("SomaOitoLong", "\n", "Tempo Médio: ", média, "\n", "Desvio Padrão: ", desvio)

sum = 0
for i in range(qtTestes):
    argumento = epdsid_pb2.String(texto="olá mundo!")
    começo = perf_counter()
    resultado = stub.InverteString(argumento)
    término = perf_counter()
    arrTempos[i] = término - começo
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
print("InverteString", "\n", "Tempo Médio: ", média, "\n", "Desvio Padrão: ", desvio)

sum = 0
for i in range(qtTestes):
    argumento = epdsid_pb2.SolicitacaoComplexo(id=1, nome="Ana", tags=["a", "b", "c"])
    começo = perf_counter()
    resultado = stub.ChamadaComplexo(argumento)
    término = perf_counter()
    arrTempos[i] = término - começo
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
print("ChamadaComplexo", "\n", "Tempo Médio: ", média, "\n", "Desvio Padrão: ", desvio)