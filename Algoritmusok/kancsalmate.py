class igen:
    def __init__(self) -> None:
        super().__init__()
        self.osztok()
        print(self.prim())
    def faktorialis(self):
        x = 1
        a = int(input())
        for i in range(1, a+1):
            x = x * i
        print(x)

    def osztok(self):
        self.lista = list()
        szam = int(input())
        for i in range(1, szam + 1):
            if szam % i == 0:
                self.lista.append(i)
        print(self.lista)

    def prim(self):
        prim = False
        if len(self.lista) == 2:
            prim = True
            return prim


igen()