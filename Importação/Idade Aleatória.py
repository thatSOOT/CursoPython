import random

nome = input()
estado = ["é novinho(a) ainda.", "começou sua vida agora!","tem muito o que experênciar ainda", "tá no pé na cova"]
idade = int(random.randrange(1,101))
if(idade <= 17):
    print("{} tem {} de idade, {}".format(nome,idade,estado[0]))
elif(idade > 18 and idade < 30):
    print("{} tem {} de idade, {}".format(nome,idade,estado[1]))
elif(idade >= 30 and idade <= 70):
    print("{} tem {} de idade, {}".format(nome,idade,estado[2]))
else:
    print("{} tem {} de idade, {}".format(nome,idade,estado[3]))