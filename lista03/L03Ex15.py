primeiro_intervalo = int(input("Digite o primeiro intervalo: "))

segundo_intervalo = int(input("Digite o segundo intervalo: "))

# primeiro valor menor que o segundo valor

soma_numeros = 0

for i in range(primeiro_intervalo, segundo_intervalo + 1):
    if i % 2 == 0:
        soma_numeros += i
        print(f'Número par {i}')

print(f'A soma dos números é: {soma_numeros}')
