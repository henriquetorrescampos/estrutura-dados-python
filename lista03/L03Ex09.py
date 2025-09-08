soma_numeros = 0

for i in range(1, 11):
    numero = int(input(f"Digite o {i}º número: "))
    if numero > 0:
        soma_numeros += numero
    else:
        print("Digite um número positivo.")

print(f'A soma dos números é: {soma_numeros}')
print(f'A média dos números é: {soma_numeros / 10}')
