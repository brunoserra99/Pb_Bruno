class Lampada:
    def __init__(self, ligada=False):
        # A lâmpada começa desligada por padrão, mas pode ser ligada ao criar o objeto
        self.ligada = ligada
    
    def liga(self):
        # Altera o estado da lâmpada para ligada
        self.ligada = True
    
    def desliga(self):
        # Altera o estado da lâmpada para desligada
        self.ligada = False
    
    def esta_ligada(self):
        # Retorna o estado da lâmpada (True se ligada, False se desligada)
        return self.ligada

# Testando a classe
lampada = Lampada()  # A lâmpada começa desligada

# Liga a lâmpada
lampada.liga()
print(f"A lâmpada está ligada? {lampada.esta_ligada()}")  # Esperado: True

# Desliga a lâmpada
lampada.desliga()
print(f"A lâmpada ainda está ligada? {lampada.esta_ligada()}")  # Esperado: False
