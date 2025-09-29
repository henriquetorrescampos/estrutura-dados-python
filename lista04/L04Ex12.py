a = [input(f"Digite o nome do {i+1} aluno: ") for i in range(3)]

b = [int(input(f"Digite a nota do {i+1} aluno: ")) for i in range(3)]

max_grade = max(b)
index_max_grade = b.index(max_grade)

print(f"O aluno {a[index_max_grade]} tirou a maior nota: {max_grade}")
