from time import perf_counter
import numpy as np

import cliente as c

import matplotlib.pyplot as plt


def teste_desempenho(funcao, *argumento):
    começo = perf_counter()
    resultado = funcao(*argumento)
    término = perf_counter()
    return término - começo


qtTestes = 10
arrTempos = [0] * qtTestes
médias = []
desvios = []

func = c.ChamadaVazio
for i in range(qtTestes):
    arrTempos[i] = teste_desempenho(func)
dados = np.array(arrTempos)
média = dados.mean()
desvio = dados.std()
print(func.__name__)
print("Tempo Médio:\t", média)
print("Desvio Padrão:\t", desvio)
médias.append(média)
desvios.append(desvio)

argumento = [-6745436184021600282, 3213420826097711078, 8882416611680843605, 933260006861483163, 5337830554114930269, -
             2327841631299803011, 3509734561335164606, 2376314678599160760, -5868783255512587062, -4665431211468056768]
func = c.ValorAbsolutoLong
for i in range(qtTestes):
    arrTempos[i] = teste_desempenho(func, argumento[i % len(argumento)])
dados = np.array(arrTempos)
média = dados.mean()
desvio = dados.std()
print(func.__name__)
print("Tempo Médio:\t", média)
print("Desvio Padrão:\t", desvio)
médias.append(média)
desvios.append(desvio)

func = c.SomaOitoLong
for i in range(qtTestes):
    argumento = range(i, i+8)
    arrTempos[i] = teste_desempenho(func, *argumento)
dados = np.array(arrTempos)
média = dados.mean()
desvio = dados.std()
print(func.__name__)
print("Tempo Médio:\t", média)
print("Desvio Padrão:\t", desvio)
médias.append(média)
desvios.append(desvio)

func = c.InverteString
texto_base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * 17
for potencia in range(1, 11):
    argumento = texto_base[:2**potencia]
    for i in range(qtTestes):
        arrTempos[i] = teste_desempenho(func, argumento)
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
    print(func.__name__ + f" (tamanho string {2**potencia})")
    print("Tempo Médio:\t", média)
    print("Desvio Padrão:\t", desvio)
    médias.append(média)
    desvios.append(desvio)

func = c.ChamadaComplexo
argumento = (1, "Ana", ["a", "b", "c"])
for i in range(qtTestes):
    arrTempos[i] = teste_desempenho(func, *argumento)
dados = np.array(arrTempos)
média = dados.mean()
desvio = dados.std()
print(func.__name__)
print("Tempo Médio:\t", média)
print("Desvio Padrão:\t", desvio)
médias.append(média)
desvios.append(desvio)

# matplotlib
functions = [
    "ChamadaVazio",
    "ValorAbsolutoLong",
    "SomaOitoLong",
    "InvStr 2", "InvStr 4", "InvStr 8", "InvStr 16", "InvStr 32",
    "InvStr 64", "InvStr 128", "InvStr 256", "InvStr 512", "InvStr 1024",
    "ChamadaComplexo"
]

# Plot
plt.figure(figsize=(12, 6))
x = np.arange(len(functions))

plt.bar(x, médias, yerr=desvios, capsize=4, color='skyblue')
plt.xticks(x, functions, rotation=45, ha='right')
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Desempenho gRPC (média e desvio padrão)")
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
