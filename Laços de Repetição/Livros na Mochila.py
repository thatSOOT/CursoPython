peso = 0
quantidade = 0
while True:
    livro = int(input())
    peso += livro
    if(peso < 18):
        quantidade += 1
    else:
        break
print(quantidade)