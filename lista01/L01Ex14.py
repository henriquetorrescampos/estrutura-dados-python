percentual_saude = 0.10
percentual_educacao = 0.25
percentual_alimentacao = 0.30
percentual_vestuario = 0.10
percentual_lazer = 0.05
percentual_outros = 0.20

renda_mensal = float(input("Digite a sua renda mensal em R$: "))

valor_aplicado_saude = renda_mensal * percentual_saude
valor_aplicado_educacao = renda_mensal * percentual_educacao
valor_aplicado_alimentacao = renda_mensal * percentual_alimentacao
valor_aplicado_vestuario = renda_mensal * percentual_vestuario
valor_aplicado_lazer = renda_mensal * percentual_lazer
valor_aplicado_outros = renda_mensal * percentual_outros

print(
    f"""
    O valor aplicado em saúde R${valor_aplicado_saude}
    O valor aplicado em educação R${valor_aplicado_educacao}
    O valor aplicado em alimentação R${valor_aplicado_alimentacao}
    O valor aplicado em vestuário R${valor_aplicado_vestuario}
    O valor aplicado em lazer R${valor_aplicado_lazer}
    O valor aplicado em outros R${valor_aplicado_outros}
    """
    )