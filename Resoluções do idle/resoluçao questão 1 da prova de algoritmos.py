#Questão 1

preco = float(input())
quantidade = int(input())

total = preco*quantidade
print(f"{total:.2f}")

desconto_fixo = 0.10*total
desconto_variavel = 0.01 *quantidade * total

total = total - desconto_fixo - desconto_variavel

print(f'{total:.2f}')
