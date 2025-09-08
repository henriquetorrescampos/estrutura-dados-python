poupanca_maria = float(input("Maria, digite o valor da sua econômia guardada: "))

poupanca_jose = float(input("José, digite o valor da sua econômia guardada: "))

valor_total_poupanca = poupanca_maria + poupanca_jose

percentual_maria = (poupanca_maria / valor_total_poupanca) * 100

percentual_jose = (poupanca_jose / valor_total_poupanca) * 100

print(
    f"Nessa poupança em conjunta, a participação da maria é de {percentual_maria}% e a participação do josé é de {percentual_jose}%"
    )