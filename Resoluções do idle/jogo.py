from random import choice

L = [1, 2, 3, 4, 5, 6, 7,]

jogo = []

while len(jogo) < 6:
    x = choice(L)
    L.remove(x)
    print(f'jogo atual: {jogo} | Numero: {x}')
    input()
    if x in jogo:
        print('numero invalido')
    else:
        jogo.append(x)
    
print(f'O seu jogo é: {jogo}')
