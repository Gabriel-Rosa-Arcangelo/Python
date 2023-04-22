'''Crie uma função que recebe uma lista de números 
e retorna a soma dos elementos pares e o produto dos elementos ímpares.'''

import math

def l_num (lista):
    pares = [p for p in lista if p % 2 == 0]
    impares = [i for i in lista if i % 2 != 0]
    return sum(pares), math.prod(impares)

new = input('Digite uma lista: ')
lista = [int(x) for x in new.split(',')]
result = l_num(lista)

print(result)