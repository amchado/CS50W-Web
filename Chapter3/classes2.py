class Flight():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.passageiros = []

    def adicionarPassageiros(self, name):
        if not self.assentosVagos():
            return False  
        self.passageiros.append(name)
        return True

    def assentosVagos(self):
        return self.capacidade - len(self.passageiros)

flight = Flight(3)

pessoas = ["Arthur" , "Gustavo" , "Samira", "Lucas"]

for pessoa in pessoas:
    sucesso = flight.adicionarPassageiros(pessoa)
    if sucesso:
        print(f"{pessoa} foi adicionada ao voô")
    else:
        print(f"Não há assento para {pessoa} sobramdo")