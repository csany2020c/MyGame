class Ventilator:
    def __init__(self):
        self.maxzaj = "60Db,"
        self.magassag = "140cm,"
        self.fogyasztas = "70W,"
        self.ara = "32500ft"

    def __str__(self) -> str:
        return "{a} {b} {c} {d}".format(a=self.maxzaj, b=self.magassag, c=self.fogyasztas, d=self.ara)


sajatventilator1 = Ventilator()
sajatventilator1.magassag = "140cm,"
sajatventilator1.fogyasztas = "50W,"
sajatventilator1.ara = "10700ft"


sajatventilator2 = Ventilator()
sajatventilator2.maxzaj = "75Db,"
sajatventilator2.magassag = "170cm,"
sajatventilator2.fogyasztas = "70W,"
sajatventilator2.ara = "36000ft"


sajatventilator3 = Ventilator()
sajatventilator3.maxzaj = "40Db,"
sajatventilator3.magassag = "110cm,"
sajatventilator3.fogyasztas = "35W,"
sajatventilator3.ara = "8000ft"


sajatventilator4 = Ventilator()


def asda():
    asd: int = int(input("maxzaj?"))
    if asd == 40:
        print(sajatventilator3)
    elif asd == 60:
        print(sajatventilator3)
        print(sajatventilator1)
    elif asd == 75:
        print(sajatventilator3)
        print(sajatventilator1)
        print(sajatventilator2)


asda()
