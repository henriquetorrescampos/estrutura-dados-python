a, b, c = [], [], []

for i in range(3):
    numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
    numB = int(input(f"Digite o {i+1}º número do segundo array: "))
    a.append(numA), b.append(numB)

for i in range(len(a)):
    c.append(a[i] - b[i])

print(c)



