class Ventilator:
    def __init__(self):
        self.maxzaj = 60
        self.magassag = 140
        self.fogyasztas = 70
        self.ara = 32500


sajatventilator = Ventilator()
sajatventilator.magassag = 140
sajatventilator.fogyasztas = 50
sajatventilator.ara = 10700

print(sajatventilator.maxzaj)
