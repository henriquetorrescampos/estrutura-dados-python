a, b = [], []

for i in range(5):
    numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
    a.append(numA)

for i in range(len(a) -1, -1, -1):
    b.append(a[i])

print(b)