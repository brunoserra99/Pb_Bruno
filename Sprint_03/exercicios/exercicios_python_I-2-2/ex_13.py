with open('arquivo_texto.txt', 'r') as arquivo:
    # Imprimir o conteúdo do arquivo sem adicionar uma linha extra
    print(arquivo.read(), end='')