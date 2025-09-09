primeira_maior_nota = 0
segunda_maior_nota = 0
primeira_matricula = 0
segunda_matricula = 0
primeira_materia = ''
segunda_materia = ''

for i in range(1, 101):
    matricula = int(input("Digite seu número de matrícula: "))
    materia = input("Digite o nome da matéria: ")
    nota = float(input("Digite sua nota: "))

    if nota > primeira_maior_nota:
        segunda_maior_nota = primeira_maior_nota
        segunda_matricula = primeira_matricula
        segunda_materia = primeira_materia

        primeira_maior_nota = nota
        primeira_matricula = matricula
        primeira_materia = materia
    
    elif nota > segunda_maior_nota and nota != primeira_maior_nota:
        segunda_maior_nota = nota
        segunda_matricula = matricula
        segunda_materia = materia

    print(f"""
          O aluno de matrícula {primeira_matricula} da matéria {primeira_materia} obteve a primeira maior nota {primeira_maior_nota}.
          O aluno de matrícula {segunda_matricula} da matéria {segunda_materia} obteve a segunda maior nota {segunda_maior_nota}. 
        """
    )

