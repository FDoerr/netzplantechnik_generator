

class Netzplanknoten():

    def __init__(
                self,
                name:str,
                dauer:int,
                direkte_nachfolger:list|None = None,
                direkte_vorgaenger:list|None = None
                ) -> None:
        
        self.name:  str = name 
        self.dauer: int = dauer
        self.direkte_nachfolger: list|None = direkte_nachfolger
        self.direkte_vorgaenger: list = []

        self.faz: int|None = None 
        self.fez: int|None = None 

        self.saz: int|None = None
        self.sez: int|None = None     
      
        self.gesamt_puffer: int|None = None
        self.freier_puffer: int|None = None   

          
        
    def __repr__(self) -> str:
        return f'{self.name}'
        
                # {self.dauer=}
                # {self.direkte_nachfolger=}
                # {self.direkte_vorgaenger=}
                # {self.faz=}
                # {self.fez=}
                # {self.saz=}
                # {self.sez=}
                # {self.gesamt_puffer=}
                # {self.freier_puffer=}
        

    def berechne_faz(self):
        # max FEZ des Vorgängers

        max_fez_vorgaenger = 0

        for vorgaenger in self.direkte_vorgaenger:            
            fez_vorgaenger = vorgaenger.fez

            if fez_vorgaenger >= max_fez_vorgaenger:
                max_fez_vorgaenger = fez_vorgaenger

        self.faz = max_fez_vorgaenger

        #print(f'{self.name=} FAZ gesetzt: {self.faz=}')




    def berechne_fez(self):
        # faz + dauer

        if self.faz is None: # start des netzplans
            self.fez = self.dauer      
        else:            
            self.fez = self.faz + self.dauer 

        #print(f'{self.name=} FEZ gesetzt: {self.fez=}')


    def berechne_sez(self):
        # min SAZ des nachfolgers
        ...

    def berechne_saz(self):
        # SAZ - dauer
        ...

    def berechne_gesamt_puffer(self):
        # SAZ - FAZ
        ...

    def berechne_freier_puffer(self):
        # min FAZ des Nachfolgers - FEZ
        ...