idade_pessoa1 = int(input("Digite a sua idade: "))

idade_pessoa2 = int(input("Digite a sua idade: "))

idade_pessoa3 = int(input("Digite a sua idade: "))

if idade_pessoa1 > idade_pessoa2:
    maior_idade = idade_pessoa1
else:
    maior_idade = idade_pessoa2

if idade_pessoa1 > idade_pessoa3:
    maior_idade = idade_pessoa1
else:
    maior_idade = idade_pessoa3

print(f"A idade mais velha é {maior_idade} anos.")