count_par = 0
count_impar = 0

for num in range(1, 201):
    numero = int(input(f"Digite o {num}º número: "))
    if numero > 0:
        if num % 2 == 0:
            count_par += 1
        elif num % 2 != 0:
            count_impar += 1
    else:
        print("Digite número inteiro.")

print(f'Existem {count_par} números pares.')
print(f'Existem {count_impar} números ímpares.')