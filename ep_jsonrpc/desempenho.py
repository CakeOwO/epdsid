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

func = c.InverteString
texto_base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * 16913
potenciaMax = 20
médiasString = []
desviosString = []
for potencia in range(1, potenciaMax + 1):
    argumento = texto_base[:2**potencia]
    for i in range(qtTestes):
        arrTempos[i] = teste_desempenho(func, argumento)
    dados = np.array(arrTempos)
    média = dados.mean()
    desvio = dados.std()
    print(func.__name__ + f" (tamanho string {2**potencia})")
    print("Tempo Médio:\t", média)
    print("Desvio Padrão:\t", desvio)
    médiasString.append(média)
    desviosString.append(desvio)

# matplotlib
nomeFunc = ["ChamadaVazio", "ValorAbsolutoLong",
            "SomaOitoLong", "ChamadaComplexo"]

tamEntradaString = [f"{2**i}" for i in range(1, potenciaMax + 1)]

médias_ms = [média * 1000 for média in médias]
desvios_ms = [desvio * 1000 for desvio in desvios]

# barras
plt.figure(figsize=(19, 10))
x = np.arange(len(nomeFunc))
plt.bar(x, médias_ms, yerr=desvios_ms, capsize=4, color='skyblue')
plt.xticks(x, nomeFunc, rotation=45, ha='right')
plt.ylabel("Tempo de Execução (milisegundos)")
plt.title("Desempenho gRPC (média e desvio padrão)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()

médiasString_ms = [média * 1000 for média in médiasString]
desviosString_ms = [desvio * 1000 for desvio in desviosString]
sizes = [2**i for i in range(1, potenciaMax + 1)]

# linha
plt.figure(figsize=(19, 10))
x = np.arange(len(tamEntradaString))
plt.plot(x, médiasString_ms, marker='o', linestyle='-')
plt.xticks(x, tamEntradaString, rotation=45, ha='right')
plt.xlabel("Tamanho da String (caracteres)")
plt.ylabel("Tempo de Execução (milisegundos)")
plt.title("Desempenho InverteString vs Tamanho da String")
plt.grid(True, linestyle='--', alpha=0.6)
plt.fill_between(x, np.array(médiasString_ms) - np.array(desviosString_ms),
                 np.array(médiasString_ms) + np.array(desviosString_ms), alpha=0.2)
plt.show()