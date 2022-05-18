from typing import TextIO
from typing import List

class Csuka:
    def __init__(self):
        super().__init__()
        self.meret:int = 42
        self.femstoplis:bool = True
        self.marka:str = "Nike"
        self.szin:str = "Fekete"


encsukam = Csuka()
encsukam.meret = 44
encsukam.femstoplis = False
encsukam.marka = "Adidas"
encsukam.szin = "Feher"
print(encsukam.femstoplis)



