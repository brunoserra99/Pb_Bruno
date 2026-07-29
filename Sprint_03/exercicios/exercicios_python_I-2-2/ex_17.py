def dividir_em_tres(lista):
    # Calculando o tamanho de cada parte
    tamanho = len(lista) // 3
    
    # Dividindo a lista em 3 partes
    parte1 = lista[:tamanho]
    parte2 = lista[tamanho:tamanho*2]
    parte3 = lista[tamanho*2:]
    
    return parte1, parte2, parte3

# Testando com a nova lista
lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
parte1, parte2, parte3 = dividir_em_tres(lista_teste)
