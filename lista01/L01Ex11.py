icms = 0.12

produto = input("Digite o nome do produto vendido: ")
valor_produto = float(input("Digite o valor do protudo em R$: "))

icms_pago = valor_produto * icms

print(f"O ICMS pago no(a) {produto} foi de R$ {icms_pago}.")