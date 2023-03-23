Precos = {1:5.30, 2:6.0, 3:3.20, 4:2.50}
codigo = int(input())
quantidade =int(input())
total = Precos[codigo]*quantidade
if total >= 40:
    total = total*0.85
elif quantidade >= 15:
    total = total*0.85
print("R$ {:.2f}".format(total))