peso_livro1 = float(input("Digite o peso do primeiro livro: "))

peso_livro2 = float(input("Digite o peso do segundo livro: "))

peso_livro3 = float(input("Digite o peso do terceiro livro: "))

if peso_livro1 > peso_livro2:
    mais_pesado1 = peso_livro1
else:
    mais_pesado1 = peso_livro2

if peso_livro2 > peso_livro3:
    mais_pesado2 = peso_livro2
else:
    mais_pesado2 = peso_livro2

livro_mais_pesado = mais_pesado1 + mais_pesado2

print(f'A soma dos dois livros mais pesados é {livro_mais_pesado}')
