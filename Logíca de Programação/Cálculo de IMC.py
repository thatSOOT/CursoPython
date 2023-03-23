peso = float(input())
altura = float(input())
resultado = ["abaixo do peso", "normal", "acima do peso", "com obesidade"]
resultadoN = 1
IMC = peso/(altura*altura)
if(IMC < 18.5):
    resultadoN = 0
elif(IMC >= 18.5 and IMC < 25):
    resultadoN = 1
elif(IMC >= 25 and IMC < 30):
    resultadoN = 2
else:
    resultadoN = 3
print("O seu IMC é de {:.2f}, você está {}".format(IMC, resultado[resultadoN]))