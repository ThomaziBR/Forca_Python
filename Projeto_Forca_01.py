######################################### Forkinha ###########################################
#                         Projeto 1: Construção do Jogo da Forca                             #
#                   By Bruna Kuntz, Mariana Sampaio e Thomaz Albuquerque                     #
##############################################################################################


#################################### Funções Secundárias ######################################

# Função 1
#----------------------------- Escolhendo a palavra de arquivo csv ---------------------------#
def SorteandoPalavra(arquivo1, arquivo2):

    #______________________________ Importação de biblioteca ___________________________________#
    import pandas as pd
    from random import randint

    #________________________________ Banco de Palavras ________________________________________#
    df = pd.read_csv(arquivo1)
    df2 = pd.read_csv(arquivo2)

    #___________________________ Randomização da categoria _____________________________________#
    n = randint(0, 6)

    if n == 0:
        categoriaf = 'Animal'
    elif n == 1:
        categoriaf = 'Cor'
    elif n == 2:
        categoriaf = 'Lugares'
    elif n == 3:
        categoriaf = 'Comida'
    elif n == 4:
        categoriaf = 'Profissões'
    elif n == 5:
        categoriaf = 'Minha sogra é'
    else:
        categoriaf = 'Objeto'

    #____________________________ Randomização da palavra _____________________________________#
    randomico = randint(0, 48)
    palavraf = df[categoriaf][randomico]
    palavra2f = df2[categoriaf][randomico]
    lista1 = []
    lista2 = []

    for i in range(len(palavraf)):
        lista1.append(palavraf[i])

    for i in range(len(palavra2f)):
        lista2.append(palavra2f[i])

    return lista1, lista2, categoriaf, palavraf, palavra2f


# Função 2
#------------------------------------ Definindo o enigma -------------------------------------#
def EnigmaF(palavrinha):
    enigma = []

    d = 0
    for i in range(len(palavrinha)):
        if palavrinha[i].isspace() == True:
            enigma.append(' ')

            d += 1
        elif palavrinha[i] == '-':
            enigma.append('-')

            d += 1
        else:
            enigma.append('_')
    return enigma, d


# Função 3
#------------------------------------ Tentando e verificando o chute --------------------------#
def chutando(lista):
    palpitef = input('Chute uma letra: ')
    while palpitef in lista or len(palpitef) != 1 or palpitef.isdigit() == True:
        if palpitef in lista:
            palpitef = input('Você já deu esse palpite. Tente um novo: ')
        elif len(palpitef) != 1:
            palpitef = input('Só pode 1 carácter. Tente de novo: ')
        elif palpitef.isdigit() == True:
            palpitef = input('É só letra, sua loka. Tenta de novo: ')

    return palpitef


#################################### Função Principal ######################################

