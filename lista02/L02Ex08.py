a = int(input("Digite o primeiro valor: "))

b = int(input("Digite o segundo valor: "))

c = int(input("Digite o terceiro valor: "))

if (a + b > c and a + c > b and b + c > a):
    if a == b == c:
        print("Equilátero")
    elif a == b or b == c or a == c:
        print("Isósceles")
    else:
        print("Escaleno")