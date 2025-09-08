count_negativos = 0
soma_numero_positivo = 0

for num in range(1, 5):
    numero = int(input(f"Digite o {num}º número: "))
    if numero > 0:
        soma_numero_positivo += numero
    else:
        count_negativos += 1

print(f"A soma dos números positivos é {soma_numero_positivo} e a quantidade dos números negativos é {count_negativos}")
