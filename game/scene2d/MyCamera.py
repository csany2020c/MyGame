from game.scene2d import MyBaseActor, MyLifeCycles


class MyCamera(MyLifeCycles):

    def __init__(self) -> None:
        self._x: float = 0
        self._y: float = 0
        self._track: 'MyBaseActor' = None
        # self.zoom: float = 1
        # self.rotatate: float = 0
        super().__init__()

    def set_x(self, x: int):
        self._x = x
        self._track = None

    def set_y(self, y: int):
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

    def act(self, delta_time: float):
        # super().act(delta_time)
        if self._track is not None:
            self._x = self._track.x
            self._y = self._track.y

    x: float = property(get_x, set_x)
    y: float = property(get_y, set_y)
    tracking: 'MyBaseActor' = property(get_tracking, set_tracking)
