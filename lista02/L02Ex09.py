nota_aluno = float(input("Digite a sua nota: "))

if nota_aluno <= 4.9:
    print("Menção: MI - Inferior")
elif nota_aluno <= 6.9:
    print("Menção: MM - Médio")
elif nota_aluno <= 8.9:
    print("Menção: MS - Médio Superior")
else: 
    print("Menção: SS - Superior")