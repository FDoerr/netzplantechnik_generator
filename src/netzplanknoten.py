

class Netzplanknoten():

    def __init__(
                self,
                name:str,
                dauer:int,
                direkte_nachfolger:list = None,
                direkte_vorgaenger:list = None
                ) -> None:
        
        self.name:  str = name 
        self.dauer: int = dauer
        self.direkte_nachfolger: list[str] = direkte_nachfolger
        self.direkte_vorgaenger: list[str] = []

        self.faz: int|None = None # TODO: Direkt berechnen
        self.fez: int|None = None # TODO: Direkt berechnen

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
        ...   

    def berechne_fez(self):
        # faz + dauer
        ...

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