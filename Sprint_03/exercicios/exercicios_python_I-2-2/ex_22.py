class Pessoa:
    def __init__(self, id):
        self.id = id  # Atributo público
        self.__nome = None  # Atributo privado
    
    @property
    def nome(self):
        """Getter para o atributo __nome"""
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        """Setter para o atributo __nome"""
        if not valor:
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor