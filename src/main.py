from netzplanknoten import Netzplanknoten as knoten
from netzplan_manager import Netzplanmanager


def main():
    knoten_4 = knoten('knoten_4', 3, [])
    knoten_3 = knoten('knoten_3', 3, [knoten_4])
    knoten_2 = knoten('knoten_2', 2, [knoten_4])
    knoten_1 = knoten('knoten_1', 1, [knoten_2, knoten_3])


    alle_knoten = [knoten_1, knoten_2, knoten_3, knoten_4]
    netzplanmanager = Netzplanmanager(alle_knoten)

    netzplanmanager.vorgaenger_zuweisen()
    netzplanmanager.knoten_vorwaerts_rechnen()
    netzplanmanager.knoten_rueckwaerts_rechnen()
    netzplanmanager.gesamt_puffer_berechnen()
    netzplanmanager.freie_puffer_berechnen()
    netzplanmanager.alle_knoten_ausgeben()
    kritischer_pfad_liste= netzplanmanager.kritischen_pfad_bestimmen()
    print('Kritischer Pfad: ', kritischer_pfad_liste)
    ...


if __name__=='__main__':
    main()