from machine import Machine
import aux_module
import random

def endGame(tabuleiro):
    '''Verifica se o jogo acabou'''
    if ((tabuleiro[0] == tabuleiro[3]) and tabuleiro[0] != -1):
        return tabuleiro[0]
    elif ((tabuleiro[1] == tabuleiro[2]) and tabuleiro[1] != -1):
        return tabuleiro[1]
    elif (((tabuleiro[0] == tabuleiro[1]) and (tabuleiro[2] == tabuleiro[3]) or (tabuleiro[0] == tabuleiro[2]) and (tabuleiro[1] == tabuleiro[3])) and tabuleiro[0] != -1 and tabuleiro[2] != -1):
        return 0
    else:
        return -1

# -1 => Espaço Vazio
# 1 => Marcado pro Jogador
# 2 => Marcado pra Maquina
def newMatch(machine, evolve):
    machine.gerarPesos()
    
    rodadas = 0
    tabuleiro = [-1,-1,-1,-1]
    turn = random.randint(1,2)

    while True:
        end = endGame(tabuleiro)
        if end == 1:
            if not evolve: print("Você venceu!")
            return aux_module.compararResultado(machine, "LOSE", rodadas)
        elif end == 2:
            if not evolve: print("Você perdeu!")
            return aux_module.compararResultado(machine, "WIN", rodadas)
        elif end == 0:
            if not evolve: print("Empate!")
            return aux_module.compararResultado(machine, "DRAW", rodadas)
        elif end == -1:
            rodadas = rodadas + 1
            
            i = -1
            if (turn == 1):
                if not evolve: print("\n>>> Sua vez <<<")
                if not evolve:
                    i = int(input(">>> "))
                else:
                    i = random.randint(0,3)
                    while tabuleiro[i] != -1:                
                        i = random.randint(0,3)
            else:
                if not evolve: print("\n>>> Vez da Maquina <<<")
                i = machine.jogar(tabuleiro)

            if (i >= 0 and i < 4) and (tabuleiro[i] == -1):
                tabuleiro[i] = turn
            else:
                if not evolve: print("\nJogada Incorreta!")
                if turn == 1:
                    if not evolve: print("Você perdeu!")
                    return aux_module.compararResultado(machine, "WIN", rodadas)
                else:
                    if not evolve: print("Você ganhou!")
                    return aux_module.compararResultado(machine, "ERROR", rodadas)

            turn = (turn % 2) + 1
            if not evolve: aux_module.printTabuleiro(tabuleiro)

def testGenerations(listMachine):
    i = 0
    for machine in listMachine:
        print("INDIVIDUO "+str(i + (machine.generation * 500)))
        ws = True
        while ws:
            ws = newMatch(machine, True)
        i = i +1

def makeEnvolve():
    # Generation 0
    listMachines = []
    gen = 0
    n = 500
    for i in range(n):
        m = Machine()
        m.gerarPesos()
        
        listMachines.append(m)

    while True:
        print("GERACAO "+ str(gen))
        # Faz testes
        testGenerations(listMachines)

        # Avança a Geração
        gen += 1
        listMachines = aux_module.evolve(gen, n)

def fight(gen):
    m = Machine(gen)
    m.readBest(True)
    while True:
        newMatch(m, False)
    
if  __name__ == "__main__":
    makeEnvolve()
    #fight(124)
        
