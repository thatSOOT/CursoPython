sucesso = 0
media = 0
for i in range(7):
    entregas = int(input())
    if(entregas >= 100):
        sucesso += 1
    media += entregas
print("{}\n{}".format(sucesso,int(media/7)))