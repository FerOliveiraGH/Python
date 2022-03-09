class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.__numero = numero
        self.__titular = cliente.nome
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite + self.saldo

    def set_limite(self, valor):
        self.__limite = valor

    def extrato(self):
        return "Saldo conta {}: R$ {:.2f}".format(self.numero, self.saldo)

    @staticmethod
    def codigo_banco():
        return '001'

    def __pode_sacar(self, valor):
        if self.limite < valor:
            print('Limite indisponível!')
            return False

        return True
