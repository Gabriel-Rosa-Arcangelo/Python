lista_b = [4, 5, 6]
lista = ['Carlos', 123, True, 1.8]
lista[3] = 'Maria'

lista.extend(lista_b)

del lista[2]

lista.append('Joao')
lista.pop(1)
lista.insert(1, 'Nome')

print(lista)

