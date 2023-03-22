temp = int(input())
sec = input()

if(sec != "S" and sec != "N"):
    print("Erro")
elif(temp >= 37):
    if(sec == "S"):
        print("Exames Especiais")
    else:
        print("Exames Basicos")
elif(temp < 37):
    if(sec == "S"):
        print("Exames Basicos")
    else:
        print("Liberado")