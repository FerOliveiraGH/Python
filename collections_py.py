from collections import Counter


class Objeto:
    def __init__(self, valor):
        self.__valor = valor

    def __str__(self):
        return f'Valor: {self.__valor}'

    @property
    def valor(self):
        return self.__valor

    def __lt__(self, other):
        if not isinstance(other, Objeto):
            raise ValueError('Objetos não podem ser comparados.')

        return self.valor < other.valor


objeto1 = Objeto(560)
objeto2 = Objeto(550)

objetos = [objeto1, objeto2]

for objeto in sorted(objetos, reverse=True):
    print(objeto)

idades = [52, 21, 42, 98, 36, 45, 12]
nomes = ['Fernando', 'Leonardo', 'Thaise', 'Glauco']
print(sorted(idades))
print(sorted(nomes))

tupla = ('Fernando', 33)
print(tupla)

idades2 = [53, 21, 42, 99, 36, 45, 13]
idades.extend(idades2)

conjunto = set(idades)  # ignora duplicados / não tem ordem
print(conjunto)
print(sorted(conjunto))
conjunto2 = {53, 22, 42, 97, 44}

print(conjunto & conjunto2)  # obter apenas duplicados
print(conjunto ^ conjunto2)  # existe apenas em um dos conjuntos

dicionario = {
    'chave': 'valor'
}
print(dicionario['chave'])
print(dicionario.get('chave_inexistente', 'sem valor'))
dicionario['adicionar'] = 'adicionado'
print(dicionario)
del dicionario['chave']
print(dicionario)

for key in dicionario.keys():
    print(key)

for value in dicionario.values():
    print(value)

for key, value in dicionario.items():
    print(key, value)


texto = """
        texto de palavras para obter a porcentagem de aparição das mesmas. em alguns momentos isso pode ser interessante 
        para quebrar alguns tipos de criptografia.
        """


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%".format(caractere, proporcao * 100))


analisa_frequencia_de_letras(texto)
