def my_map(lst, f):
    return [f(x) for x in lst]
    
# Função que eleva um número à potência de 2
def quadrado(x):
    return x ** 2

# Lista de entrada
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Testando a função my_map
resultado = my_map(lista, quadrado)

print(resultado)
