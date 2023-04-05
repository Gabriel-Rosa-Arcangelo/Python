'''Desafio 2:
Escreva um programa que leia um número inteiro do usuário e verifique se esse número é par ou ímpar.
Se for par, imprima "O número é par". Se for ímpar, imprima "O número é ímpar".'''
while True:
    try:
        n1 = int(input('Digite n1: '))
        break
    except:
        print('n1 tem que ser um número inteiro')

if n1 % 2 == 0: 
    print('Par')
else: 
    print('Impar')