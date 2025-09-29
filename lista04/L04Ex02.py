a, b = [], []

for i in range(11):
    num = int(input(f"Digite o {i+1}º número: "))
    a.append(num)

for index in range(len(a)):
    if a[index] % 2 == 0:
        b.append(a[index] * 5)
    else:
        b.append(a[index] + 5)

print(b)