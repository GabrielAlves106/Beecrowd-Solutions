dd,mm,aaaa = input().split('/') # splita o input, usando '/' conforme o enunciado
#dd = int(dd)
#mm = int(mm)
#aaaa = int(aaaa)

soma =int(dd+mm+aaaa) # transforma em inteiro

def eh_par(a): # função que verifica se é par
    if soma%2 ==0:
        return 'par'
    else:
        return 'impar'

verificar = eh_par(soma)
print(verificar)
