class MyLifeCycles:

    def show(self):
        if __debug__:
            print(str(self) + " Show")

    def act(self, delta_time: float):
        pass

    def draw(self):
        pass

    def hide(self):
        if __debug__:
            print(str(self) + " Hide")
