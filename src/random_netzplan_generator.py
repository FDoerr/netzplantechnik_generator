from netzplanknoten import Netzplanknoten as Knoten
import random


class RandomNetzplanGenerator:

    def __init__(self,
                 anzahl_knoten:int  = 10,
                 max_dauer:int      = 10,
                 max_nachfolger:int = 3,
                 seed               = None
                 ) -> None:
        
        self.anzahl_knoten  = anzahl_knoten
        self.max_dauer      = max_dauer
        self.max_nachfolger = max_nachfolger        

        self.seed = seed


    def netzplan_generieren(self): 

        random.seed = self.seed
        liste_knoten = list()

        # knoten erzeugen
        for i in range(self.anzahl_knoten):
            name: str  = f'Knoten_{i}'
            dauer: int = random.randint(1, self.max_dauer)
        
            knoten = Knoten(name, dauer)

            liste_knoten.append(knoten)


        # nachfolger festlegen

        for i, knoten in enumerate(liste_knoten):
            anzahl_nachfolger: int = random.randint(0, self.max_nachfolger)
            
            #TODO: überprüfen ob mehr nachfolger als folgeknoten in liste exisitieren
            anzahl_restliche_elemente: int = len(liste_knoten) - i
            print(f'{anzahl_restliche_elemente <= anzahl_nachfolger=}')
            if anzahl_restliche_elemente <= anzahl_nachfolger:
                print('zu viele nachfolger')


            # print(f'{knoten.name}: {anzahl_nachfolger=}')
            # for j in range(anzahl_nachfolger):
            #     print(f'Nachfolger: {liste_knoten[i+j+1].name}')

        

        print(liste_knoten)
        return liste_knoten
    

    #def netzplan_generieren2():
        #  pfade  generieren
        #  lege fest wie viele pfade es geben soll
        #  platziere teil der knoten auf pfad also knoten/pfad
        #  platziere andere knoten auf alternativpfaden
        #  generiere random verbindungen zwischen pfaden
        #  mini pfade 
       # ...

