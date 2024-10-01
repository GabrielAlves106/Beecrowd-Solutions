n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

def retorna_media(n1,n2,n3,n4):
    return (2*n1 + 3*n2 + 4*n3 + 1*n4)/4

media = retorna_media(n1,n2,n3,n4)
print(media)

