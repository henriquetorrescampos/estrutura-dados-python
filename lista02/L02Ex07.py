salario_vendedor = float(input("Digite seu salário: "))

valor_venda_mes = int(input("Digite o montante total vendido: "))

if valor_venda_mes <= 10_000:
    novo_salario = salario_vendedor * 1.15
elif valor_venda_mes <= 50_000:
    novo_salario = salario_vendedor * 1.20
else:
    novo_salario = salario_vendedor * 1.30

print(f"O novo salário do vendor é de R$ {novo_salario}")