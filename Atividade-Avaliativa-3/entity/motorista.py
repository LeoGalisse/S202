from entity.corrida import Corrida

class Motorista:
    def __init__(self, nota: int):
        self.corridas = []
        self.nota = nota

    def adicionar_corrida(self, corrida):
        if isinstance(corrida, Corrida):
            self.corridas.append(corrida)
        else:
            print("Apenas objetos da classe Corrida podem ser adicionados à lista de corridas.")
