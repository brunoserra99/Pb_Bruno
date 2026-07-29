def soma_numeros(string):
    # Divide a string pelos separadores de vírgula e converte os valores para inteiros
    numeros = map(int, string.split(','))
    
    # Retorna a soma dos números
    return sum(numeros)

# String com os números
entrada = "1,3,4,6,10,76"

# Chama a função e imprime apenas a soma
print(soma_numeros(entrada))