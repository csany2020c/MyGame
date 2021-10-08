from SzBKStage import *

class Esikaeso(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(EsosStage())


class Sutanap(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(NaposStage())


class Esikaho(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(HavasStage())

class Esikmindketo(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        self.add_stage(KettosStage())