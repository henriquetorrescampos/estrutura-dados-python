a = [int(input(f"Digite o {i+1}º número do primeiro array: ")) for i in range(25)]
b = [int(input(f"Digite o {i+1}º número do primeiro array: ")) for i in range(25)]

zipped_array = list(zip(a, b))
array_interpolado = []

for num in zipped_array:
    for pair in  num:
        array_interpolado.append(pair)

