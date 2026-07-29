# Iterar sobre os números de 2 a 100
for num in range(2, 101):  # Começa a partir de 2
    primo = True  # Suponha que o número seja primo
    for i in range(2, int(num**0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        if num % i == 0:
            primo = False  # Se encontrar um divisor, não é primo
            break
    if primo:
        print(num)  # Imprime o número primo em uma nova linha