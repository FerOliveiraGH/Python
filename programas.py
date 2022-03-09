class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    def __str__(self):
        print('Nome:', self.nome, '| Ano:', self.ano, '| Likes:', self.likes)


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} | Ano: {self.ano} | Duracao: {self.duracao} min | Likes {self.likes}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} | Ano: {self.ano} | Temporadas: {self.temporadas} | Likes {self.likes}'


class Playlist:
    def __init__(self, nome, lista_programas):
        self.__nome = nome
        self.__programas = lista_programas

    @property
    def nome(self):
        return self.__nome

    def __len__(self):
        return len(self.__programas)

    def __getitem__(self, item):
        return self.__programas[item]

    def __str__(self):
        return f'Playlist: {self.nome} | Tamanho: {len(self)}'

    def append(self, item):
        self.__programas.append(item)


filme = Filme('bigbug', 2021, 160)
filme2 = Filme('ww1984', 2021, 159)
serie = Serie('smallville', 2021, 3)
serie2 = Serie('mr robot', 2021, 4)

filme.dar_like()
serie2.dar_like()

programas = [filme, serie, filme2]

playlist_fds = Playlist('fds', programas)

playlist_fds.append(serie2)

print(playlist_fds)

for programa in playlist_fds:
    print(programa)
