'''Escreva uma função em Python que receba uma lista de tuplas, cada tupla contendo 2 strings
representando um nome e um sobrenome, respectivamente. A função deve retornar a lista ordenada
pelo sobrenome das pessoas em ordem alfabética, e caso o sobrenome seja igual, pelo nome em ordem alfabética.'''

def tuplas():
    tuplas = []
    while True:
        nome = input('Nome: ')
        sobrenome = input('Sobrenome: ')
        tuplas.append((nome, sobrenome))
        parar = input('Parar? (y/n) ')
        if parar == 'y':
            break

    return sorted(tuplas, key=lambda t: (t[1].lower(), t[0].lower()))

lista_tuplas = tuplas()
print(lista_tuplas)

