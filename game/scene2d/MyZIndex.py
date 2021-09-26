from typing import List


class MyZIndex:

    auto_z_index: int = 0

    def __init__(self) -> None:
        MyZIndex.auto_z_index += 100
        self._z_index = MyZIndex.auto_z_index
        print(self.__str__() + str(self._z_index) + " Z index")

    def set_z_index(self, zindex: int):
        self._z_index = zindex

    def get_z_index(self) -> int:
        return self._z_index

#    def __eq__(self, other: 'MyZIndex') -> bool:
#        return self._z_index == other._z_index

#    def __ne__(self, other: 'MyZIndex') -> bool:
#        return self._z_index != other._z_index

    def __lt__(self, other: 'MyZIndex') -> bool:
        return self._z_index < other._z_index

    def __gt__(self, other: 'MyZIndex') -> bool:
        return self._z_index > other._z_index

    z: int = property(get_z_index, set_z_index)
    z_index: int = property(get_z_index, set_z_index)
