cpf = '514.272.918.88'
cpf_numerico = [int(c) for c in cpf if c.isdigit()]


soma = 0
for i in range(10):
    soma += cpf_numerico[i] * (11 - i)
    
digito2 = ((soma * 10) % 11)
    
if digito2 > 9:
    digito2 = 0

print(digito2)