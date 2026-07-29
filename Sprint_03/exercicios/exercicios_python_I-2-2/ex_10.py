def remover_duplicados(lista):
    nova_lista = []
    itens_vistos = set()  # Conjunto para rastrear elementos já vistos
    for item in lista:
        if item not in itens_vistos:
            nova_lista.append(item)
            itens_vistos = itens_vistos | {item} 
    return nova_lista


lista_teste = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

# Chamada da função e exibição do resultado
nova_lista = remover_duplicados(lista_teste)
print(nova_lista)