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


class rugo(game.scene2d.MyMathFunction):

    def f(self, t: float) -> float:

        x0 = 1 # A kitérés kezdeti értéke (m)
        v0 = 10 # Kezdeti sebesség (m/s)


        c = 0.82 # Csillapítási tényező, Damping ratio (konstans érték)
        k = 20 # Rugómerevség (N/m) Stiffness
        m = 5  # Tömeg (N) mass
        f = 1  # Frekvancia (Hz)

        zeta = c / (2 * math.sqrt(k * m)) # Csillapítási faktor
        # \zeta < 1(Underdamped),
        # \zeta = 1(Critically Damped),
        # \zeta > 1(Overdamped).

        sqrt1ms2 = math.sqrt(1 - math.pow(zeta, 2))

        p = sqrt1ms2 * f # Csillapított sajátfrekvencia (Hz)
        omegak = 2 * math.pi * p;

        # https://engcourses-uofa.ca/books/vibrations-and-sound/damped-free-vibrations-of-single-degree-of-freedom-systems/free-vibrations-of-a-damped-spring-mass-system/

        return 0 if t < 0 else \
            math.pow(math.e, -zeta * omegak * t) * \
            (((v0 + zeta * omegak * x0) / (sqrt1ms2 * omegak)) * math.sin(sqrt1ms2 * omegak * t) +
             x0 * math.cos(sqrt1ms2 * omegak * t))


class Screen(game.scene2d.MyScreen):

    def __init__(self):
        super().__init__()
        m = game.scene2d.MyMathGraphStage()
        m.add_math_function(rugo())
        # m.add_math_function(masodfoku())
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

# Game().run()
