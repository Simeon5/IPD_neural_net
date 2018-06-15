import random

#Spieler der immer kooperiert
class PDAC:
    
    #Instanzierung
    def __init__(self,name):
        self.name = name
        self.decisions = []
        self.Gesamtnutzen = 0
               


    #Spielentscheidung
    def play(self,i):
        self.decisions.append(0)
        return 0


    #Gegner festlegen
    def set_opponent(self, enemy):
        self.opponent=enemy
        
    
    #String methode überschreiben zur Ausgabe der Spielerdetails
    def __str__(self):
        return self.name+": \n" + "Gesamtnutzen: " + str(self.Gesamtnutzen) + "\n" +"Durschnittgewinn/Runde: " + str(self.Gesamtnutzen/len(self.decisions)) + "\n" + str(self.decisions)







#Spieler der immer schweigt
class PDAD:

    #Instanzierung
    def __init__(self,name):
        self.name = name
        self.decisions = []
        self.Gesamtnutzen = 0


    #Spielentscheidung
    def play(self,i):
        self.decisions.append(1)
        return 1


    #Gegner festlegen
    def set_opponent(self, enemy):
        self.opponent=enemy

    #String methode überschreiben zur Ausgabe der Spielerdetails
    def __str__(self):
        return self.name+": \n" + "Gesamtnutzen: " + str(self.Gesamtnutzen) + "\n" +"Durschnittgewinn/Runde: " + str(self.Gesamtnutzen/len(self.decisions)) + "\n" + str(self.decisions)





#Spieler der Tft spielt
class PDTft:

    #Instanzierung
    def __init__(self,name):
        self.name = name
        self.decisions = []
        self.Gesamtnutzen = 0


    #Spielentscheidung
    def play(self,i):

        if i<=1:
            print(self.name + " spielt 0")
            self.decisions.append(0)

        else:
            print(str(self.name) + " spielt " + str(self.opponent.decisions[i-2]))
            self.decisions.append(self.opponent.decisions[i-2])


    #Gegner festlegen
    def set_opponent(self, enemy):
        self.opponent=enemy

    #String methode überschreiben zur Ausgabe der Spielerdetails
    def __str__(self):
        return self.name+": \n" + "Gesamtnutzen: " + str(self.Gesamtnutzen) + "\n" +"Durschnittgewinn/Runde: " + str(self.Gesamtnutzen/len(self.decisions)) + "\n" + str(self.decisions)




#Spieler der random spielt
class PDrandom:

    #Instanzierung
    def __init__(self,name):
        self.name = name
        self.decisions = []
        self.Gesamtnutzen = 0


    #Spielentscheidung
    def play(self,i):

        if random.random() <= 0.5:
            self.decisions.append(0)
            return 0

        else:
            self.decisions.append(1)
            return 1


    #Gegner festlegen
    def set_opponent(self, enemy):
        self.opponent=enemy

    #String methode überschreiben zur Ausgabe der Spielerdetails
    def __str__(self):
        return self.name+": \n" + "Gesamtnutzen: " + str(self.Gesamtnutzen) + "\n" +"Durschnittgewinn/Runde: " + str(self.Gesamtnutzen/len(self.decisions)) + "\n" + str(self.decisions)
