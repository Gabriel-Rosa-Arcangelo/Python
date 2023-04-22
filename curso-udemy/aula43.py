frase = 'Essa frase, é um exemplo'
lista = frase.split(',')

for i, frase in enumerate(lista):
    print('-'.join(lista[i].strip().replace(' ', '')))

condicao = 10==11
print('Valor' if condicao else 'Outro valor')