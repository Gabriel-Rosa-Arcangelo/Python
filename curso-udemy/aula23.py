num_str = input('digita pra ser dobrado: ')

try:
    num_flt = float(num_str)
    print(f'O dobro de {num_str} é {num_flt* 2:.2f}')
except:
    print('não é um numero!')
