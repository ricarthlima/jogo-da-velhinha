import random
import os.path

#32 pesos
class Machine:
    def __init__(self, generation = 0):
        self.pesos = []
        self.generation = generation
        self.erro = False
        self.empates = 0
        self.winStreak = 0
        self.roundsToLose = 0
        
    def neuronios(self, tabuleiro):
        a = tabuleiro[0]
        b = tabuleiro[1]
        c = tabuleiro[2]
        d = tabuleiro[3]
        neuroniosA = []
        for i in range(0,4):
            l1 = a * self.pesos[1+(i*4)]
            l2 = b * self.pesos[2+(i*4)]
            l3 = c * self.pesos[3+(i*4)]
            l4 = d * self.pesos[4+(i*4)]
            neuronio = l1 + l2 + l3 + l4
            if (neuronio > 0):
                neuroniosA.append(neuronio)
            else:
                neuroniosA.append(0)

        neuroniosB = []
        for i in range(0,4):
            l1 = neuroniosA[0] * self.pesos[17+(i*4)]
            l2 = neuroniosA[1] * self.pesos[18+(i*4)]
            l3 = neuroniosA[2] * self.pesos[19+(i*4)]
            l4 = neuroniosA[3] * self.pesos[20+(i*4)]
            neuronio = l1 + l2 + l3 + l4
            if (neuronio > 0):
                neuroniosB.append(neuronio)
            else:
                neuroniosB.append(0)

        return neuroniosB

    def gerarPesos(self):
        pesos = []
        for i in range(0,34):
            pesos.append(random.randint(-1000,1000))
        self.pesos = pesos

    def jogar(self, tabuleiro):
        jogadas = self.neuronios(tabuleiro)
        return jogadas.index(max(jogadas))

    def writeBest(self):
        file = open('g'+str(self.generation)+'.csv','w')
        file.write('gen:'+str(self.generation)+"\n")
        file.write('error:'+str(self.erro)+"\n")
        file.write('draws:'+str(self.empates)+"\n")
        file.write('ws:'+str(self.winStreak)+"\n")
        file.write('rtl:'+str(self.roundsToLose)+"\n")
        for peso in self.pesos:
            file.write(str(peso) + ";")
        file.close()
    
    def readBest(self,bol):
        if bol:
            if os.path.exists('g'+str(self.generation)+'.csv'):
                file = open('g'+str(self.generation)+'.csv','r')
                txt = file.read()
                file.close()

                linhas = txt.split("\n")

                #Ler Geração
                self.generation = int(linhas[0].split(":")[1])
                
                #Ler Erro
                erro = linhas[1].split(":")[1]
                if erro == "False":
                    self.erro = False
                else:
                    self.erro = True

                #Ler Empates
                self.empates = int(linhas[2].split(":")[1])

                #Ler WinStreak
                self.winStreak = int(linhas[3].split(":")[1])

                #Ler RoundsToLose
                self.roundsToLose = int(linhas[4].split(":")[1])

                #Ler Pesos
                listaStrings = linhas[5].split(";")
                listaInts = []
                for string in listaStrings:
                    if(string != ""):
                        listaInts.append(int(string))

                self.pesos = listaInts
            else:
                self.gerarPesos()
                self.writeBest()
