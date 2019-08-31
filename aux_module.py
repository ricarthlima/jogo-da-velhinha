from machine import Machine
import random

def printTabuleiro(tabuleiro):
    tab = []
    for i in tabuleiro:
        if i == -1:
            tab.append(" ")
        if i == 1:
            tab.append("X")
        if i == 2:
            tab.append("O")
    print("|"+tab[0]+"|"+tab[1]+"|")
    print("-----")
    print("|"+tab[2]+"|"+tab[3]+"|")

def compararResultado(machine, status, rodadas):
    best = Machine(machine.generation)
    best.readBest(True)
    continuar = False

    if status == "LOSE":
        roundsToLose = rodadas
    elif status == "WIN":
        machine.winStreak += 1
        continuar = True
    elif status == "DRAW":
        machine.winStreak += 1
        machine.empates += 1
        continuar = True
    elif status == "ERROR":
        machine.erro = True

    newBest = False
    if (status != "ERROR"):
        if (machine.winStreak > best.winStreak):
            newBest = True
        elif (best.winStreak == machine.winStreak) and (machine.empates < best.empates):
            newBest = True
        elif (best.winStreak == machine.winStreak) and (machine.empates == best.empates) and (machine.roundsToLose > best.roundsToLose):
            newBest = True

    if newBest:
        machine.writeBest()

    return continuar

def gaussianRandom(point, gen):
    a = -9999
    sigma = 10 - gen
    if sigma <= 1 :
        sigma = 1
    while a < -1000 or a > 1000:
        a = int(random.gauss(point, sigma))
    return a

def evolve(generation, n):
    best = Machine(generation)
    best.readBest(True)

    listMachines = []
    for ind in range(n):
        pesos = []
        for pes in range(0,34):
            pesos.append(gaussianRandom(best.pesos[pes],generation))

        newMachine = Machine()
        newMachine.pesos = pesos
        newMachine.generation = generation

        listMachines.append(newMachine)
    return listMachines
