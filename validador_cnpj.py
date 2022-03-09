from re import sub


class ValidadorCnpj:
    def __init__(self, cnpj: str = None):
        self.__cnpj_enviado = None
        self.__cnpj = None
        self.__valido = False
        if cnpj:
            self.validar(cnpj)

    def __str__(self):
        return f'CNPJ {self.__cnpj_enviado} {"valido" if self.__valido else "invalido"}!'

    def validar(self, cnpj: str = None):
        try:
            self.__setar_cnpj_enviado(cnpj)

            self.__formatar_cnpj()

            self.__validar_preenchido()

            self.__validar_total_digitos()

            self.__validar_primeiro_digito()

            self.__validar_segundo_digito()

            self.__valido = True
        except ValueError:
            self.__valido = False

        return self.__valido

    def __setar_cnpj_enviado(self, cnpj):
        if cnpj:
            self.__cnpj_enviado = cnpj

    def __formatar_cnpj(self):
        self.__cnpj = sub(u'[^0-9:]', '', str(self.__cnpj_enviado))

    def __validar_preenchido(self):
        if not self.__cnpj:
            raise ValueError('Informe um CNPJ!')

    def __validar_total_digitos(self):
        if len(self.__cnpj) != 14:
            raise ValueError('CNPJ invalido!')

    def __validar_primeiro_digito(self):
        validar_primeiro = int(self.__cnpj[0]) * 5 + int(self.__cnpj[1]) * 4 + int(self.__cnpj[2]) * 3 \
                           + int(self.__cnpj[3]) * 2 + int(self.__cnpj[4]) * 9 + int(self.__cnpj[5]) * 8 \
                           + int(self.__cnpj[6]) * 7 + int(self.__cnpj[7]) * 6 + int(self.__cnpj[8]) * 5 \
                           + int(self.__cnpj[9]) * 4 + int(self.__cnpj[10]) * 3 + int(self.__cnpj[11]) * 2

        resto = validar_primeiro % 11
        primeiro_digito = 0 if resto < 2 else 11 - resto

        if primeiro_digito != int(self.__cnpj[12]):
            raise ValueError('CNPJ invalido!')

    def __validar_segundo_digito(self):
        validar_segundo = int(self.__cnpj[0]) * 6 + int(self.__cnpj[1]) * 5 + int(self.__cnpj[2]) * 4 \
                          + int(self.__cnpj[3]) * 3 + int(self.__cnpj[4]) * 2 + int(self.__cnpj[5]) * 9 \
                          + int(self.__cnpj[6]) * 8 + int(self.__cnpj[7]) * 7 + int(self.__cnpj[8]) * 6 \
                          + int(self.__cnpj[9]) * 5 + int(self.__cnpj[10]) * 4 + int(self.__cnpj[11]) * 3 \
                          + int(self.__cnpj[12]) * 2

        resto = validar_segundo % 11
        segundo_digito = 0 if resto < 2 else 11 - resto

        if segundo_digito != int(self.__cnpj[13]):
            raise ValueError('CNPJ invalido!')


if __name__ == '__main__':
    cnpj_enviado = input('Digite um CNPJ: ')
    validador = ValidadorCnpj(cnpj_enviado)
    print(validador)
    validador.validar('18.781.203/0001-28')
    print(validador)
