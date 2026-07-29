# Abrir o arquivo actors.csv para leitura
with open("actors.csv", "r") as arquivo_csv:
    # Ler todas as linhas do arquivo, ignorando o cabeçalho
    linhas = arquivo_csv.readlines()[1:]  # Ignorar o cabeçalho

# Criar uma lista para armazenar os dados processados
dados_atores = []

# Processar cada linha
for linha in linhas:
    partes = linha.strip().split(",")  # Dividir por vírgulas
    nome_ator = partes[0]  # Nome do ator
    try:
        # Remover possíveis símbolos e converter a receita total bruta para float
        receita_total_bruta = float(partes[1].replace("$", "").replace(",", ""))
    except ValueError:
        receita_total_bruta = 0.0  # Caso a conversão falhe, atribuir 0

    # Adicionar os dados como uma tupla
    dados_atores.append((nome_ator, receita_total_bruta))

# Ordenar a lista pela receita total bruta em ordem decrescente
dados_atores.sort(key=lambda x: x[1], reverse=True)

# Gerar as linhas de saída no formato desejado
linhas_saida = [f"{ator} - {receita:.2f}\n" for ator, receita in dados_atores]

# Escrever o resultado no arquivo etapa-5.txt
with open("etapa-5.txt", "w") as arquivo_saida:
    arquivo_saida.writelines(linhas_saida)

# Exibir mensagem de sucesso
print("O processo foi concluído com sucesso. O arquivo 'etapa-5.txt' comcluido.")
