numero = int(input("Digite um número: "))

if numero > 0:
    count = 1
    soma_numeros = 0
    while count <= numero:
        soma_numeros += count
        count += 1

print(f"A soma dos números de 1 até {numero} é: {soma_numeros}")

