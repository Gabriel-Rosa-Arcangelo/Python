lista = []

while True:
    
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar: ')
    
    if opcao == 'i':
        valor = input('Escreva o que você quer inserir: ')
        lista.append(valor)
        
    elif opcao == 'a':
        if lista == []:
            print('Nao tem nada')
            continue
        deleta = input('Escreva o indice que você quer deletar: ')
        try:
            lista.pop(int(deleta))
        except:
            print('Digite o indice correto')
        
    elif opcao == 'l':
        if lista == []:
            print('Nao tem nada')
            continue
        for index, item in enumerate(lista):
            print(index, item)
            
    else:
        print('Selecione uma das 3 letras')
            
        
    
    