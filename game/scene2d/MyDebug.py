class MyDebug:

    def __init__(self) -> None:
        self._debug: bool = False

    def set_debug(self, debug: bool):
        self._debug = debug

    def get_debug(self) -> bool:
        return self._debug

    debug: bool = property(get_debug, set_debug)