def ForcaGame():
    #-------------------------------- Importações de bibliotecas ------------------------------#
    from time import sleep
    from os import system
    import emoji

    system('cls')
    #---------------------------------- Animação de Boas Vindas ------------------------------#
    for i in range(2):
        print(r'''  ______________________________________            😊
  |     BEM-VINDO AO JOGO DA FORCA       |          /|\
  |    ---------------------------       |         / | \ 
  |     Se prepare para o desafio        |          / \
   ______________________________________          /   \
  ''')
        sleep(1.7)
        system('cls')
        print(r'''  ______________________________________           \😉 /
  |     BEM-VINDO AO JOGO DA FORCA       |          \|/
  |    ---------------------------       |           | 
  |     Se prepare para o desafio        |          / \
   ______________________________________          /   \
  ''')
        sleep(1.7)
        system('cls')

    #-------------------------------- Coletando Nome do Jogador--------------------------------#
    nomejogador = input(r'''  ______________________________________            😊
  |     BEM-VINDO AO JOGO DA FORCA       |          /|\
  |    ---------------------------       |         / | \ 
  |     Qual é o nome do jogador?        |          / \
   ______________________________________          /   \
          ''')
    system('cls')

    #-------------------------------- Definindo desenho da forca -------------------------------#
    forca = [r"""_______           
  |
  |
  |
  |
  |
  |   
  |
  """,
             r"""_______           
  |
  |     😁
  |    
  |  
  |    
  |   
  |
  """,
             r"""_______           
  |
  |    🤨
  |    /|\
  |   
  | 
  |  
  |
  """,
             r"""_______           
  |
  |    😮
  |    /|\
  |   / | \
  |  
  | 
  | 
  """,
             r"""_______           
  |
  |    😲
  |    /|\
  |   / | \
  |    / \
  |   
  |
  """,
             r"""_______           
  |
  |    💀
  |    /|\
  |   / | \
  |    / \
  |   /   \
  |
  """]

    #-------------------------------------- Jogando ------------------------------------------#
    vidas = 5
    c = 0  # quantidade de acertos
    listaletras = []
    f = 0  # desenho forca
    letraspalavra, letraspalavra2, categoria, palavra, palavra2 = SorteandoPalavra(
        'tabela palavras.csv', 'tabela palavras - com acento.csv')
    chutes, D = EnigmaF(letraspalavra)
    separador = '-'  # separador das letras

    while vidas != 0:
        coracao = '❤'*(vidas)

        # Menu
        print(
            f'Jogador: {nomejogador}                       Categoria: {categoria}')
        print(
            f'Vidas: {coracao}                         Letras chutadas:{separador.join(listaletras)}')

        # Desenho Forca
        print(forca[f])
        print(' '.join(chutes))

        #__________________________________________ Palpitando _______________________________________#
        palpite = chutando(listaletras)
        listaletras.append(palpite)

        #__________________________________ Errou ou Acertou o chute? ____________________________________#
        if palpite in letraspalavra:
            for i in range(len(letraspalavra)):
                if palpite == letraspalavra[i]:
                    chutes[i] = letraspalavra2[i]
                    c += 1
        else:
            f += 1
            vidas -= 1

        system('cls')

        #__________________________________ Já acertou a palavra toda? ___________________________________#
        if c == (len(letraspalavra)-D):

            # Menu
            print(
                f'Jogador: {nomejogador}                       Categoria: {categoria}')
            print(
                f'Vidas: {coracao}                         Letras chutadas:{separador.join(listaletras)}')

            # Desenho Forca
            print(forca[f])
            print(' '.join(chutes))
            print(
                '''\n____777777777___777777777___
  ___77777777777_777777777777777__
  _7777777777777777777777777777777_
  _7777777777777777777777777777777
  _777777777777( \__/ )77777777777
  _777777777777(=' : '=)777777777_
  __77777777777(")__(")77777777___
  ___77777777777777777777777_____
  ____7777777777777777777_______
  ______7777777777777777________
  ________77777777777___________
  ___________77777______________
  _____________7________________''')
            sleep(1.9)
            system('cls')

            textofinal = f'''
  ⊂_ヽ 
  　 ＼＼ Λ＿Λ 
  　　 ＼( 'ㅅ' ) 
  　　　 >　⌒ヽ 
  　　　/ 　 へ＼ 
  　　 /　　/　＼＼ 
  　　 ﾚ　ノ　　 ヽ_つ 
  　　/　/ 
  　 /　/| 
  　(　(ヽ 
  　|　|、＼ 
  　| 丿 ＼ ⌒) 
  　| |　　) / 
  `ノ )　　Lﾉ
  PARABÉNS, AMORE! A palavra é {palavra2}'''
            break

    #__________________________________ Já acabou com todas as chances? _________________________________#
    if vidas == 0:
        # Menu
        print(
            f'Jogador: {nomejogador}                       Categoria: {categoria}')
        print(
            f'Vidas: ❌                         Letras chutadas:{separador.join(listaletras)}')

        # Desenho Forca
        print(forca[f])
        print(' '.join(chutes))
        textofinal = f'\n ಥ_ಥ GAME OVER! Você não conseguiu descobrir a palavra {palavra}'

    #-------------------------------------- Resultado do jogo ------------------------------------------#
    print(f'{textofinal}\n')
    resp = input('Quer jogar de novo? (S/N) ').strip()[0].upper()
    while resp == "N":
        break
    while resp not in "SN":
        resp = input(
            'S ou N amore!! Quer jogar de novo? (S/N) ').strip()[0].upper()
    while resp in "S":
        ForcaGame()


################################################# START ###############################################
ForcaGame()
