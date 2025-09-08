salario_atual_funcionario = float(input("Digite seu salário R$"))

sexo_funcionario = input("Digite seu sexo, M para masculino ou F para feminino: ")

if sexo_funcionario == "M":
    novo_salario = salario_atual_funcionario * 1.10
elif sexo_funcionario == "F":
    novo_salario = salario_atual_funcionario * 1.09

print(f"O novo salario do funcionário é: {novo_salario}")