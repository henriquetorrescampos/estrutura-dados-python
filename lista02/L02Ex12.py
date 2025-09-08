idade_pessoa1 = int(input("Digite a sua idade: "))

idade_pessoa2 = int(input("Digite a sua idade: "))

idade_pessoa3 = int(input("Digite a sua idade: "))

media_idade = int((idade_pessoa1 + idade_pessoa2 + idade_pessoa3) / 3)

contador = 0

if idade_pessoa1 > media_idade:
    contador += 1
if idade_pessoa2 > media_idade:
    contador += 1
if idade_pessoa3 > media_idade:
    contador += 1

print(f"A média das idades é {media_idade} e tem {contador} pessoas acima da média.")
