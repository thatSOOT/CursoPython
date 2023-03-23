frase = input()
quantidade = 0
for i in frase.split(" "):
    if(i != ""):
        quantidade += 1
print(quantidade)