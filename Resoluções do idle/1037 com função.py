def intervalo(n):
    if 0 <= n <= 25:
        return 'Intervalo [0,25]' 
    elif 25 < n <= 50:
        return 'Intervalo (25,50]' 
    elif 50 < n <= 75:
        return 'Intervalo (50,75]'
    elif 75 < n <= 100:
        return 'Intervalo 75,100' 
    else:
        return 'Fora de Intervalo'
n = float(input())
print(intervalo(n))
    
