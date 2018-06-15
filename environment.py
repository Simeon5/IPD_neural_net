import actors
from util import Nutzen
import random

class Environment:


    def __init__(self,n):

        self.Rundenzahl = n

        #Intelligenter Spieler erzeugen
        actor1 = actors.PDAC("Spieler1")


        #Gegner mit zufälliger Strategie erstellen
        x = random.random()

        if x <0.25:
            actor2 = actors.PDAC("Spieler2")

        elif 0.25 <= x < 0.5:
            actor2 = actors.PDAD("Spieler2")

        elif 0.5 <= x < 0.75:
            actor2 = actors.PDTft("Spieler2")

        else:
            actor2 = actors.PDrandom("Spieler2")



        #Gegner festlegen
        actor1.set_opponent(actor2)
        actor2.set_opponent(actor1)


        #Spielbeginn
        i=1
        while i<= self.Rundenzahl:
            actor1.play(i)
            actor2.play(i)
            Nutzen.get_utility(actor1, actor2, i)
            i = i+1
        
        print(actor1)
        print("\n")
        print(actor2)
