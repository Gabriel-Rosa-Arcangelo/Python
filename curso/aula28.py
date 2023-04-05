pri_nm = input('Primeiro nome: ')
t_nm = len(pri_nm)

if pri_nm.find(' ') != -1:
  print("Somente o primeiro nome")

elif t_nm <= 4:
    print('Nome curto!')

elif t_nm >= 5 and t_nm <=6:
    print('Nome normal')

elif t_nm > 6:
    print('Nome grande!')