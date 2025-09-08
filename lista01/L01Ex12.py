percentual_comissao_vendedor = 0.15

produto = input("Digite o nome do produto: ")

valor_produto = float(input("Digite o valor do produto em R$: "))

comissao_vendedor = valor_produto * percentual_comissao_vendedor

print(f"O valor da comissão do vendedor é de R$ {comissao_vendedor}.")
