preco = float(input("Preço do Produto: "))
quantidade = float(input("Quantidade do Produto: "))
valor = preco*quantidade

if valor > 200:
    opcao = input("DESCONTO [D] OU PARCELAMENTO [P]: ")
    if opcao == "D":
        desconto = valor * 0.05
        print(f'Desconto de R$ {desconto:.2f}')
        total = valor-desconto
        print(f"Total: {total:.2f}")
    else:
        parcelamento = valor/4
        print(f'Parcelas: {parcelamento:.2f}')
        print(f'Total: {valor:.2f}')

    
    
