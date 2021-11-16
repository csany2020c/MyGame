from game.scene2d import MyBaseActor, MyLifeCycles, MyGame
from game.simpleworld import MyRectangle


class MyCamera(MyLifeCycles):

    def __init__(self, width: float, height: float) -> None:
        self._x: float = 0
        self._y: float = 0
        self._tracking_speed: float = 0.1
        self._w: float = width
        self._h: float = height
        self._track_window: MyRectangle = MyRectangle(self._w * 0.20, self._h * 0.20,
                                         self._w - self._w * 0.20,
                                         self._h - self._h * 0.20)
        self._track: 'MyBaseActor' = None
        # TODO: 3 db ötösért, működő forgatás és zoom!!!
        # self._zoom: float = 1
        # self._rotatate: float = 0
        super().__init__()

    def set_tracking_window(self, percent_left: float, percent_top: float, percent_right: float, percent_bottom: float):
        self._track_window = MyRectangle(self._w * percent_left, self._h * percent_top,
                                         self._w - self._w * percent_right,
                                         self._h - self._h * percent_bottom)

    def set_x(self, x: float):
        self._x = x
        self._track = None

    def set_y(self, y: float):
        self._y = y
        self._track = None

    def get_x(self) -> float:
        return self._x

    def get_y(self) -> float:
        return self._y

    def set_tracking(self, track_actor: MyBaseActor):
        self._track = track_actor

    def get_tracking(self) -> MyBaseActor:
        return self._track

    def set_tracking_speed(self, speed: float):
        self._tracking_speed = speed

    def get_tracking_speed(self) -> float:
        return self._tracking_speed

    def act(self, delta_time: float):
        # super().act(delta_time)
        if self._track is not None:

            l = self._track.x - self._x - self._track_window.getX()
            if l < 0:
                self._x += l * self._tracking_speed

            r = self._track.x - self._x - self._track_window.getWidth() + self._track.width
            if r > 0:
                self._x += r * self._tracking_speed

            t = self._track.y - self._y - self._track_window.getY()
            if t < 0:
                self._y += t * self._tracking_speed

            b = self._track.y - self._y - self._track_window.getHeight() + self._track.width
            if b > 0:
                self._y += b * self._tracking_speed

    x: float = property(get_x, set_x)
    y: float = property(get_y, set_y)
    tracking_speed: float = property(get_tracking_speed, set_tracking_speed)
    tracking: 'MyBaseActor' = property(get_tracking, set_tracking)
