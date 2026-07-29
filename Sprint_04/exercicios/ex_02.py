'''
E02
Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.
É obrigatório aplicar as seguintes funções:
- len
- filter
- lambda
Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
'''
#def conta_vogais(texto:str)-> int:


def conta_vogais(texto):
    vogais_busca = "aeiouAEIOU"
    vogais_filtro = filter(lambda c: c in vogais_busca, texto)
    return len(list(vogais_filtro))

# Teste com um valor fixo
texto = "Contar vogais"
#texto = input("Digite a palavra para contar as vogais: ")

# Resultado
resultado = conta_vogais(texto)
print(f"Quantidade de vogais em '{texto}': {resultado}")