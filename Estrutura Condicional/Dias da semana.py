dDS = ["Domingo", "Segunda", "Terca", "Quarta", "Quinta", "Sexta", "Sabado"]
x = int(input())
if(x > 7):
    input("valor invalido")
else:
    print(dDS[x-1])