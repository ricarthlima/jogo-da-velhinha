import random

#32 pesos
def neuronios(a,b,c,d,listaPesos):
    neuroniosA = []
    for i in range(0,4):
        l1 = a * listaPesos[1+(i*4)]
        l2 = b * listaPesos[2+(i*4)]
        l3 = c * listaPesos[3+(i*4)]
        l4 = d * listaPesos[4+(i*4)]
        neuronio = l1 + l2 + l3 + l4
        if (neuronio > 0):
            neuroniosA.append(neuronio)
        else:
            neuroniosA.append(0)

    neuroniosB = []
    for i in range(0,4):
        l1 = neuroniosA[0] * listaPesos[17+(i*4)]
        l2 = neuroniosA[1] * listaPesos[18+(i*4)]
        l3 = neuroniosA[2] * listaPesos[19+(i*4)]
        l4 = neuroniosA[3] * listaPesos[20+(i*4)]
        neuronio = l1 + l2 + l3 + l4
        if (neuronio > 0):
            neuroniosB.append(neuronio)
        else:
            neuroniosB.append(0)

    return neuroniosB

def pesar(a,b,c,d):
    pesos = []
    for i in range(0,34):
        pesos.append(random.randint(-1000,1000))
    return neuronios(a,b,c,d,pesos)

def jogar(tabuleiro):
    jogadas = pesar(tabuleiro[0],tabuleiro[1],tabuleiro[2],tabuleiro[3])
    return jogadas.index(max(jogadas))

def vencedor(i, tipo):
    if (tipo == "PVP"):
        print("Vencedor é o jogador " + str(i-1))

    if (tipo == "PVM"):
        if (i == 2):
            print("Você venceu!")
        else:
            print("Você perdeu!")

def empate():
    print("Deu empate")

def printTabuleiro(tabuleiro):
    tab = []
    for i in tabuleiro:
        if i == 1:
            tab.append(" ")
        if i == 2:
            tab.append("X")
        if i == 3:
            tab.append("O")
    print("|"+tab[0]+"|"+tab[1]+"|")
    print("-----")
    print("|"+tab[2]+"|"+tab[3]+"|")


#PvP
def pvp():
    tabuleiro = [1,1,1,1]
    vezDe = 1
    while True:
        #Verifica se o jogo acabou
        if ((tabuleiro[0] == tabuleiro[3]) and tabuleiro[0] != 1):
            vencedor(tabuleiro[0], "PVP")
            break
        elif ((tabuleiro[1] == tabuleiro[2]) and tabuleiro[1] != 1):
            vencedor(tabuleiro[1], "PVP")
            break
        elif (((tabuleiro[0] == tabuleiro[1]) and (tabuleiro[2] == tabuleiro[3]) or (tabuleiro[0] == tabuleiro[2]) and (tabuleiro[1] == tabuleiro[3])) and tabuleiro[0] != 1 and tabuleiro[2] != 1):
            empate()
            break
        else:
            print("Vez do jogador: " + str(vezDe))
            i = int(input(">>> "))
            if (i >= 0 and i < 4) and tabuleiro[i] == 1:
                tabuleiro[i] = vezDe + 1
            else:
                print("Jogou errado!")

            vezDe = (vezDe % 2) + 1
            printTabuleiro(tabuleiro)


#PvM
def pvm():
    tabuleiro = [1,1,1,1]
    vezDe = 2
    while True:
        #Verifica se o jogo acabou
        if ((tabuleiro[0] == tabuleiro[3]) and tabuleiro[0] != 1):
            vencedor(tabuleiro[0], "PVM")
            break
        elif ((tabuleiro[1] == tabuleiro[2]) and tabuleiro[1] != 1):
            vencedor(tabuleiro[1], "PVM")
            break
        elif (((tabuleiro[0] == tabuleiro[1]) and (tabuleiro[2] == tabuleiro[3]) or (tabuleiro[0] == tabuleiro[2]) and (tabuleiro[1] == tabuleiro[3])) and tabuleiro[0] != 1 and tabuleiro[2] != 1):
            empate()
            break
        else:
            if (vezDe == 1):
                print("\nSua vez:")            
                i = int(input(">>> "))
            else:
                print("\nVez da máquina!")
                i = jogar(tabuleiro)
            if (i >= 0 and i < 4) and tabuleiro[i] == 1:
                tabuleiro[i] = vezDe + 1
            else:
                print("\nJogou errado, perdeu a vez!")

            vezDe = (vezDe % 2) + 1
            printTabuleiro(tabuleiro)

#MAIN
pvm()
        

