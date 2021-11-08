import string
from typing import TextIO
from typing import List


class Fajlbeolvasas:

    def __init__(self):
        szoveg: TextIO = open("!_Spec/orvosi_nobeldijak.txt", "r")
        content: str = szoveg.read()
        szoveg.close()
        print(content)
        """szovegketo: List['str'] = szoveg.split(" ")
        print(szovegketo)"""

Fajlbeolvasas()
