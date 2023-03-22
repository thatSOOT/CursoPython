vogais = ["a", "e", "i", "o", "u"]
char = input()
if(char in vogais):
    print("Eh vogal")
elif(len(char) > 1):
    print("1 caractere, por favor!")
else:
    print("Nao eh vogal")
