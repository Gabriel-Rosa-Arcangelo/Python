try:
    numero = input('Digite um numero inteiro: ')
    inteiro = int(numero)
    if inteiro % 2 == 0:
        print('Numero é par')
    else:
        print('Numero é ímpar')
except:
    print('O numero não é inteiro')
