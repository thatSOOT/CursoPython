import moeda

moedaV = int(input("Qual o válor da moeda? "))
x = int(input("Quer aumetar o valor da moeda em quanto? "))
moedaV = moeda.aumentar(moedaV,x)
print("O valor da moeda agora é: {}".format(moedaV))

