respostas = ["APROVADO COM LOUVOR","APROVADO","REPROVADO","REPROVADO POR FALTAS"]
def ClassificaAluno(media,faltas):
    if(faltas <= 10):
        if(media >= 9.5):
            return 0
        elif(media >= 7):
            return 1
        else:
            return 2
    else:
        return 3
inpMedia = float(input())
inpFaltas = int(input())
print(respostas[ClassificaAluno(inpMedia,inpFaltas)])