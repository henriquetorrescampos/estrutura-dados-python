tarifa_agua = float(input("Digite a tarifa da água: "))

tarifa_esgoto = tarifa_agua * 0.8

conta_agua = tarifa_agua + tarifa_esgoto

print(f"A sua conta de água a ser paga é: {conta_agua}")