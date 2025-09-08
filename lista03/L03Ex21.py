for i in range(1, 101):
    matricula = int(input("Digite seu número de matrícula: "))
    nota = float(input("Digite sua nota: "))
    sexo = int(input("Digite 1 para masculino e 2 para feminino: "))
    soma_alturas += altura


    if menor_altura < altura:
        menor_altura = altura
    elif altura > maior_altura:
        maior_altura = altura

    if sexo == 2:
        altura_mulher += altura

print(
    f"""A maior altura da turma é ${maior_altura} 
        A menor altura da turma é {menor_altura}
        A média da altura das mulheres é {altura_mulher/50}
        A média de altura da turma é {soma_alturas/50}
    """
    )

