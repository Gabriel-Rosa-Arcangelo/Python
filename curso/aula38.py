for i in range(10):

    if i == 2:
        print('i é 2 pulando...')
        continue

    if i == 8:
        print('Else não será executado!')
        break

    for j in range(1,3):
        print(i, j)
else:
    print('Nunca será executado.')