salario_mensal_funcionario = float(input("Digite o seu salário mensal: "))

if salario_mensal_funcionario <= 900:
    print("Isento de imposto de renda.")
elif salario_mensal_funcionario <= 1_800:
    imposto = (salario_mensal_funcionario * 0.15) + 135
    print(f"Imposto a ser pago R$ {imposto:.2f}")
else:
    imposto = (salario_mensal_funcionario * 0.275) + 360
    print(f"Imposto a ser pago R$ {imposto:.2f}")

