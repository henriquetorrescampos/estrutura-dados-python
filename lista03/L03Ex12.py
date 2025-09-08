menor_salario = float(input(f'Digite o 1º salário: '))

for i in range(2, 101):
    salario = float(input(f'Digite o {i}º salário: '))
    if salario < menor_salario:
        menor_salario = salario

print(f'O menor salário foi: R${menor_salario}')

    