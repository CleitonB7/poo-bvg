class Carro:
    def __init__(self, ano, marca, modelo, cor, placa):
        self.__ano = ano
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__placa = placa  

    # Getters
    def get_ano(self):
        return self.__ano

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_cor(self):
        return self.__cor

    def get_placa(self):
        return self.__placa

    # Setters
    def set_cor(self, nova_cor):
        self.__cor = nova_cor

    def set_placa(self, nova_placa):
        if self.__validar_placa(nova_placa):
            self.__placa = nova_placa
        else:
            raise ValueError("Placa inválida")

    # Método auxiliar privado para validação
    def __validar_placa(self, placa):
        return len(placa) == 7 and placa.isalnum()

    def exibir_detalhes(self):
        print(f"Car: {self.__ano} {self.__marca} {self.__modelo}, Color: {self.__cor}, Plate: {self.__placa}")

    def atualizar_cor(self, nova_cor):
        self.set_cor(nova_cor)
        print(f"Car color updated to: {self.__cor}")

class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf  

    # Getters
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    # Setters
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        if self.__validar_cpf(novo_cpf):
            self.__cpf = novo_cpf
        else:
            raise ValueError("CPF inválido")

    # Método auxiliar privado para validação
    def __validar_cpf(self, cpf):
        return len(cpf.replace(".", "").replace("-", "")) == 11 and cpf.replace(".", "").replace("-", "").isdigit()
    def exibir_informacoes(self):
        print(f"Client: {self.__nome}, CPF: {self.__cpf}")