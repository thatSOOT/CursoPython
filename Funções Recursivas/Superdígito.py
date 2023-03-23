def Conotacao(x,y):
    z = ""
    for i in range(y):
        z += x
    return z

def SuperDigito(x):
    ph = x
    adding = 0
    while(len(ph)>1):
        adding = 0
        for i in ph:
            adding += int(i)
        ph = str(adding)
    return ph

numero_conotacao = input()
newNumero = Conotacao(numero_conotacao.split(" ")[0],int(numero_conotacao.split(" ")[1]))
print(SuperDigito(newNumero))