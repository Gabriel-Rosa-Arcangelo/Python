'''Escreva uma função soma_maior_menor que recebe uma tupla contendo números inteiros como argumento
 e retorna a soma do maior e do menor número.'''

def soma_maior_menor(tupla: tuple) -> int:
    soma = max(tupla) + min(tupla)
    return soma

t = (10, 5, 8, 20, 3)
print(soma_maior_menor(t))
