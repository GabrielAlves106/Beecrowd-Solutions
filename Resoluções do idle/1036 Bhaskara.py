a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

def bhaskara(a,b,c):
    delta = (b**2) - 4 *a*c
    if a ==0:
        print('Impossivel calcular')
    elif delta ==0:
        print('Impossivel calcular')
    else:
        x1 = (-b + delta ** (1/2)) / (2*a)
        print(f'R1 = {x1:.5f}')
        x2 = (-b - delta ** (1/2)) / (2*a)
        print(f'R2 = {x2:.5f}')
bhaskara = bhaskara(a,b,c)
