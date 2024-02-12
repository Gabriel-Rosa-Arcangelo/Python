cpf = '415.227.908-98'
cpf_numerico = [int(c) for c in cpf if c.isdigit()]

soma = 0
for i in range(9):
    soma += cpf_numerico[i] * (10 - i)

digito1 = 11 - (soma % 11)
digito1 = 0 if digito1 > 9 else digito1

print(digito1)