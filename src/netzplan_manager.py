from netzplanknoten import Netzplanknoten

class Netzplanmanager:

    def __init__(self, alle_knoten:list[Netzplanknoten]) -> None:
        self.alle_knoten: list[Netzplanknoten] = alle_knoten


    def vorgaenger_zuweisen(self) -> None:

        for knoten in self.alle_knoten:
            for nachfolger in knoten.direkte_nachfolger: # type: ignore
                nachfolger.direkte_vorgaenger.append(knoten) # type: ignore


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


    def kritischen_pfad_bestimmen(self) -> list[Netzplanknoten]:
        kritischer_pfad_liste = list()

        for knoten in self.alle_knoten:  
            if knoten.gesamt_puffer == 0: 
                kritischer_pfad_liste.append(knoten)

        return kritischer_pfad_liste    


    def alle_knoten_ausgeben(self) -> None:
        for knoten in self.alle_knoten:        
            print('--------------------------------------------------------------')    
            print(knoten)


    def generiere_mermaid_diagramm(self) -> str:
        diagramm_str = "paste diagramm here:  https://mermaid.live/\n"
        diagramm_str += "graph LR\n"
        for knoten in self.alle_knoten:
            diagramm_str += f"    {knoten.name}[\"{knoten.name}"
            diagramm_str += f"<br>FAZ: {knoten.faz} | FEZ: {knoten.fez}"
            diagramm_str += f"<br>D: {knoten.dauer} | GP: {knoten.gesamt_puffer} | FP: {knoten.freier_puffer}"
            diagramm_str += f"<br>SAZ: {knoten.saz} | SEZ: {knoten.sez}\"]\n"
            for vorgaenger in knoten.direkte_vorgaenger:
                diagramm_str += f"    {vorgaenger.name} --> {knoten.name}\n"
        return diagramm_str