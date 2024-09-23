preco = float(input())
qtd  = int(input())
semdesconto = preco*qtd
qtd = float(qtd)
qtd = qtd*0.01

fixoeqtd = 0.10+qtd

descontofixo = semdesconto*fixoeqtd
descontofinal = semdesconto-descontofixo

print(f'{semdesconto:.2f}')
print(f'{descontofinal:.2f}')

