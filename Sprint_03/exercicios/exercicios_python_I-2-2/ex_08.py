# Lista de palavras
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

# Verificando cada palavra
for palavra in palavras:
    if palavra == palavra[::-1]:  # Verifica se a palavra é igual ao seu inverso
        print(f"A palavra: {palavra} é um palíndromo")
    else:
        print(f"A palavra: {palavra} não é um palíndromo")