def funcao_varios_parametros(*args, **kwargs):
    # Imprime os parâmetros não nomeados (args)
    for arg in args:
        print(arg)

    # Imprime os parâmetros nomeados (kwargs)
    for chave, valor in kwargs.items():
        print(valor)

# Exemplo de chamada da função
funcao_varios_parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)