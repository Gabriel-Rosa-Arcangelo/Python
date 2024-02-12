frase = ' Olha só que ,  coisa interessante'
lista_palavras = frase.split()

for i, frase in enumerate(lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()

frases_unidas = ' -'.join(lista_palavras)

print(frases_unidas)