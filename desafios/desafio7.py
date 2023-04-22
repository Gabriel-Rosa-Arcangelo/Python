'''Crie uma função que receba uma lista de números e retorne uma nova lista com apenas
 os números pares da lista original, usando list comprehension.'''

'''def l_numbers(lista):
    n = []
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            n.append(lista[i])
    return n

novo = input('Digite a lista: ')
lista = [int(x) for x in novo.split(',')]
print(l_numbers(lista))'''

#Outra solução

def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

numbers_str = input('Type your numbers: ')
numbers = [int(n) for n in numbers_str.split(',')]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
