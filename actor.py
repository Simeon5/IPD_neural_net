import random


class Actor:



    # Bestimmt zufällig Strategie des dummen Spielers
    def strategy(self, n):

        # Always Cooperate
        if self.strategy_decider <= 0.33:

            self.alwayscooperate()

        # Always Defect
        elif 0.33 < self.strategy_decider <= 0.66:

            self.alwaysdefect()

        #TFT
        else:

            self.titfortat(n)




    #Instanzierung
    def __init__(self, name):

        self.name = name
        self.decisions = []
        self.Gesamtnutzen = 0
        self.strategy_decider = random.random()


    #Strategien
    def alwaysdefect(self):

        print(self.name + " spielt 1")
        self.decisions.append(1)


    def alwayscooperate(self):

        print(self.name + " spielt 0")
        self.decisions.append(0)


    def titfortat(self,i):

        if i<=1:
            print(self.name + " spielt 0")
            self.decisions.append(0)


        else:
            print(str(self.name) + " spielt " + str(self.opponent.decisions[i-2]))
            self.decisions.append(self.opponent.decisions[i-2])



    #Gegner festlegen
    def set_opponent(self, enemy):

        self.opponent=enemy
