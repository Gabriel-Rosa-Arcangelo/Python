nome = input('Primeiro nome: ')
tamanho = len(nome)

if tamanho >= 1 and tamanho <= 4:
    print('Nome é curto')
elif tamanho >=5 and tamanho <=6:
    print('Nome é normal')
else:
    print('Nome é grande')
