#import random
#random_list = random.sample(range(500), 50)
#mediana = 0
#media = 0
#valor_minimo = 0
#valor_maximo = 0--/ 

import random

random_list = random.sample(range(500), 50)

# Calculando o valor mínimo e máximo
valor_minimo = min(random_list)
valor_maximo = max(random_list)

# Calculando o valor médio
media = sum(random_list) / len(random_list)

# Calculando a mediana
random_list.sort()  # Ordena a lista
n = len(random_list)
if n % 2 == 1:
    mediana = random_list[n // 2]  # Se a lista tiver um número ímpar de elementos
else:
    mediana = (random_list[n // 2 - 1] + random_list[n // 2]) / 2  # Se a lista tiver um número par de elementos

# Exibindo os resultados
print(f"Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")


