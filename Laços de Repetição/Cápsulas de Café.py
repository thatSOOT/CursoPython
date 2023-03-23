capsulas = 0
for i in range(7):
    caixa = int(input())
    tamamho = input()
    if(tamamho == "p" or tamamho == "P"):
        capsulas += caixa*10
    elif(tamamho == "g" or tamamho == "G"):
        capsulas += caixa*16
print("{}\n{}".format(capsulas,int(capsulas*2/7)))