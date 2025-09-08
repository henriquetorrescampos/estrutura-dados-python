nota1 = float(input("Digite a primeira nota de 0 a 10: "))

nota2 = float(input("Digite a segunda nota de 0 a 10: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")