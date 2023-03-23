frase = input()
letra = input()
quantidade = 0
for i in frase:
    if(i == letra):
        quantidade += 1
print(quantidade)