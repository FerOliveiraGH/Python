def msg_sair_do_jogo():
    print(f"Para sair digite (q!)", end='\n\n')


def sair_do_jogo(comando):
    if comando == 'q!':
        print('Até logo!')
        exit()
