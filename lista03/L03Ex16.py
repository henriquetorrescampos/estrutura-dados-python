numero = int(input("Digite um número: "))
count = 1

while count <= numero:
    if count % 15 == 0:
        print(f'O número {count} é múltiplo de 3 e 5.')
    count += 1