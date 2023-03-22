unidade = input()
temperatura = float(input())

if(unidade == "C"):
    if(temperatura >= -273.15):
        print("{:.2f} F".format((temperatura * 9/5) + 32))
        print("{:.2f} K".format((temperatura + 273.15)))
    else:
        print("Valor de temperatura abaixo do minimo")
elif(unidade == "F"):
    if(temperatura >= -459.67):
        print("{:.2f} C".format((temperatura - 32) * 5/9))
        print("{:.2f} K".format((temperatura - 32) * 5/9 + 273.15))
    else:
        print("Valor de temperatura abaixo do minimo")
else:
    if(temperatura >= 0):
        print("{:.2f} C".format(temperatura - 273.15))
        print("{:.2f} F".format((temperatura - 273.15) * 9/5 + 32))
    else:
        print("Valor de temperatura abaixo do minimo")