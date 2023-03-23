numeros = []
for i in range(10):
    numeros.append(int(input()))
x = int(input())
iguais = 0
for i in numeros:
    if(i == x):
        iguais += 1
print(iguais)