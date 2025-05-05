from cliente import ChamadaVazio, ValorAbsolutoLong, SomaListaLong, InverteString, AdicionaContato, PegaContato, AtualizaContato, RemoveContato, ListaContatos


def run():
    print("ChamadaVazio:", ChamadaVazio())
    print("ValorAbsolutoLong:", ValorAbsolutoLong(-336721962620426358))
    print("SomaListaLong:", SomaListaLong([1, 2, 3, 4, 5, 6, 7, 8]))
    print("InverteString:", InverteString(texto="olá muundo!"))
    print("AdicionaContato:", AdicionaContato(**{
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
    }))
    print("PegaContato:", PegaContato(id=1))
    print("AtualizaContato:", AtualizaContato(**{
        "id": 2,
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
    }))
    print("AtualizaContato:", AtualizaContato(**{
        "id": 1,
        "nome": "Ana Paula Oliveira",
        "email": "ana.oliveira@gmail.com",
        "telefone": "+55 11 91234-5679",
        "rotulos": ["amiga", "trabalho"],
        "endereco": {
            "nomeendereco": "Rua das Acácias, 120",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "04567-000",
            "pais": "Brasil"
        },
        "favorito": True
    }))
    print("ListaContatos:", ListaContatos())
    print("RemoveContato:", RemoveContato(id=1))


if __name__ == '__main__':
    run()
