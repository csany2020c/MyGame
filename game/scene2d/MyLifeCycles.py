class MyLifeCycles:

    def create(self):
        if __debug__:
            print(str(self) + " Create")

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

    def dispose(self):
        if __debug__:
            print(str(self) + " Dispose")

