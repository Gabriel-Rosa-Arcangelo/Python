import decimal
num_1 = decimal.Decimal('0.2')
num_2 = decimal.Decimal('0.3')
num_3 = num_1 + num_2
print(num_3)
print(f'{num_3:.2f}')
print(round(num_3, 2))