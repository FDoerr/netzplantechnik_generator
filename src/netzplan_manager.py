from netzplanknoten import Netzplanknoten

class Netzplanmanager:

    def __init__(self, alle_knoten:list[Netzplanknoten]) -> None:
        self.alle_knoten: list[Netzplanknoten] = alle_knoten


    def vorgaenger_zuweisen(self) -> None:

        for knoten in self.alle_knoten:
            for nachfolger in knoten.direkte_nachfolger: # type: ignore
                nachfolger.direkte_vorgaenger.append(knoten) # type: ignore


    def knoten_platzieren(self):        
        for knoten in self.alle_knoten:
            print(knoten)
            print('--------------------')


    def knoten_vorwaerts_rechnen(self) -> None:
        for knoten in self.alle_knoten:
            knoten.berechne_faz()
            knoten.berechne_fez()
    

    def knoten_rueckwaerts_rechnen(self) -> None:
        for knoten in reversed(self.alle_knoten):
            knoten.berechne_sez()
            knoten.berechne_saz()
 
    
    def freie_puffer_berechnen(self) -> None:
        for knoten in self.alle_knoten:
            knoten.berechne_freier_puffer()


    def gesamt_puffer_berechnen(self) -> None:
        for knoten in self.alle_knoten:
            knoten.berechne_gesamt_puffer()

