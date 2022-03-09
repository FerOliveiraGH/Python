from procedural.componentes.sair_do_jogo import sair_do_jogo


def dificuldade_jogo():
    easy = 20
    medium = 10
    hard = 5

    print("Escolha a dificuldade do jogo!")
    print(f"(1) Easy - {easy} tentativas")
    print(f"(2) Medium - {medium} tentativas")
    print(f"(3) Hard - {hard} tentativas", end='\n\n')

    dificuldade = input("Qual dificuldade? \n")
    sair_do_jogo(dificuldade)

    if dificuldade == '1':
        return easy
    if dificuldade == '2':
        return medium
    if dificuldade == '3':
        return hard

    print('Dificuldade não encontrada!', end='\n\n')
    return dificuldade_jogo()
