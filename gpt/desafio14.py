'''Escreva uma função que receba uma lista de dicionários, 
onde cada dicionário representa um aluno e contém as chaves "nome", "idade" e "notas"
(que é uma lista com as notas do aluno). A função deve retornar um dicionário com as seguintes informações:

O número total de alunos
A média das idades dos alunos
A média das notas dos alunos'''

def lista_dict(dicionarios):
    total = len(dicionarios)
    soma_idades = 0
    soma_notas = 0

    for i in dicionarios:
        for n in i["notas"]:
            soma_notas += n
        soma_idades += i["idade"]
    media_idade = soma_idades / total
    media_nota = soma_notas / (total * len(dicionarios[0]["notas"]))

    return  {
        "total alunos" : total,
        "media idades" : media_idade,
        "media notas " : "{:.1f}".format(media_nota)
    }

alunos = [
    {"nome": "João", "idade": 20, "notas": [7.5, 8.0, 6.5]},
    {"nome": "Maria", "idade": 19, "notas": [9.0, 8.5, 7.0]},
    {"nome": "Pedro", "idade": 21, "notas": [6.5, 7.0, 7.5]},
    {"nome": "Ana", "idade": 18, "notas": [8.0, 8.0, 8.5]},
    {"nome": "José", "idade": 23, "notas": [8.9,4.5,2.7]}
]

print(lista_dict(alunos))