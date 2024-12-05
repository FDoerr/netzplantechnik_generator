

class Netzplanknoten():

    def __init__(
                self,
                name:str,
                dauer:int,
                direkte_nachfolger:list|None = None,
                direkte_vorgaenger:list|None = None #TODO: line not needed?
                ) -> None:
        
        self.name:  str = name 
        self.dauer: int = dauer
        self.direkte_nachfolger: list|None = direkte_nachfolger
        self.direkte_vorgaenger: list = list()

        self.faz: int|None = None 
        self.fez: int|None = None 

        self.saz: int|None = None
        self.sez: int|None = None     
      
        self.gesamt_puffer: int|None = None
        self.freier_puffer: int|None = None   
          
        
    def __repr__(self) -> str:
        return f'{self.name}'
    
        
    def __str__(self) -> str:
        output_str: str = f'''\
   Direkte Vorgänger: {self.direkte_vorgaenger}
    FAZ           FEZ
     ↓             ↓
  ┌──────┐      ┌──────┐
  │  {self.faz:0>2}  │      │  {self.fez:0>2}  │
  ├──────┴──────┴──────┤
  │{self.name: ^20}│
  ├──────┬──────┬──────┤
D→│  {self.dauer:0>2}  │  {self.gesamt_puffer:0>2}  │  {self.freier_puffer:0>2}  │←FP
  ├──────┼──────┼──────┤
  │  {self.saz:0>2}  │   ↑  │  {self.sez:0>2}  │
  └──────┘  GP  └──────┘
     ↑              ↑
    SAZ            SEZ
   Direkte Nachfolger: {self.direkte_nachfolger}'''
        return output_str


    def berechne_faz(self) -> None:
        # max FEZ des Vorgängers

        max_fez_vorgaenger = 0

        for vorgaenger in self.direkte_vorgaenger:            
            fez_vorgaenger = vorgaenger.fez

            if fez_vorgaenger >= max_fez_vorgaenger:
                max_fez_vorgaenger = fez_vorgaenger

        self.faz = max_fez_vorgaenger



    def berechne_fez(self) -> None:
        # faz + dauer

        if self.faz is None: # start des netzplans
            self.fez = self.dauer      
        else:            
            self.fez = self.faz + self.dauer 


    def berechne_sez(self) -> None:
        # min SAZ des nachfolgers

        dir_nachfolger = self.direkte_nachfolger
        if dir_nachfolger == [] or dir_nachfolger is None : #Ende des Netzplans
            self.sez = self.fez

        else:
            liste_saz_nachfolger = list()
            for nachfolger in dir_nachfolger:
                liste_saz_nachfolger.append(nachfolger.saz)

            self.sez = min(liste_saz_nachfolger)
        
       
    def berechne_saz(self) -> ValueError | None:
        # SEZ - dauer

        if self.sez is None:
            return ValueError(f'Error: SEZ von {self.name=} ist None')
        self.saz = self.sez - self.dauer


    def berechne_gesamt_puffer(self):
        # SAZ - FAZ
        
        if self.saz is None or self.sez is None:
           return ValueError(f'Error: SAZ oder SEZ von {self.name=} ist None')
        
        self.gesamt_puffer = self.saz - self.faz # type: ignore


    def berechne_freier_puffer(self):
        # min FAZ des Nachfolgers - FEZ

        dir_nachfolger = self.direkte_nachfolger
        if dir_nachfolger == [] or dir_nachfolger is None : #Ende des Netzplans
            self.freier_puffer = 0

        else:
            liste_faz_nachfolger = list()
            for nachfolger in dir_nachfolger:
                liste_faz_nachfolger.append(nachfolger.faz)

            self.freier_puffer = min(liste_faz_nachfolger) - self.fez

