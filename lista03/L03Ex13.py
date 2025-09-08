maior_salario = float(input("Digite o 1º salário: "))

for i in range(1, 101):
    salario = float(input(f"Digite o {i}º salário: "))
    if salario > maior_salario:
        maior_salario = salario

print(f"O maior salário é  R${maior_salario}")