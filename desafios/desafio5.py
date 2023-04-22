'''Escreva um programa que leia um número inteiro e diga se ele é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.'''

import math

n1 = int(input('Digite n1: '))
is_prime = True

if n1 < 2:
    is_prime = False
else:
    for i in range(2, int(math.sqrt(n1)) + 1):
        if n1 % i == 0:
            is_prime = False
            break

if is_prime:
    print('Primo')
else:
    print('N primo')
