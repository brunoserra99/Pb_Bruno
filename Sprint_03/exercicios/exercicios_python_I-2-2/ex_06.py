# Listas fornecidas
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Conversão das listas em conjuntos e cálculo da interseção
interseccao = set(a) & set(b)

# Conversão do resultado em lista para exibição e impressão
resultado = list(interseccao)
print(resultado)