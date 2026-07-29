# Superclasse Passaro
class Passaro:
    def voar(som_diferente):
        print("Voando...")
    
    def emitir_som(som_diferente):
        pass  # A ser implementado nas subclasses

# Subclasse Pato
class Pato(Passaro):
    def emitir_som(som_diferente):
        print("Pato emitindo som...")
        print("Quack Quack")

# Subclasse Pardal
class Pardal(Passaro):
    def emitir_som(som_diferente):
        print("Pardal emitindo som...")
        print("Piu Piu")

# Testando as classes
pato = Pato()
pardal = Pardal()

print("Pato")
pato.voar()
pato.emitir_som()

print("\nPardal")
pardal.voar()
pardal.emitir_som()
