'''Desafio 1:
Escreva uma função que receba uma lista de números como parâmetro e retorne o maior número da lista.'''

def maior_lista(lista):
    maior = lista[0]
    for i in range(1,len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

novo = input('Digite os valores separados por virgula: ')
lista = [int(x) for x in novo.split(',')]
print(maior_lista(lista))
