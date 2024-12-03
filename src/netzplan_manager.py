from netzplanknoten import Netzplanknoten

class Netzplanmanager:

    def __init__(self, alle_knoten:list[Netzplanknoten]) -> None:
        self.alle_knoten: list[Netzplanknoten] = alle_knoten


    def vorgaenger_zuweisen(self) -> None:

        for knoten in self.alle_knoten:
            for nachfolger in knoten.direkte_nachfolger:
                nachfolger.direkte_vorgaenger.append(knoten)


    def knoten_platzieren(self):        
        for knoten in self.alle_knoten:
            print(knoten)
            print('--------------------')
