import actor
import random

#KLassse erstellt Spieler und lässt sie gegeneinander spielen
class Model:

    Rundenzahl = 0


    def __init__(self, n):

        self.Rundenzahl = n

        actor1 = actor.Actor("Spieler1")
        actor2 = actor.Actor("Spieler2")

        actor1.set_opponent(actor2)
        actor2.set_opponent(actor1)


        i=1
        while i<= self.Rundenzahl:
            actor1.strategy(i)
            actor2.strategy(i)
            self.get_utility(actor1, actor2, i)
            i = i+1

        print (actor1.decisions)
        print (actor2.decisions)


    #Nutzenfunktion
    def get_utility(self, Spieler1, Spieler2, x):
        T=5
        P=1
        R=3
        S=0

        if (Spieler1.decisions[x-1]==0 and Spieler2.decisions[x-1]==0):
            Spieler1.Gesamtnutzen = Spieler1.Gesamtnutzen + R
            Spieler2.Gesamtnutzen = Spieler2.Gesamtnutzen + R

        elif (Spieler1.decisions[x-1]==0 and Spieler2.decisions[x-1]==1):
            Spieler1.Gesamtnutzen = Spieler1.Gesamtnutzen + P
            Spieler2.Gesamtnutzen = Spieler2.Gesamtnutzen + S

        elif (Spieler1.decisions[x-1]==1 and Spieler2.decisions[x-1]==0):
            Spieler1.Gesamtnutzen = Spieler1.Gesamtnutzen + S
            Spieler2.Gesamtnutzen = Spieler2.Gesamtnutzen + P

        elif (Spieler1.decisions[x-1]==1 and Spieler2.decisions[x-1]==1):
            Spieler1.Gesamtnutzen = Spieler1.Gesamtnutzen + T
            Spieler2.Gesamtnutzen = Spieler2.Gesamtnutzen + T

        else:
            print("Fail Utility")

        print("Spieler 1 Gesamtnutzen: " + str(Spieler1.Gesamtnutzen))
        print("Spieler 2 Gesamtnutzen: " + str(Spieler2.Gesamtnutzen))
