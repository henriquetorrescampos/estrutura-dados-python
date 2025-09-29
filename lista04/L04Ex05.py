a, b = [], []

for i in range(2):
    numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
    a.append(numA)

for i in range(len(a)):
    b.append(a[i] / 2)

print(a, b)