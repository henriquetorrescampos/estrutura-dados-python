qtd_otimo = 0
qtd_bom = 0
qtd_regular = 0
qtd_ruim = 0
qtd_pessimo = 0
idade = 0
media_idade_ruim = 0
maior_idade_otimo = 0
maior_idade_ruim = 0
maior_idade_pessimo = 0
percentual_pessimo = 0
diferenca_idade_maior_ruim = 0

for i in range(1, 101):
    idade = int(input("Digite sua idade: "))
    avaliacao = input(
        """
        Avalie o filme digitando uma das letras abaixo 
        A - Ótimo 
        B - Bom 
        C - Regular 
        D - Ruim
        E - Péssimo 
        """
    ).upper()

    match avaliacao:
        case 'A':
            qtd_otimo += 1
            if idade > maior_idade_otimo:
                maior_idade_otimo = idade
        case 'B':
            qtd_bom += 1
        case 'C':
            qtd_regular += 1
        case 'D':
            qtd_ruim += 1
            media_idade_ruim += idade
            if idade > maior_idade_ruim:
                maior_idade_ruim = idade
        case 'E':
            qtd_pessimo += 1
            if idade > maior_idade_pessimo:
                maior_idade_pessimo = idade
        case _:
            print("Letra inválida.")
    
diferenca_percentual = ((qtd_bom - qtd_regular) / qtd_bom) * 100
percentual_pessimo = (qtd_pessimo / 100) * 100
diferenca_idade_maior_ruim = maior_idade_otimo - maior_idade_ruim

print(f"""
      A quantidade respostas ótimos foi {qtd_otimo}.
      A diferença percentual entre respostas bom e regular é {diferenca_percentual:.2f}
      A média de idade das pessoas que respondeu ruim é {media_idade_ruim/qtd_ruim}
      O percentual de respostas péssimas é {percentual_pessimo} 
      A maior idade que escolheu péssimo é {maior_idade_pessimo}
      A diferença entre as maiores idades ótimo e ruim é {diferenca_idade_maior_ruim}
"""
    )
