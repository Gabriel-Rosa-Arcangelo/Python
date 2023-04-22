import os

plv_sc = 'MACACO'
size = len(plv_sc)
plv_user = '* '*size
plv = ''
num_ten = 0

print(f'A palavra secreta {plv_user} tem {size} letras \n')

while True:

    plv_f = ''

    l_user = input('Proponha uma letra: ').upper()
    num_ten += 1
    
    if len(l_user) > 1 or l_user.isdigit():
        print('Digite apenas uma letra!\n')
        continue

    if l_user in plv_sc:
        plv += l_user
        
        
        for l in plv_sc:
            if l in plv:
                plv_f += l
            else:
                plv_f += ' * '

        print(plv_f,'\n')
    
    if plv_f == plv_sc:
        print('VOCÊ GANHOU!!!')
        print(f'Número de tentativas: {num_ten}')
        break
            



