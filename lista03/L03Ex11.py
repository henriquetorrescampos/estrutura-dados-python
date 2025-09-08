soma_idade = 0

for i in range(1, 101):
    idade = int(input(f"Digite a {i}º idade: "))
    soma_idade += idade

media_idade = soma_idade / 100

print(f'A média das idades é: {media_idade}.')