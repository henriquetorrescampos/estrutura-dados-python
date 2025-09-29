a = []

for i in range(21):
    numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
    a.append(numA)

menor, maior = a[0], a[0]

for i in range(len(a)):
    if a[i] < menor:
        menor = a[i]
    elif a[i] > maior:
        maior = a[i]


