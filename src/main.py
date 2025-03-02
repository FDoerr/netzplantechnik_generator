from netzplanknoten import Netzplanknoten as Knoten
from netzplan_manager import Netzplanmanager
from random_netzplan_generator import RandomNetzplanGenerator as Generator


def main():

    knoten_8 = Knoten('Knoten_8', 2, [])
    knoten_7 = Knoten('Knoten_7', 5, [knoten_8])
    knoten_6 = Knoten('Knoten_6', 10, [knoten_7])
    knoten_5 = Knoten('Knoten_5', 8, [knoten_7])
    knoten_4 = Knoten('Knoten_4', 2, [knoten_6, knoten_5])
    knoten_3A = Knoten('Knoten_3A', 4, [knoten_6])
    knoten_3 = Knoten('Knoten_3', 7, [knoten_3A])
    knoten_2 = Knoten('Knoten_2', 10, [knoten_6])
    knoten_1 = Knoten('Knoten_1', 3, [knoten_2, knoten_3, knoten_4])

    alle_knoten = [knoten_1, knoten_2, knoten_3, knoten_3A, knoten_4, knoten_5, knoten_6, knoten_7, knoten_8]

    netzplanmanager = Netzplanmanager(alle_knoten)

    netzplanmanager.vorgaenger_zuweisen()
    netzplanmanager.knoten_vorwaerts_rechnen()
    netzplanmanager.knoten_rueckwaerts_rechnen()
    netzplanmanager.gesamt_puffer_berechnen()
    netzplanmanager.freie_puffer_berechnen()
    #netzplanmanager.alle_knoten_ausgeben()
    #kritischer_pfad_liste= netzplanmanager.kritischen_pfad_bestimmen()
    #print('Kritischer Pfad: ', kritischer_pfad_liste)
    netzplanmanager.visualisiere_netzplan()
    

    #generator = Generator()
    #generator.netzplan_generieren()
    ...


if __name__=='__main__':
    main()