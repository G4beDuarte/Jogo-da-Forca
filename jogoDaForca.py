# Gabriel Duarte 
# RA: 1134890

import os

def limparTela():
    os.system("clear") 

def solicitarJogadores():
    limparTela()
    print("Seja bem-vindo ao jogo da Forca")
    input("Pressione ENTER para continuar....")
    limparTela()
    nomeDesafiante = input("Digite o nome do desafiante: ")
    nomeCompetidor = input("Digite o nome do competidor: ")
    return nomeDesafiante, nomeCompetidor

def pedirPalavraEdicas():
    limparTela()
    palavraChave = input("Qual é a palavra chave: ".lower())
    dica1 = input("Digite a dica 1: ")
    dica2 = input("Digite a dica 2: ")
    dica3 = input("Digite a dica 3: ")
    return palavraChave, dica1, dica2, dica3

def ocultarPalavra(palavra, letrasReveladas):
    palavraOculta = ""
    for letra in palavra:
        if letra in letrasReveladas:
            palavraOculta += letra
        else:
            palavraOculta += "*"
    return palavraOculta

def jogarForca(nomeDesafiante, nomeCompetidor,palavraChave, dica1, dica2, dica3):
    letrasReveladas = []
    erros = 0

    while True:
        limparTela()
        palavraOculta = ocultarPalavra(palavraChave, letrasReveladas)
        print(f"{nomeCompetidor}, a palavra tem {len(palavraOculta)} de letras ")
        print(palavraOculta)
        print("Erros:", (erros))
        opcao = input("Escolha uma opção ((1) Jogar /(2) Pedir dica): ")

        if opcao == "2":
            limparTela()
            print("(1) Dica N°1")
            print("(2) Dica N°2")
            print("(3) Dica N°3")
            opcaoDica = input("Selecione uma das 3 dicas: ")
            if opcaoDica == "1":
                print(f"A dica é: {dica1}")
            elif opcaoDica == "2":
                print(f"A dica é: {dica2}")
            elif opcaoDica == "3":
                print(f"A dica é: {dica3}")
            else:
                print("Dica inválida!")
            letra = input("Digite uma letra: ").lower()
        elif opcao == "1":
            letra = input("Digite uma letra: ").lower()
        else:
            print("Opção inválida: ((1) Jogar / (2) Pedir dica) ")
            continue

        if letra in letrasReveladas:
            print("Você já tentou essa letra. Tente novamente!")

        if letra in palavraChave:
            letrasReveladas.append(letra)
            if set(letrasReveladas) == set(palavraChave):
                limparTela()
                print(f"Parabéns, {nomeCompetidor}! Você acertou a palavra é: {palavraChave}")
                break
        else:
            erros += 1
            if erros == 6:
                limparTela()
                print(f"{nomeCompetidor} você errou 6 vezes e perdeu! O {nomeDesafiante} ganhou!")
                break

    input("Pressione ENTER para continuar!")
    menu()

def menu():
    limparTela()
    print("""                                                                                                                                                                                                    
MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEENNNNNNNN        NNNNNNNNUUUUUUUU     UUUUUUUU
M:::::::M             M:::::::ME::::::::::::::::::::EN:::::::N       N::::::NU::::::U     U::::::U
M::::::::M           M::::::::ME::::::::::::::::::::EN::::::::N      N::::::NU::::::U     U::::::U
M:::::::::M         M:::::::::MEE::::::EEEEEEEEE::::EN:::::::::N     N::::::NUU:::::U     U:::::UU
M::::::::::M       M::::::::::M  E:::::E       EEEEEEN::::::::::N    N::::::N U:::::U     U:::::U 
M:::::::::::M     M:::::::::::M  E:::::E             N:::::::::::N   N::::::N U:::::D     D:::::U 
M:::::::M::::M   M::::M:::::::M  E::::::EEEEEEEEEE   N:::::::N::::N  N::::::N U:::::D     D:::::U 
M::::::M M::::M M::::M M::::::M  E:::::::::::::::E   N::::::N N::::N N::::::N U:::::D     D:::::U 
M::::::M  M::::M::::M  M::::::M  E:::::::::::::::E   N::::::N  N::::N:::::::N U:::::D     D:::::U 
M::::::M   M:::::::M   M::::::M  E::::::EEEEEEEEEE   N::::::N   N:::::::::::N U:::::D     D:::::U 
M::::::M    M:::::M    M::::::M  E:::::E             N::::::N    N::::::::::N U:::::D     D:::::U 
M::::::M     MMMMM     M::::::M  E:::::E       EEEEEEN::::::N     N:::::::::N U::::::U   U::::::U 
M::::::M               M::::::MEE::::::EEEEEEEE:::::EN::::::N      N::::::::N U:::::::UUU:::::::U 
M::::::M               M::::::ME::::::::::::::::::::EN::::::N       N:::::::N  UU:::::::::::::UU  
M::::::M               M::::::ME::::::::::::::::::::EN::::::N        N::::::N    UU:::::::::UU    
MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEENNNNNNNN         NNNNNNN      UUUUUUUUU                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
""")
    print("(1) Jogar Novamente")
    print("(2) Sair do Jogo")
    opcaoMenu = input("Escolha uma opção: ")

    if opcaoMenu == "1":
        nomeCompetidor, nomeDesafiante = solicitarJogadores()
        palavraChave, dica1, dica2, dica3 = pedirPalavraEdicas()
        jogarForca(nomeDesafiante, nomeCompetidor,palavraChave, dica1, dica2, dica3)
    elif opcaoMenu == "2":
        print("Obrigado por jogar!")
    else:
        print("Opção inválida! Escolha entre 1 e 2.")
        menu()

def main():
    nomeCompetidor, nomeDesafiante = solicitarJogadores()
    palavraChave, dica1, dica2, dica3 = pedirPalavraEdicas()
    jogarForca(nomeDesafiante, nomeCompetidor,palavraChave, dica1, dica2, dica3)

if __name__ == "__main__":
    main()