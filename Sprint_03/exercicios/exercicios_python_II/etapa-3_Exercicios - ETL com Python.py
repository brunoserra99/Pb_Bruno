# Lê o arquivo actors.csv
with open("actors.csv", "r") as file:
    lines = file.readlines()

# Ignorar o cabeçalho
header = lines[0]
data = lines[1:]

# Variáveis para armazenar o ator com maior média
top_actor = ""
highest_average = 0

# Itera pelas linhas para encontrar o ator com maior Average per Movie
for line in data:
    columns = line.strip().split(",")  # Divide os campos por vírgula
    actor = columns[0]
    average_per_movie = float(columns[3])  # Average per Movie está na quarta coluna (índice 3)
    
    # Atualiza o maior valor encontrado
    if average_per_movie > highest_average:
        highest_average = average_per_movie
        top_actor = actor

# Escreve o resultado no arquivo etapa-3.txt
with open("etapa-3.txt", "w") as output_file:
    output_file.write(f"Ator com a maior média de receita por filme:\n")
    output_file.write(f"Nome: {top_actor}\n")
    output_file.write(f"Média por filme: ${highest_average} milhões\n")

# Indica que a operação foi concluída
print("Operação finalizada! Resultado salvo no arquivo 'etapa-3.txt'.")
