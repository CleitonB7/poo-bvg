from abc import ABC, abstractmethod

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

class SeguroVeiculo(ABC):
    def __init__(self, id, cliente, valor_base, carro):
        self.id = id
        self.cliente = cliente 
        self.valor_base = valor_base
        self.carro = carro  
    
    @abstractmethod
    def calcular_valor(self):
        pass
    
    def exibir_detalhes(self):
        print(f"Insurance ID: {self.id}")
        self.cliente.exibir_informacoes()
        self.carro.exibir_detalhes()
        print(f"Base Value: R${self.valor_base:.2f}")

class SeguroCarro(SeguroVeiculo):
    def __init__(self, id, cliente, valor_base, carro, tipo_carro, possui_abs):
        super().__init__(id, cliente, valor_base, carro)
        self.tipo_carro = tipo_carro
        self.possui_abs = possui_abs
    
    def calcular_valor(self):
        valor = self.valor_base
        if self.tipo_carro.lower() == "suv":
            valor *= 1.2 
        elif self.tipo_carro.lower() == "esportivo":
            valor *= 1.5  
        if self.possui_abs:
            valor *= 0.95  
        print(f"Calculated insurance value (Car): R${valor:.2f}")
        return valor

class SeguroMoto(SeguroVeiculo):
    def __init__(self, id, cliente, valor_base, carro, cilindradas, tipo_moto):
        super().__init__(id, cliente, valor_base, carro)
        self.cilindradas = cilindradas
        self.tipo_moto = tipo_moto
    
    def calcular_valor(self):
        valor = self.valor_base
        if self.cilindradas > 500:
            valor *= 1.3  
        if self.tipo_moto.lower() == "esportiva":
            valor *= 1.4  
        print(f"Calculated insurance value (Moto): R${valor:.2f}")
        return valor

# Testando o sistema
if __name__ == "__main__":
    carro = Carro(2020, "Toyota", "Corolla", "Branco", "XYZ-1234")
    moto = Carro(2022, "Honda", "CB500", "Preto", "ABC-5678")  
    cliente = Cliente("João Silva", "123.456.789-00")
    
    seguro_carro = SeguroCarro(1, cliente, 1500.0, carro, "SUV", True)
    seguro_moto = SeguroMoto(2, cliente, 800.0, moto, 600, "Esportiva")
    
    print("Detalhes do Seguro de Carro:")
    seguro_carro.exibir_detalhes()
    seguro_carro.calcular_valor()
    
    print("\nDetalhes do Seguro de Moto:")
    seguro_moto.exibir_detalhes()
    seguro_moto.calcular_valor()