#Nutzenfunktion

class Nutzen:

    def get_utility(Spieler1, Spieler2, x):
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
