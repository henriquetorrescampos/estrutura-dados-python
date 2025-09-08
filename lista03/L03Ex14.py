idade = int(input("Digite a 1º idade: "))
count = 1

menor_idade = idade
maior_idade = idade

while count < 100:
    idade_while = int(input(f"Digite a {count+1}º idade: "))
    
    if idade_while > maior_idade:
        maior_idade = idade_while
        
    elif idade_while < menor_idade:
        menor_idade = idade_while

    count += 1

print(f"A diferença entre a maior idade e a menor idade é {maior_idade - menor_idade}")