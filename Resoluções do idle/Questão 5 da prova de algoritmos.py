# Questão 5

trabalho = float(input())
prova_regular = float(input())

media = (trabalho+prova_regular)/2

if media >= 6.0:
    print('aprovado')
elif (trabalho+10)/2 >=0.6:
    print('talvez com a sub')
else:
    print('reprovado')
