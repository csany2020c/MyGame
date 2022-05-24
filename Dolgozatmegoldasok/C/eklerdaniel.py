class Barlang:

    def __init__(self, parse: str):
        darablás: list[str] = parse.strip().split("\t")
        self.nev: str = darablás[1]
        self.hossz: float = float(darablás[2])
        self.kit: float = float(darablás[3])
        self.mely: float = float(darablás[4])
        self.mag: float = float(darablás[5])
        self.tel: str = darablás[1]

        def __str__(self) -> str:
            return "{nev}\t{hossz}\t{kit}\t {mely}\t{mag}\t{tel}".format(nev=self.het, hossz=self.hossz, kit=self.kit, mely = self.mely, mag = self.mag, tel = self.tel)
