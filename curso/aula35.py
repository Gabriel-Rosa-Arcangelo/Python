string = 'string'
i = 0

while i < len(string):
    letra = string[i]

    if letra == 'n':
        break

    print(letra)
    i += 1
else:
    print('fim do else')
print('Fim')