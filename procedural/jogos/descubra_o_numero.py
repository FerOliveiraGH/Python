from random import randint
from procedural.componentes.dificuldade import dificuldade_jogo
from procedural.componentes.sair_do_jogo import msg_sair_do_jogo, sair_do_jogo


def jogar():
    tentativa = 1
    numero_secreto = randint(1, 100)
    pontos = 1000

    msg_bem_vindo()

    msg_sair_do_jogo()

    dificuldade = dificuldade_jogo()

    tentar(tentativa, numero_secreto, dificuldade, pontos)


def msg_bem_vindo():
    print('-----------------------')
    print('Jogo Descubra o Número!')
    print('-----------------------', end='\n\n')


def tentar(tentativa, numero_secreto, dificuldade, pontos):
    limite_tentativa(tentativa, dificuldade)

    chute = digite_seu_numero()

    chute = inteiro(chute)

    range_chute(chute)

    acertou(chute, numero_secreto, pontos)

    errou(chute, numero_secreto, tentativa, dificuldade, pontos)


def limite_tentativa(tentativa, dificuldade):
    if tentativa > dificuldade:
        print(f'Você já tentou {dificuldade} vezes, você perdeu!')
        fim_de_jogo()


def digite_seu_numero():
    chute = input('Digite um número entre 1 e 100: ')

    sair_do_jogo(chute)

    print('Você digitou', chute)
    return chute


def inteiro(chute):
    try:
        return int(chute)
    except ValueError:
        print('É permitido apenas números! você perdeu!')
        fim_de_jogo()


def range_chute(chute):
    if chute < 1 or chute > 100:
        print('Números permitidos são de 1 a 100, você perdeu!')
        fim_de_jogo()


def acertou(chute, numero_secreto, pontos):
    if numero_secreto == chute:
        print(f'Assertou! parabéns você ganhou! Total de pontos: {pontos}')
        fim_de_jogo()


def errou(chute, numero_secreto, tentativa, total, pontos):
    if maior(chute, numero_secreto):
        print('Você errou para cima!', end='\n\n')
    else:
        print('Você errou para baixo!', end='\n\n')

    pontos = pontos - 20

    tentar(tentativa + 1, numero_secreto, total, pontos)


def maior(chute, numero_secreto):
    return chute > numero_secreto


def fim_de_jogo():
    print('Fim de jogo.', end='\n\n')
    jogar()


if __name__ == '__main__':
    jogar()
