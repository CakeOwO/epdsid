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

func = c.SomaListaLong
for i in range(qtTestes):
    argumento = range(i, i+8)
    arrTempos[i] = teste_desempenho(func, argumento)
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


contatos = [
    {
        "id": 1,
        "name": "Ana Paula Oliveira",
        "email": "ana.oliveira@gmail.com",
        "phone": "+55 11 91234-5678",
        "tags": ["amiga", "trabalho"],
        "favorite": True,
        "address": {
            "street": "Rua das Acácias, 120",
            "city": "São Paulo",
            "state": "SP",
            "zip": "04567-000",
            "country": "Brasil"
        }
    },
    {
        "id": 2,
        "name": "Carlos Eduardo Silva",
        "email": "carlos.silva@empresa.com.br",
        "phone": "+55 21 99876-5432",
        "tags": ["cliente"],
        "favorite": False,
        "address": {
            "street": "Av. das Américas, 2000",
            "city": "Rio de Janeiro",
            "state": "RJ",
            "zip": "22640-102",
            "country": "Brasil"
        }
    },
    {
        "id": 3,
        "name": "Fernanda Costa",
        "email": "fernanda.costa@outlook.com",
        "phone": "+55 31 98765-4321",
        "tags": ["família"],
        "favorite": True,
        "address": {
            "street": "Rua do Sol, 45",
            "city": "Belo Horizonte",
            "state": "MG",
            "zip": "30140-110",
            "country": "Brasil"
        }
    },
    {
        "id": 4,
        "name": "João Pedro Rocha",
        "email": "joao.rocha@usp.br",
        "phone": "+55 19 91234-0000",
        "tags": ["universidade"],
        "favorite": False,
        "address": {
            "street": "Rua das Palmeiras, 75",
            "city": "Campinas",
            "state": "SP",
            "zip": "13083-970",
            "country": "Brasil"
        }
    },
    {
        "id": 5,
        "name": "Mariana Lima",
        "email": "mariana.lima@yahoo.com",
        "phone": "+55 81 92222-3333",
        "tags": ["colega"],
        "favorite": True,
        "address": {
            "street": "Av. Boa Viagem, 888",
            "city": "Recife",
            "state": "PE",
            "zip": "51020-001",
            "country": "Brasil"
        }
    },
    {
        "id": 6,
        "name": "Rodrigo Mendes",
        "email": "rodrigo.mendes@techmail.com",
        "phone": "+55 41 98700-1234",
        "tags": ["projeto", "engenharia"],
        "favorite": False,
        "address": {
            "street": "Rua das Laranjeiras, 234",
            "city": "Curitiba",
            "state": "PR",
            "zip": "80240-000",
            "country": "Brasil"
        }
    },
    {
        "id": 7,
        "name": "Luana Souza",
        "email": "luana.souza@servicos.gov.br",
        "phone": "+55 61 99666-7777",
        "tags": ["governo"],
        "favorite": False,
        "address": {
            "street": "Esplanada dos Ministérios, Bloco A",
            "city": "Brasília",
            "state": "DF",
            "zip": "70040-000",
            "country": "Brasil"
        }
    },
    {
        "id": 8,
        "name": "Felipe Martins",
        "email": "felipe.martins@startup.io",
        "phone": "+55 51 99999-9999",
        "tags": ["startup", "parceiro"],
        "favorite": True,
        "address": {
            "street": "Rua Independência, 890",
            "city": "Porto Alegre",
            "state": "RS",
            "zip": "90035-071",
            "country": "Brasil"
        }
    },
    {
        "id": 9,
        "name": "Patrícia Gomes",
        "email": "patricia.gomes@edu.br",
        "phone": "+55 71 92345-6789",
        "tags": ["educação"],
        "favorite": False,
        "address": {
            "street": "Av. Sete de Setembro, 456",
            "city": "Salvador",
            "state": "BA",
            "zip": "40060-001",
            "country": "Brasil"
        }
    },
    {
        "id": 10,
        "name": "Bruno Ferreira",
        "email": "bruno.ferreira@design.com",
        "phone": "+55 98 91111-2222",
        "tags": ["design", "freelancer"],
        "favorite": False,
        "address": {
            "street": "Rua das Artes, 321",
            "city": "São Luís",
            "state": "MA",
            "zip": "65010-000",
            "country": "Brasil"
        }
    }
]

func = c.AdicionaContato
for i in range(qtTestes):
    argumento = contatos[i].values()
    arrTempos[i] = teste_desempenho(func, argumento)
dados = np.array(arrTempos)
média = dados.mean()
desvio = dados.std()
print(func.__name__)
print("Tempo Médio:\t", média)
print("Desvio Padrão:\t", desvio)
médias.append(média)
desvios.append(desvio)

# matplotlib
nomeFunc = ["ChamadaVazio", "ValorAbsolutoLong", "SomaOitoLong"]

tamEntradaString = [f"{2**i}" for i in range(1, potenciaMax + 1)]

médias_ms = [média * 1000 for média in médias]
desvios_ms = [desvio * 1000 for desvio in desvios]

# barras
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

