a = float(input("Digite o primeiro número: "))

b = float(input("Digite o segundo número: "))

c = float(input("Digite o terceiro número: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("Não tem solução real.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"As solução é: {x}")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As soluções são: {x1} e {x2}")