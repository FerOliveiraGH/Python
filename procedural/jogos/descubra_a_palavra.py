from random import randrange
from procedural.componentes.dificuldade import dificuldade_jogo
from procedural.componentes.sair_do_jogo import msg_sair_do_jogo, sair_do_jogo


def jogar():
    msg_bem_vindo()

    msg_sair_do_jogo()

    tentativa = 1

    dificuldade = dificuldade_jogo()

    palavra_secreta = obter_palavra_secreta()

    letras_certas = criar_letras_certas(palavra_secreta)

    tentar(tentativa, dificuldade, palavra_secreta, letras_certas)


def msg_bem_vindo():
    print("------------------------")
    print("Jogo Descubra a Palavra!")
    print("------------------------", end='\n\n')


def obter_palavra_secreta():
    palavras = open('D:\\Drive\\Alura\\Python\\procedural\\jogos\\palavras.txt', "r")

    lista_palavras = []
    for palavra in palavras:
        lista_palavras.append(palavra.strip('\n'))

    palavras.close()

    palavra_secreta = lista_palavras[randrange(0, len(lista_palavras))]

    print('Palavra:', '_' * len(palavra_secreta))

    return palavra_secreta


def criar_letras_certas(palavra):
    return ['_' for letra in palavra]


def tentar(tentativa, dificuldade, palavra_secreta, letras_certas):
    limite_tentativa(tentativa, dificuldade, palavra_secreta)

    chute = digitar_chute()

    verifica_letras_certas(chute, palavra_secreta, letras_certas)

    acertou(chute, palavra_secreta, letras_certas)

    tentar(tentativa + 1, dificuldade, palavra_secreta, letras_certas)


def limite_tentativa(tentativa, dificuldade, palavra_secreta):
    if tentativa > dificuldade:
        print("Esgotou as tentativas, você perdeu!")
        print(f'A palavra era "{palavra_secreta}"', end='\n\n')
        fim_de_jogo()


def digitar_chute():
    chute = input('Digite uma letra/palavra! \n')
    chute = chute.strip()

    sair_do_jogo(chute)

    return chute


def verifica_letras_certas(chute, palavra_secreta, letras_certas):
    for index, letra in enumerate(palavra_secreta):
        if chute.lower() == letra.lower():
            letras_certas[index] = letra


def acertou(chute, palavra_secreta, letras_certas):
    acertou_o_chute(chute, palavra_secreta)

    acertou_a_palavra(palavra_secreta, letras_certas)


def acertou_o_chute(chute, palavra_secreta):
    if chute.lower() == palavra_secreta.lower():
        print('Palavra:', palavra_secreta)
        print('Você acertou!')
        fim_de_jogo()


def acertou_a_palavra(palavra_secreta, letras_certas):
    palavra = ''.join(letras_certas)
    print('Palavra:', palavra)

    if palavra == palavra_secreta:
        print('Você acertou!')
        fim_de_jogo()


def fim_de_jogo():
    print('Fim de jogo.', end='\n\n')
    jogar()


if __name__ == "__main__":
    jogar()
