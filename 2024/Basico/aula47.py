nome = input('Qual seu nome?')
idade = input('Qual sua idade?')

if '' in nome:
    espaco = True

if nome and idade:
    print(f'Seu nome é {nome} ')
    print(f'Seu nome invertido é {nome[::-1]} ')
    print(f'Seu nome contém espaços : {espaco} ') 
    print(f'Seu nome tem {len(nome)} letras') 
    print(f'A primeira letra do seu nome é {nome[0]} ')
    print(f'A ultima letra do seu nome é {nome[-1]} ')
else:
    print('Desculpe, você deixou campos vazios')



    
    
    
