'''Escreva uma função que recebe uma lista de números e retorna o segundo menor número da lista.
 Se a lista tiver menos de 2 elementos, a função deve retornar None.'''

def segundo_menor (lista):
    menor = lista[0]
    s_menor = None
    for i in range(1, len(lista)):
        if lista[i] < menor:
            s_menor = menor
            menor = lista[i]
        elif s_menor is None or lista[i] < s_menor:
            s_menor = lista[i]
    
    if len(lista) < 1:
        return None
    else:
        return s_menor

lista = [5, 3, 1, 4, 6]
print(segundo_menor(lista))  # 3