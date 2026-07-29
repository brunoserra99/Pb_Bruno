# Declarando a variável 'numeros' e adicionando números usando range()
numeros = list(range(1, 4))

# Verificando se cada número é par ou ímpar
for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")