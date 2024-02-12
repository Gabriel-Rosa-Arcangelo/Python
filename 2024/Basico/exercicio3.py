nome = input('Digite um nome: ')
novo = ''
count = 0

while count < len(nome):
    letra = f'{nome[count]}*'
    novo += letra
    count += 1

print(f'*{novo}')
