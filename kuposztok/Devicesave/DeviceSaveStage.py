import game
import pygame
import socket


class DeviceSaveStage(game.scene2d.MyStage):
    def __init__(self):
        super().__init__()
        self.devicename = socket.gethostname()
        self.devicewrite()
        self.namelabel = game.scene2d.MyLabel("")
        self.namelabel.set_color(255, 255, 255)
        self.add_actor(self.namelabel)

    def devicewrite(self):
        with open('../kuposztok/Save/devices.txt', 'r+') as device:
            self.bemenet = input()
            self.alldevice = str(device.readline())
            self.deviceben = self.alldevice
            if self.deviceben == self.devicename:
                device.write("" + '\t' + str(self.bemenet))
            if self.deviceben == self.devicename + str(self.bemenet):
                device.write("" + '\t' + str(self.bemenet))
            if self.deviceben != self.devicename:
                device.write('\n' + str(self.devicename))
            device.close()

    def act(self, delta_time: float):
        super().act(delta_time)
        self.namelabel.set_text(self.bemenet)
