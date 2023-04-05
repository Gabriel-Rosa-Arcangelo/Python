'''Escreva uma função em Python que receba uma lista de números
 e retorne uma nova lista sem números repetidos, mantendo a ordem da primeira ocorrência de cada número.

Exemplo:

Entrada:
[3, 2, 1, 2, 3, 4, 5, 4]

Saída:
[3, 2, 1, 4, 5]'''

def funcao (lista):
    return list(set(lista))

lista = [3, 2, 1, 2, 3, 4, 5, 4]
print(funcao(lista))