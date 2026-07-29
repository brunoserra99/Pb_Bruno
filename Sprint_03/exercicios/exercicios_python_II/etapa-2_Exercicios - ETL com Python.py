# Abrindo o arquivo actors.csv
with open("/content/actors.csv", "r", encoding="utf-8") as csv_file:
    linhas = csv_file.readlines()

# Extraindo cabeçalho e linhas de dados
cabecalho = linhas[0].strip().split(",")
dados = [linha.strip().split(",") for linha in linhas[1:]]

# Encontrando o ator com maior número de filmes
maior_num_filmes = 0
ator_com_mais_filmes = ""

for linha in dados:
    nome_ator = linha[0]  # Coluna 'Actor'
    # Convertendo a string para float, removendo espaços em branco e convertendo para int
    num_filmes = int(float(linha[2].strip()))  # Coluna 'Number of movies'

    if num_filmes > maior_num_filmes:
        maior_num_filmes = num_filmes
        ator_com_mais_filmes = nome_ator

# Escrevendo os resultados no arquivo etapa-1.txt
with open("/content/etapa-1.txt", "w", encoding="utf-8") as arquivo_saida:
    arquivo_saida.write(f"Ator com maior número de filmes: {ator_com_mais_filmes}\n")
    arquivo_saida.write(f"Quantidade de filmes: {maior_num_filmes}\n")

print("Os dados foram gravados no arquivo etapa-1.txt com sucesso.")