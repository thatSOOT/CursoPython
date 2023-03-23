cinema = 0
boliche = 0
for i in range(7):
    escolha = input()
    if escolha.lower() == "cinema":
        cinema += 1
    elif escolha.lower() == "boliche":
        boliche += 1
if(cinema >= boliche):
    print("CINEMA")
else:
    print("BOLICHE")