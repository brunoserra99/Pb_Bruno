# Lê o arquivo CSV
with open('estudantes.csv', 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Processar cada linha
resultados = []
for linha in linhas:
    dados = linha.strip().split(',') 
    nome = dados[0] 
    try:
        notas = list(map(int, dados[1:])) 
        maiores_notas = sorted(notas, reverse=True)[:3] 
        media = round(sum(maiores_notas) / 3, 2)  
        resultados.append((nome, maiores_notas, media))
    except ValueError:
        print(f"Erro ao processar as notas para o estudante: {nome}")

# Resultados por nome 
resultados_ordenados = sorted(resultados, key=lambda x: x[0])

# Resultados 
for nome, notas, media in resultados_ordenados:
    print(f"Nome: {nome} Notas: {notas} Média: {media}")

'''
# Resultados 
for nome, notas, media in resultados_ordenados[:1]:
    print(f"Nome: {nome} Notas: {notas} Média: {media}")
'''
