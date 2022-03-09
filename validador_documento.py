from validador_cpf import ValidadorCpf
from validador_cnpj import ValidadorCnpj


class ValidadorDocumento:
    def __init__(self):
        self.__documento = None
        self.__tipo = 'DESCONHECIDO'
        self.__valido = False
        self.__cpf = False
        self.__cnpj = False
        self.__validador_cpf = ValidadorCpf()
        self.__validador_cnpj = ValidadorCnpj()

    def __str__(self):
        return f'Documento {self.__documento} tipo {self.__tipo} é {"valido" if self.__valido else "invalido"}!'

    def validar(self, documento):
        self.__setar_documento(documento)

        self.__cpf = self.__validador_cpf.validar(documento)

        if not self.__cpf:
            self.__cnpj = self.__validador_cnpj.validar(documento)

        if not self.__cpf and not self.__cnpj:
            self.__valido = False

        if self.__cpf or self.__cnpj:
            self.__valido = True

        self.__obter_tipo()

        return self.__valido

    def __setar_documento(self, documento):
        self.__documento = documento
        self.__cpf = False
        self.__cnpj = False
        self.__valido = False

    def __obter_tipo(self):
        if self.__cpf:
            self.__tipo = 'CPF'
        elif self.__cnpj:
            self.__tipo = 'CNPJ'
        else:
            self.__tipo = 'DESCONHECIDO'


if __name__ == '__main__':
    documento_enviado = input('Digite um documento: ')
    validador = ValidadorDocumento()
    validador.validar(documento_enviado)
    print(validador)
    validador.validar('698.127.150-88')
    print(validador)
    validador.validar('18.781.203/0001-28')
    print(validador)
