a = [int(input(f"Digite a {i+1} nota do primeiro array: ")) for i in range(25)]
b = [int(input(f"Digite a {i+1} nota do segundo array: ")) for i in range(25)]

a.sort()
b.sort()

ziped_array = list(zip(a, b))

array_interpolado = [num for pair in ziped_array for num in pair]

array_interpolado.sort()


