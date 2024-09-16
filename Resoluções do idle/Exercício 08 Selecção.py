
a = float(input('a?'))
b = float(input('b?'))
c = float(input('c?'))

if a < b+c and b < a+c and c < a+b:
    elif a==b and b==c:
        print('Triangulo Equilátero')
    elif a==b or a==c or b==c:
        print('Triangulo isósceles')
    else:
        print('Escaleno')
else:
    print('Traingulo Inválido')

    
