n = int(input())
contador = 1 


def tabuada(n):
    contador = 1 
    while contador <=10:
        print(n,'X',contador,'=',contador*n)
        contador = contador + 1

tabuada(n)

# Recebe um número natural N entre 0 e 10
#n = int(input("Digite um número natural (0 a 10): "))

# Verifica se N está dentro do intervalo permitido
#if 0 <= n <= 10:
    # Laço de repetição para exibir a tabuada de N
    #contador = 1
    #while contador <= 10:
        #print(f"{n} x {contador} = {n * contador}")
        #contador += 1
