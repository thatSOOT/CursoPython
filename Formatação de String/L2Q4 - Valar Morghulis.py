nDeMortes = int(input())
nomes = []
for i in range(nDeMortes):
    falecido = input()
    nomes.append(falecido)
for i in nomes:
    print("Cara familia {}, sentimos muito pela tragica morte de {}.".format(i.split(" ")[1], i.split(" ")[0]))
    if i.split(" ")[1] == "Lannister":
        print("Os campos agora o ouvirao rugir.")
    elif i.split(" ")[1] == "Stark":
        print("O inverno chega para todos.")
    elif i.split(" ")[1] == "Targaryen":
        print("Voces sao superestimados mesmo.")