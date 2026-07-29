import random
import csv
import os

# Gerando os números aleatórios
numeros_aleatorios = [random.randint(1, 100) for _ in range(10000)]

# Verificando se o arquivo já existe e criando-o se necessário
if not os.path.exists('arquivo.csv'):
    with open('arquivo.csv', 'w', newline='') as csvfile:
        # Criando um objeto escritor CSV
        writer = csv.writer(csvfile)

        # Escrevendo cada número em uma nova linha
        for numero in numeros_aleatorios:
            writer.writerow([numero])
else:
    print("O arquivo 'arquivo.csv' já existe. Sobrescrevendo...")
    # O restante do código para sobrescrever o arquivo

print("Números salvos em arquivo.csv")