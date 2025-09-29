a = []

for i in range(3):
    numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
    a.append(numA)

a = [element for element in a[::-1]]