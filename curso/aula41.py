lista = []

while True:
    print('\nSelecione uma opção.')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        item = input('Valor: ')
        lista.append(item)

    elif opcao == 'a':
        indice = input('Indice: ')
        try:
            del(lista[int(indice)])
        except ValueError:
            print('Digite um numero int')
        except IndexError:
            print('Indice não está na lista')
        except Exception:
            print('Erro desconhecido')
        
    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar.')
            continue
        for i, item in enumerate(lista):
            print(i,lista[i])

    else:
        print('Opção Inválida!')