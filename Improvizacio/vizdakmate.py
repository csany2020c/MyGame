from typing import List

class Doga:
    def __init__(self) -> None:
        super().__init__()
        self.pontszam = int
        self.osszpontszam: int = 40


        self.osszpontszam = input("Kérem az összpontszámot")
        self.pontszam = input("Az ön pontszáma: ")
        self.szazalek: float = self.pontszam / self.osszpontszam * 100.0
        print("Az elért százalék:" + str(self.szazalek))



Doga()