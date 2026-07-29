# Abrir o arquivo CSV
arquivo_csv = "actors.csv"
resultado_txt = "etapa-4.txt"

# Inicializar dicionário para contagem de aparições dos filmes
contagem_filmes = {}

# Ler o arquivo linha por linha
with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
    # Ignorar a primeira linha (cabeçalho)
    cabecalho = arquivo.readline()
    
    for linha in arquivo:
        # Dividir a linha pelos delimitadores de CSV (vírgula)
        dados = linha.strip().split(",")
        
        # Extrair o nome do filme na coluna "#1 Movies" (índice 4)
        filme = dados[4].strip()
        
        # Incrementar contagem do filme no dicionário
        if filme in contagem_filmes:
            contagem_filmes[filme] += 1
        else:
            contagem_filmes[filme] = 1

# Ordenar os filmes pela quantidade de aparições em ordem decrescente
filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: x[1], reverse=True)

# Escrever o resultado no arquivo "etapa-4.txt"
with open(resultado_txt, "w", encoding="utf-8") as arquivo_resultado:
    for filme, quantidade in filmes_ordenados:
        arquivo_resultado.write(f"{filme}: {quantidade}\n")

print(f"Processamento concluído! Resultado salvo no arquivo '{resultado_txt}'.")
