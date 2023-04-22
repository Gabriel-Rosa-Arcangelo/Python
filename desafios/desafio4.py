'''Escreva um programa que leia um número inteiro e exiba a sua tabuada (de 1 a 10).'''

n1 = int(input('Digite n1: '))
i=0
for i in range(1,11): 
    print(f'{n1}*{i} = {n1*i}')
