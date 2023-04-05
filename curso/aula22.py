nome = input('Nome: ')
if nome:
    print(f'Seu nome é {nome}')
    print(f'invertido é {nome[::-1]}')

    if ' ' in nome:
        print('contém espaços')
    else:
        print('NÃO contém espaços')

    print(f'tem {len(nome)} letras')
    print(f'A primeira letra é {nome[0]}')
    print(f'A ultima é {nome[-1]}')
else:
    print('Nada foi digitado!')


