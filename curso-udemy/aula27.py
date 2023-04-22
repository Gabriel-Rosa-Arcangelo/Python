try:
    hora = str(input('Qual a hora? (00-23)H:M(00-59): ')).replace(' ', '')
    numH = int(hora[:2])
    numM = int(hora[3:5])
    Mmenor = numM < 60 and numM > -1
    Hmenor = numH <= 23 and numH > -1

    if numH and numM and ':' in hora and Mmenor and Hmenor or numH == 00 and Mmenor and Hmenor:
        if numH < 12:
            print(f'Bom dia {hora}\n')
        elif numH >= 12 and numH <= 18:
            print(f'Boa tarde {hora}\n')
        elif numH > 18 and numH <= 23:
            print(f'Boa noite {hora}\n')

    elif not Hmenor and not Mmenor:
        print('Hora e Minuto inválidos\n')

    elif not Hmenor:
        print('Hora inválida\n')
        
    elif not Mmenor:
        print('Minuto inválido\n')  

except:
    print('Formato errado!\n')






