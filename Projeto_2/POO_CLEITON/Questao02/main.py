class Carro:
    def __init__(self, ano, marca, modelo, cor, placa):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
    
    def exibir_detalhes(self):
        print(f"Car: {self.ano} {self.marca} {self.modelo}, Color: {self.cor}, Plate: {self.placa}")
    
    def atualizar_cor(self, nova_cor):
        self.cor = nova_cor
        print(f"Car color updated to: {self.cor}")

class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def exibir_informacoes(self):
        print(f"Client: {self.nome}, CPF: {self.cpf}")

class Seguro:
    def __init__(self, carro, cliente, valor, vigencia):
        self.carro = carro
        self.cliente = cliente
        self.valor = valor
        self.vigencia = vigencia
    
    def calcular_valor(self, base_valor, taxa):
        self.valor = base_valor * (1 + taxa)
        print(f"Calculated insurance value: R${self.valor}")
        return self.valor
    
    def verificar_vigencia(self):
        if self.vigencia == "active":
            print("Insurance is valid")
            return True
        else:
            print("Insurance has expired")
            return False
        
        # testando sistema
if __name__ == "__main__":
    carro = Carro(2020, "Toyota", "Corolla", "Branco", "XYZ-1234")
    cliente = Cliente("João Silva", "123.456.789-00")
    seguro = Seguro(carro, cliente, 0, "active")

    cliente.exibir_informacoes()
    carro.exibir_detalhes()
    seguro.calcular_valor(1500, 0.1)
    seguro.verificar_vigencia()