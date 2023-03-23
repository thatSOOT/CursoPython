x = input()
nDeCasas = x.split(" ")[0]
tamanhoCerto = x.split(" ")[1]
nDasCasas = input().split(" ")
tamanhoDosPes = input().split(" ")
cinderela = 0
achouCinderala = False
for i in tamanhoDosPes:
    if(i == tamanhoCerto):
        cinderela = nDasCasas[tamanhoDosPes.index(i)]
        achouCinderala = True
if achouCinderala:
    print("Cinderela mora na casa {}!".format(cinderela))
else:
    print("Nenhuma das jovens e a moca do baile.")
