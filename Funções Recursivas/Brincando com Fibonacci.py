def fibonacci(x):
    pri = 0
    seg = 1
    ter = 1
    if(x == 1):
        return 0
    elif(x == 2):
        return 1
    else:
        for i in range(x-2):
           ter = pri + seg
           pri = seg
           seg = ter
    return ter

posicao = int(input())
print(fibonacci(posicao))