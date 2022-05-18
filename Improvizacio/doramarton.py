from typing import TextIO
from typing import List

class madar:
    def __init__(self):
        super().__init__()
        self.sebesseg: int
        self.enekes: bool
        self.ropkepes: bool
        self.ragadozo: bool


solyom = madar
solyom.sebesseg = 360
solyom.enekes = True
solyom.ropkepes = True
solyom.ragadozo = True

print(solyom.enekes)