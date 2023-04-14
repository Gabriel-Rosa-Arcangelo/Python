arquivo = open("teste.txt", "w")
arquivo.write('Olá, Mundo!')
arquivo.close()

arquivo = open("teste.txt", "r")
conteudo = arquivo.read()
arquivo.close()
print(conteudo)
