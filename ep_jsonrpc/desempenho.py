from time import perf_counter
import numpy as np

import cliente as c

import matplotlib.pyplot as plt

qtTestes = 10
arrTempos = [0.0] * qtTestes
médias = []
desvios = []

# Teste ChamadoVazio
for i in range(qtTestes):
    começo = perf_counter()
    c.ChamadaVazio()
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médias.append(dados.mean())
desvios.append(dados.std())
print("ChamadoVazio")
print("Tempo Médio:\t", médias[-1])
print("Desvio Padrão:\t", desvios[-1])

valores_long = [-6745436184021600282, 3213420826097711078, 8882416611680843605, 933260006861483163, 5337830554114930269, -
                2327841631299803011, 3509734561335164606, 2376314678599160760, -5868783255512587062, -4665431211468056768]

# Teste ValorAbsolutoLong
for i in range(qtTestes):
    argumento = valores_long[i % len(valores_long)]
    começo = perf_counter()
    c.ValorAbsolutoLong(argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médias.append(dados.mean())
desvios.append(dados.std())
print("ValorAbsolutoLong")
print("Tempo Médio:\t", médias[-1])
print("Desvio Padrão:\t", desvios[-1])

# Teste SomaListaLong
for i in range(qtTestes):
    argumento = range(i, i+8)
    começo = perf_counter()
    c.SomaListaLong(argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médias.append(dados.mean())
desvios.append(dados.std())
print("SomaListaLong")
print("Tempo Médio:\t", médias[-1])
print("Desvio Padrão:\t", desvios[-1])

texto_base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * 16913
potenciaMax = 20
médiasString = []
desviosString = []

# Teste InverteString
for potencia in range(1, potenciaMax + 1):
    argumento = texto_base[:2**potencia]
    for i in range(qtTestes):
        começo = perf_counter()
        c.InverteString(argumento)
        arrTempos[i] = perf_counter() - começo
    
    dados = np.array(arrTempos)
    médiasString.append(dados.mean())
    desviosString.append(dados.std())
    print("InverteString" + f" (tamanho string {2**potencia})")
    print("Tempo Médio:\t", médiasString[-1])
    print("Desvio Padrão:\t", desviosString[-1])

contatos = [
    {
        "id": 1,
        "nome": "Ana Paula Oliveira",
        "email": "ana.oliveira@gmail.com",
        "telefone": "+55 11 91234-5678",
        "rotulos": ["amiga", "trabalho"],
        "endereco": {
            "nomeendereco": "Rua das Acácias, 120",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "04567-000",
            "pais": "Brasil"
        },
        "favorito": True
    },
    {
        "id": 2,
        "nome": "Carlos Eduardo Silva",
        "email": "carlos.silva@empresa.com.br",
        "telefone": "+55 21 99876-5432",
        "rotulos": ["cliente"],
        "endereco": {
            "nomeendereco": "Av. das Américas, 2000",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "22640-102",
            "pais": "Brasil"
        },
        "favorito": False
    },
    {
        "id": 3,
        "nome": "Fernanda Costa",
        "email": "fernanda.costa@outlook.com",
        "telefone": "+55 31 98765-4321",
        "rotulos": ["família"],
        "endereco": {
            "nomeendereco": "Rua do Sol, 45",
            "cidade": "Belo Horizonte",
            "estado": "MG",
            "cep": "30140-110",
            "pais": "Brasil"
        },
        "favorito": True
    },
    {
        "id": 4,
        "nome": "João Pedro Rocha",
        "email": "joao.rocha@usp.br",
        "telefone": "+55 19 91234-0000",
        "rotulos": ["universidade"],
        "endereco": {
            "nomeendereco": "Rua das Palmeiras, 75",
            "cidade": "Campinas",
            "estado": "SP",
            "cep": "13083-970",
            "pais": "Brasil"
        },
        "favorito": False
    },
    {
        "id": 5,
        "nome": "Mariana Lima",
        "email": "mariana.lima@yahoo.com",
        "telefone": "+55 81 92222-3333",
        "rotulos": ["colega"],
        "endereco": {
            "nomeendereco": "Av. Boa Viagem, 888",
            "cidade": "Recife",
            "estado": "PE",
            "cep": "51020-001",
            "pais": "Brasil"
        },
        "favorito": True
    },
    {
        "id": 6,
        "nome": "Rodrigo Mendes",
        "email": "rodrigo.mendes@techmail.com",
        "telefone": "+55 41 98700-1234",
        "rotulos": ["projeto", "engenharia"],
        "endereco": {
            "nomeendereco": "Rua das Laranjeiras, 234",
            "cidade": "Curitiba",
            "estado": "PR",
            "cep": "80240-000",
            "pais": "Brasil"
        },
        "favorito": False
    },
    {
        "id": 7,
        "nome": "Luana Souza",
        "email": "luana.souza@servicos.gov.br",
        "telefone": "+55 61 99666-7777",
        "rotulos": ["governo"],
        "endereco": {
            "nomeendereco": "Esplanada dos Ministérios, Bloco A",
            "cidade": "Brasília",
            "estado": "DF",
            "cep": "70040-000",
            "pais": "Brasil"
        },
        "favorito": False
    },
    {
        "id": 8,
        "nome": "Felipe Martins",
        "email": "felipe.martins@startup.io",
        "telefone": "+55 51 99999-9999",
        "rotulos": ["startup", "parceiro"],
        "endereco": {
            "nomeendereco": "Rua Independência, 890",
            "cidade": "Porto Alegre",
            "estado": "RS",
            "cep": "90035-071",
            "pais": "Brasil"
        },
        "favorito": True
    },
    {
        "id": 9,
        "nome": "Patrícia Gomes",
        "email": "patricia.gomes@edu.br",
        "telefone": "+55 71 92345-6789",
        "rotulos": ["educação"],
        "endereco": {
            "nomeendereco": "Av. Sete de Setembro, 456",
            "cidade": "Salvador",
            "estado": "BA",
            "cep": "40060-001",
            "pais": "Brasil"
        },
        "favorito": False
    },
    {
        "id": 10,
        "nome": "Bruno Ferreira",
        "email": "bruno.ferreira@design.com",
        "telefone": "+55 98 91111-2222",
        "rotulos": ["design", "freelancer"],
        "endereco": {
            "nomeendereco": "Rua das Artes, 321",
            "cidade": "São Luís",
            "estado": "MA",
            "cep": "65010-000",
            "pais": "Brasil"
        },
        "favorito": False
    }
]

médiasCRUD = []
desviosCRUD = []

# Teste AdicionaContato
for i in range(qtTestes):
    argumento = contatos[i % len(contatos)]
    argumento["id"] = i + 1
    começo = perf_counter()
    c.AdicionaContato(**argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médiasCRUD.append(dados.mean())
desviosCRUD.append(dados.std())
print("AdicionaContato")
print("Tempo Médio:\t", médiasCRUD[-1])
print("Desvio Padrão:\t", desviosCRUD[-1])

# Teste PegaContato
for i in range(qtTestes):
    argumento = i + 1
    começo = perf_counter()
    c.PegaContato(argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médiasCRUD.append(dados.mean())
desviosCRUD.append(dados.std())
print("PegaContato")
print("Tempo Médio:\t", médiasCRUD[-1])
print("Desvio Padrão:\t", desviosCRUD[-1])

# Teste AtualizaContato
for i in range(qtTestes):
    argumento = contatos[i % len(contatos)]
    argumento["id"] = i
    começo = perf_counter()
    c.AtualizaContato(**argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médiasCRUD.append(dados.mean())
desviosCRUD.append(dados.std())
print("AtualizaContato")
print("Tempo Médio:\t", médiasCRUD[-1])
print("Desvio Padrão:\t", desviosCRUD[-1])

# Teste RemoveContato
for i in range(qtTestes):
    argumento = i
    começo = perf_counter()
    c.RemoveContato(argumento)
    arrTempos[i] = perf_counter() - começo

dados = np.array(arrTempos)
médiasCRUD.append(dados.mean())
desviosCRUD.append(dados.std())
print("RemoveContato")
print("Tempo Médio:\t", médiasCRUD[-1])
print("Desvio Padrão:\t", desviosCRUD[-1])

# matplotlib

nomeFunc = ["ChamadaVazio", "ValorAbsolutoLong", "SomaOitoLong"]
médias_ms = [média * 1000 for média in médias]
desvios_ms = [desvio * 1000 for desvio in desvios]

# barras
x = np.arange(len(nomeFunc))
plt.figure(figsize=(8,6),dpi=150)
plt.bar(x, médias_ms, yerr=desvios_ms, capsize=4)
plt.xticks(x, nomeFunc, rotation=45, ha='right')
plt.ylabel("Tempo de Execução (milisegundos)")
plt.title("Desempenho JSON-RPC (média e desvio padrão)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

tamEntradaString = [f"{2**i}" for i in range(1, potenciaMax + 1)]
médiasString_ms = [média * 1000 for média in médiasString]
desviosString_ms = [desvio * 1000 for desvio in desviosString]

# linha
x = np.arange(len(tamEntradaString))
plt.figure(figsize=(8,6),dpi=150)
plt.plot(x, médiasString_ms, marker='o', linestyle='-')
plt.xticks(x, tamEntradaString, rotation=45, ha='right')
plt.xlabel("Tamanho da String (caracteres)")
plt.ylabel("Tempo de Execução (milisegundos)")
plt.title("Desempenho InverteString vs Tamanho da String (JSON-RPC)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.fill_between(x, np.array(médiasString_ms) - np.array(desviosString_ms),
                 np.array(médiasString_ms) + np.array(desviosString_ms), alpha=0.2)
plt.tight_layout()
plt.show()

# barras CRUD
nomeFuncCRUD = ["AdicionaContato", "PegaContato",
                "AtualizaContato", "RemoveContato"]

médiasCRUD_ms = [média * 1000 for média in médiasCRUD]
desviosCRUD_ms = [desvio * 1000 for desvio in desviosCRUD]

# barras
x = np.arange(len(nomeFuncCRUD))
plt.figure(figsize=(8,6),dpi=150)
plt.bar(x, médiasCRUD_ms, yerr=desviosCRUD_ms, capsize=4)
plt.xticks(x, nomeFuncCRUD, rotation=45, ha='right')
plt.ylabel("Tempo de Execução (milisegundos)")
plt.title("Desempenho CRUD JSON-RPC (média e desvio padrão)")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()