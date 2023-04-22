try:
    num = int(input('digite um int: '))
    num_pol = num % 2
    if num_pol == 0:
        print('Par')
    else:
        print('Impar')
except:
    print('N digitou int!')
