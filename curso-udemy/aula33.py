index = 0
name = input("What's your name?\n")

while index < len(name):
    new = '*' + name[index]
    index+= 1
    print(new, end='')


