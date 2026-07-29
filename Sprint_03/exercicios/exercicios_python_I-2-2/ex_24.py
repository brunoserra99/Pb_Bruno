class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)


crescente = Ordenadora([3, 4, 2, 1, 5])

lista_crescente = crescente.ordenacaoCrescente()
print(f"{lista_crescente}")


decrescente = Ordenadora([9, 7, 6, 8])

lista_decrescente = decrescente.ordenacaoDecrescente()
print(f"{lista_decrescente}")