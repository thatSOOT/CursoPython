forma = input()
if(forma == "Q"):
    lado = float(input())
    print("{:.2f} \n{:.2f}".format(lado*lado,lado*4))
elif(forma == "R"):
    lado1 = float(input())
    lado2 = float(input())
    print("{:.2f} \n{:.2f}".format(lado1*lado2,lado1*2+lado2*2))
elif(forma == "C"):
    raio = float(input())
    print("{:.2f} \n{:.2f}".format(3.14*(raio*raio),2*3.14*raio))
else:
    print("Nenhuma figura selecionada")