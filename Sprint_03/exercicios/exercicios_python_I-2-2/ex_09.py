primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]

# Usar enumerate para iterar pelos índices e elementos simultaneamente
for i, (primeiro, sobrenome, idade) in enumerate(zip(primeirosNomes, sobreNomes, idades)):
    print(f"{i} - {primeiro} {sobrenome} está com {idade} anos")