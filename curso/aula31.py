counter = 0

while counter <= 30:
    counter += 1

    if counter == 6:
        print('Não vou mostrar!')
        continue

    print(counter)

    if counter == 20:
        break
