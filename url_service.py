import re


class UrlService:
    def __init__(self, url):
        self.__url = url
        self.__validar_url()

    def __validar_url(self):
        if type(self.__url) != str:
            raise ValueError('Url é invalida.')

        self.__url = self.__url.strip()

        if not self.__url:
            raise ValueError('Url não pode ser vazia.')

        padrao_url = re.compile('(http(s)?://)?(www.)?teste.com/teste')
        match = padrao_url.match(self.__url)
        if not match:
            raise ValueError('Url é invalida.')

    def __str__(self):
        return self.__url


service = UrlService('https://www.teste.com/teste')

print(service)
