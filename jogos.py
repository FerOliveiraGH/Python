from procedural.jogos import descubra_o_numero, descubra_a_palavra
from procedural.componentes.sair_do_jogo import msg_sair_do_jogo, sair_do_jogo


def escolher_jogo():
    print('-----------------')
    print('Escolha seu Jogo!')
    print('-----------------', end='\n\n')

    msg_sair_do_jogo()

    print('(1) Descubra o Número')
    print('(2) Descubra a Palavra', end='\n\n')

    jogo = input('Qual jogo? \n')

    sair_do_jogo(jogo)

    if jogo == '1':
        return descubra_o_numero.jogar()
    if jogo == '2':
        return descubra_a_palavra.jogar()

    print('Jogo não encontrado!', end='\n\n')
    escolher_jogo()


if __name__ == '__main__':
    escolher_jogo()
