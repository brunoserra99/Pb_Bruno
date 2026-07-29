'''
E01
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.
Você deverá aplicar as seguintes funções no exercício:
- map
- filter
- sorted
- sum
Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.
'''

# Ler arquivo
with open('arquivo.csv', 'r') as file:
    numeros = file.readlines()

# Converter para inteiros
numeros = list(map(int, numeros))

# Filtro par
numeros_par = list(filter(lambda x: x % 2 == 0, numeros))

# Ordem decrescente
numeros_par_ordenados = sorted(numeros_par, reverse=True)

# Os 5 maiores
maior_par = numeros_par_ordenados[:5]

# Soma dos 5 
soma_maior_par = sum(maior_par)

# Resultados
print(maior_par)
print(soma_maior_par)
