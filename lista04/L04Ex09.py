a = []
count = 0

# for i in range(3):
#     numA = int(input(f"Digite o {i+1}º número do primeiro array: "))
#     a.append(numA)

a = [int(input(f"Digite o {i+1}º número do primeiro array: ")) for i in range(40)]

media_notas = (sum(a) / len(a))

for nota in a:
    if nota > media_notas:
        count += 1

print(f"A media é {media_notas:.2f} e {count} notas estão acima da média")


