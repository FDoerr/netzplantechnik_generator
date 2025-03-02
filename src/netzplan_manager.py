from netzplanknoten import Netzplanknoten
import matplotlib.pyplot as plt
import networkx as nx
import plotly.graph_objects as go
import math

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


    def kritischen_pfad_bestimmen(self) -> list[Netzplanknoten]:

        kritischer_pfad_liste = list()

        for knoten in self.alle_knoten:  
            if knoten.gesamt_puffer == 0: 
                kritischer_pfad_liste.append(knoten)

        return kritischer_pfad_liste



    def alle_knoten_ausgeben(self):
        for knoten in self.alle_knoten:        
            print('--------------------------------------------------------------')    
            print(knoten)



    def layout_schalen_winkel(self, graph, start_winkel=0, end_winkel=45):        
        
        start_knoten = list(graph.nodes())[0]
        # print(graph)
        # knoten_zu_ebene_dict = nx.single_source_shortest_path_length(graph, start_knoten) # z.B.: {'1': 0, '2': 1, '3': 1, '4': 1, '6': 2, '5': 2, '7': 3, '8': 4}
        knoten_zu_ebene_dict = {node: depth for depth, layer in enumerate(nx.bfs_layers(graph, start_knoten)) for node in layer}
        
        ebene_zu_knoten_dict = dict() # z.B.: {0: ['1'], 1: ['2', '3', '4'], 2: ['6', '5'], 3: ['7'], 4: ['8']}
        for knoten, ebene in knoten_zu_ebene_dict.items():
            ebene_zu_knoten_dict.setdefault(ebene, []).append(knoten)    


        knoten_zu_koordinaten_dict = dict() # z.B.: '1': (1.00, 0.42), '2': (1.81, 0.85)...
        for ebene, knoten_in_ebene in ebene_zu_knoten_dict.items():
            anzahl_knoten = len(knoten_in_ebene)
            radius = ebene + 1
            for index_knoten_in_ebene, knoten in enumerate(knoten_in_ebene):                
                # Winkel des aktuellen knotens verteilt auf Kreisbogen eingeschlossen zwischen start und end Winkeln 
                winkel = start_winkel + index_knoten_in_ebene * (end_winkel - start_winkel) / max(1, anzahl_knoten - 1)
                # Umrechnung in x-y-Koordinaten
                winkel_rad = math.radians(winkel)
                knoten_zu_koordinaten_dict[knoten] = (radius * math.cos(winkel_rad), radius * math.sin(winkel_rad))
        
        return knoten_zu_koordinaten_dict


    def visualisiere_netzplan(self):
        graph = nx.DiGraph()

        # Knoten und Kanten hinzufügen
        for knoten in self.alle_knoten:
            graph.add_node(knoten.name)
            for nachfolger in knoten.direkte_nachfolger:
                graph.add_edge(knoten.name, nachfolger.name)

        # Benutzerdefiniertes Layout erstellen
        pos = self.layout_schalen_winkel(graph, start_winkel=0, end_winkel=25)

        ax = plt.gca()
        for ebene in range(1, len(pos) + 1):
            circle = plt.Circle((0, 0), radius=ebene + 1, color="gray", fill=False, linestyle="--")
            ax.add_artist(circle)
        plt.axis("equal")

        # Graph zeichnen
        nx.draw(
            graph, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10
        )
        plt.show()