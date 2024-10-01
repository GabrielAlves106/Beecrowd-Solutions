p1 = input()
p2 = input()
p3 = input()

def tipo(p1,p2,p3):
    
    if p1 == 'vertebrado':
        if p2 == 'ave':
            if p3 == 'carnivoro':
                return 'aguia'
            else:
                return 'pomba'
        else:
            if p3 == 'onivoro':
                return 'homem'
            else:
                return 'vaca'
    else:
        if p2 == 'inseto':
            if p3 == 'hematofago':
                return 'pulga'
            else:
                return 'lagarta'
        else:
            if p3 == 'hematofago':
                return 'sanguessuga'
            else:
                return 'minhoca'
            
print(tipo(p1,p2,p3))


