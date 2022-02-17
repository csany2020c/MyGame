import math
import game

class Fuzetbol(game.scene2d.MyMathFunction):

    def f(self, x : float) -> float:
        return 2*x*x-5*x-3

class X2(game.scene2d.MyMathFunction):

    def f(self, x: float) -> float:
        return x * x


class X3(game.scene2d.MyMathFunction):

    def f(self, x: float) -> float:
        return x*x*x


class sin(game.scene2d.MyMathFunction):

    def f(self, x: float) -> float:
        return math.sin(x)


#https://mathworld.wolfram.com/FourierSeriesSquareWave.html
class square(game.scene2d.MyMathFunction):

    def __init__(self, color=(255, 255, 255)) -> None:
        super().__init__(color)
        self.wavelength: float = math.pi * 2
        self.iterations: int = 20

    def f(self, x: float) -> float:
        sum: float = 0
        for n in range (1, 1 + self.iterations * 2, 2):
            sum += 1/float(n)*math.sin(n * math.pi * x / self.wavelength * 2)
        y = 4 / math.pi * sum
        return y

class masodfoku(game.scene2d.MyMathFunction):

    def f(self, x: float) -> float:
        return 3*x*x + 7*x + 4


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        m = game.scene2d.MyMathGraphStage()
        m.add_math_function(masodfoku())
        # m.add_math_function(Fuzetbol(color=(200, 100, 50)))
        # m.add_math_function(X2(color=(200, 100, 250)))
        # m.add_math_function(X3(color=(200, 200, 250)))
        # m.add_math_function(sin(color=(100, 200, 250)))
        # m.add_math_function(square())
        self.add_stage(m)


class Game(game.scene2d.MyGame):
    def __init__(self, width: int = 1280, height: int = 720, autorun: bool = False, autosize: bool = False,
                 debug: bool = False):
        super().__init__(width, height, autorun, autosize, debug)
        self.screen=Screen()

Game().run()
