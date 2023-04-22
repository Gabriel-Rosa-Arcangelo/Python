while True:

    try: 
        option = input('+-*/ or (q)uit: ')

        if option.lower().startswith('q'): break
        elif option != '+' and option != '-' and option != '*' and option != '/': 
            print('Invalid option\n')
            continue

        num1 = float(input('num1: '))
        num2 = float(input('num2: '))

        if option == '+': print(f'{num1+num2}\n')
        elif option == '-': print(f'{num1-num2}\n')
        elif option == '*': print(f'{num1*num2}\n')
        elif option == '/': print(f'{num1/num2:.2f}\n')

    except:
        print('Invalid number\n')
        