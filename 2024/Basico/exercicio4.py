while True:
    try:
        sair = input('sair? sim ou nao: ')
        n1 = input('n1: ')
        n2 = input('n2: ')

        n1i = float(n1)
        n2i = float(n2)

        operador = input('Escolha um operador (+ - * /) :')

        if operador == '+':
            n3 = n1i + n2i
            print(n3)
        elif operador == '-':
            n3 = n1i - n2i
            print(n3)
        elif operador == '*':
            n3 = n1i * n2i
            print(n3)
        elif operador == '/':
            n3 = n1i / n2i
            print(n3)
        else:
            print('Operador inválido')

    except:
        print('n(1) ou n(2) não são válidos')