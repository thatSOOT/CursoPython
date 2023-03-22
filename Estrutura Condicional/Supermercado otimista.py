dia = input()
preco = float(input())
tipo = input()
nome = input()

if((dia == "seg" or dia == "ter" or dia == "qua") and tipo == "ouro"):
    preco /= 2
elif((dia == "qui" or dia == "sex") and (preco >= 10 and preco <= 100)):
    preco /= 3
elif(dia == "sab" and tipo == "prata"):
    preco *= 3
else:
    preco *= 2

print("O preco do produto {} no dia {} eh {:.2f}".format(nome, dia, preco))