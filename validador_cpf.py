from collections import Counter
from re import sub


class ValidadorCpf:
    def __init__(self, cpf: str = None):
        self.__cpf_enviado = None
        self.__cpf = None
        self.__valido = False
        if cpf:
            self.validar(cpf)

    def __str__(self):
        return f'CPF {self.__cpf_enviado} {"valido" if self.__valido else "invalido"}!'

    def validar(self, cpf: str = None) -> bool:
        try:
            self.__setar_cpf_enviado(cpf)

            self.__formatar_cpf()

            self.__validar_enviado()

            self.__validar_total_digitos()

            self.__validar_total_digitos_iguais()

            self.__validar_primeiro_digito()

            self.__validar_segundo_digito()

            self.__valido = True
        except ValueError:
            self.__valido = False

        return self.__valido

    def __setar_cpf_enviado(self, cpf):
        if cpf:
            self.__cpf_enviado = cpf

    def __formatar_cpf(self):
        self.__cpf = sub(u'[^0-9:]', '', str(self.__cpf_enviado))

    def __validar_enviado(self):
        if not self.__cpf:
            raise ValueError('Informe um CPF!')

    def __validar_total_digitos(self):
        if len(self.__cpf) != 11:
            raise ValueError('CPF invalido!')

    def __validar_total_digitos_iguais(self):
        total_digitos = Counter(self.__cpf).values()
        for digito in total_digitos:
            if digito == 11:
                raise ValueError('CPF invalido!')

    def __validar_primeiro_digito(self):
        validar_primeiro = int(self.__cpf[0]) * 10 + int(self.__cpf[1]) * 9 + int(self.__cpf[2]) * 8 \
                           + int(self.__cpf[3]) * 7 + int(self.__cpf[4]) * 6 + int(self.__cpf[5]) * 5 \
                           + int(self.__cpf[6]) * 4 + int(self.__cpf[7]) * 3 + int(self.__cpf[8]) * 2

        primeiro_digito = (validar_primeiro * 10) % 11
        primeiro_digito = 0 if primeiro_digito == 10 else primeiro_digito

        if primeiro_digito != int(self.__cpf[9]):
            raise ValueError('CPF invalido!')

    def __validar_segundo_digito(self):
        validar_segundo = int(self.__cpf[0]) * 11 + int(self.__cpf[1]) * 10 + int(self.__cpf[2]) * 9 \
                          + int(self.__cpf[3]) * 8 + int(self.__cpf[4]) * 7 + int(self.__cpf[5]) * 6 \
                          + int(self.__cpf[6]) * 5 + int(self.__cpf[7]) * 4 + int(self.__cpf[8]) * 3 \
                          + int(self.__cpf[9]) * 2

        segundo_digito = (validar_segundo * 10) % 11

        if segundo_digito != int(self.__cpf[10]):
            raise ValueError('CPF invalido!')


if __name__ == '__main__':
    cpf_enviado = input('Digite um CPF: ')
    validador = ValidadorCpf()
    validador.validar(cpf=cpf_enviado)
    print(validador)
    cpf_enviado1 = '698.127.150-88'
    validador.validar(cpf=cpf_enviado1)
    print(validador)
