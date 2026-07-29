def maiores_que_media(conteudo):
    """
    Recebe um dicionário de produtos e preços, 
    retorna uma lista de produtos com preço acima da média, ordenados pelo preço.
    """
    # Calcula a média dos preços
    media = sum(conteudo.values()) / len(conteudo)
    
    # Filtra os produtos com preço acima da média
    produtos_acima_da_media = [
        (produto, preco) for produto, preco in conteudo.items() if preco > media
    ]
    
    # Ordena os produtos pelo preço em ordem crescente
    produtos_acima_da_media.sort(key=lambda x: x[1])
    
    return produtos_acima_da_media


# Dicionário de produtos e preços
conteudo = {
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}

# Chama a função e exibe o resultado
resultado = maiores_que_media(conteudo)

print("Produtos com preço acima da média:")
for produto, preco in resultado:
    print(f"{produto}: R$ {preco:.2f}")
