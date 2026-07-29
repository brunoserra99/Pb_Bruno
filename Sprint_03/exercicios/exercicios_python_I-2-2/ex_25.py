class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"  

# Criando os objetos conforme as entradas fornecidas
aviao1 = Aviao("BOIENG456", 1500, 400)
aviao2 = Aviao("Embraer Praetor 600", 863, 14)
aviao3 = Aviao("Antonov An-2", 258, 12)

# Armazenando os objetos em uma lista
avioes = [aviao1, aviao2, ]

# Iterando sobre a lista e imprimindo as informações de cada avião
for aviao in avioes:
    print(f"O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima} km/h, "
          f"capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.")
