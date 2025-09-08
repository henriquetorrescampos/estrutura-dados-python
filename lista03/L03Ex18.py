count_maior30 = 0

for i in range(1, 16):
    numero = int(input(f"Digite o {i}º número: "))
    if numero > 30:
        count_maior30 += 1

print(f'Foram digitados {count_maior30} números maiores que 30.')