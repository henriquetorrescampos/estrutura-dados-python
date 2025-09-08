# Notas do 1º bimestre
nota1_bimestre1 = float(input("Digite a primeira nota do 1º bimestre: "))

nota2_bimestre1 = float(input("Digite a terceira nota 1º bimestre: "))

media_bimestre1 = (nota1_bimestre1 + nota2_bimestre1) / 2

# Notas do 2º bimestre
nota1_bimestre2 = float(input("Digite a primeira nota 2º bimestre: "))

nota2_bimestre2 = float(input("Digite a segunda nota 2º bimestre: "))

media_bimestre2 = (nota1_bimestre2 + nota2_bimestre2) / 2

media_semestral = ((media_bimestre1 * 4) + (media_bimestre2 * 6)) / 10

print(f"A média semestral é {media_semestral:.1f} pontos")