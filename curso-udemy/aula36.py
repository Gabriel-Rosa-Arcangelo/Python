frase = input('Escreva algo: ')

qtd_vezes = 0
apareceu = ''
i = 0 

while i < len(frase):

    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
        
    atual = frase.count(letra_atual)

    if qtd_vezes < atual:
        qtd_vezes = atual
        apareceu = letra_atual

    i += 1
print(f'A letra que mais apareceu foi {apareceu}\n')