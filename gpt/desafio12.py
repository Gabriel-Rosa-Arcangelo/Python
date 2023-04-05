'''Cláudio é um fazendeiro que deseja saber se a sua plantação de trigo está saudável ou não. 
Para isso, ele precisa medir a altura de cada uma das plantas
e verificar se há alguma planta que está abaixo do tamanho mínimo para a safra.

A altura mínima para a safra é de 1 metro. Faça uma função chamada verifica_plantacao
que recebe uma lista de números inteiros como parâmetro, representando a altura de cada uma das plantas,
e retorne True se todas as plantas estiverem com a altura mínima exigida ou False caso contrário.'''

def verifica_plantacao(lista):
    return all(x >= 100 for x in lista)

lista = [188, 100, 199, 130, 109]
print(verifica_plantacao(lista))