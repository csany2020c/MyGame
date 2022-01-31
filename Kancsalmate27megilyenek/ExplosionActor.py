from typing import List

import game
from pygame import mixer
from game.scene2d import MyTickTimer,MyOneTickTimer
from game.scene2d.MyStage import *


class ExplosionActor(game.scene2d.MyActor):

        def __init__(self,x:int,y:int,dmg:int):
            super().__init__("tile000.png")
            self.dmg = dmg
            self.width = 128
            self.height = 124
            self.x = x
            self.y = y
            self.iStr:str = ""
            self.i = 0
            self.imageList: List['str'] = list()
            for i in range(0,72):
                if i < 10:
                    self.iStr = "tile00" + str(i) + ".png"
                elif i>=10:
                    self.iStr = "tile0" + str(i) + ".png"
                self.imageList.append(self.iStr)
            self.timer = MyTickTimer(func=self.timeHandling2, interval=0.03, start_delay=3, repeat=True)
            self.interval = MyOneTickTimer(self.delaySound,interval=3)
            self.add_timer(self.timer)
            self.add_timer(self.interval)
        def delaySound(self,sender):
            mixer.init()
            mixer.music.load("explosion.wav")
            mixer.music.set_volume(0.3)
            mixer.music.play()
        def timeHandling2(self,sender):
            if self.image_url == self.imageList[0]:
                self.image_url = self.imageList[1]
            elif self.image_url == self.imageList[1]:
                self.image_url = self.imageList[2]
            elif self.image_url == self.imageList[2]:
                self.image_url = self.imageList[3]
            elif self.image_url == self.imageList[3]:
                self.image_url = self.imageList[4]
            elif self.image_url == self.imageList[4]:
                self.image_url = self.imageList[5]
            elif self.image_url == self.imageList[5]:
                self.image_url = self.imageList[6]
            elif self.image_url == self.imageList[6]:
                self.image_url = self.imageList[7]
            elif self.image_url == self.imageList[7]:
                self.image_url = self.imageList[8]
            elif self.image_url == self.imageList[8]:
                self.image_url = self.imageList[9]
            elif self.image_url == self.imageList[9]:
                self.image_url = self.imageList[10]
            elif self.image_url == self.imageList[10]:
                self.image_url = self.imageList[11]
            elif self.image_url == self.imageList[11]:
                self.image_url = self.imageList[12]
            elif self.image_url == self.imageList[12]:
                self.image_url = self.imageList[13]
            elif self.image_url == self.imageList[13]:
                self.image_url = self.imageList[14]
            elif self.image_url == self.imageList[14]:
                self.image_url = self.imageList[15]
            elif self.image_url == self.imageList[15]:
                self.image_url = self.imageList[16]
            elif self.image_url == self.imageList[16]:
                self.image_url = self.imageList[17]
            elif self.image_url == self.imageList[17]:
                self.image_url = self.imageList[18]
            elif self.image_url == self.imageList[18]:
                self.image_url = self.imageList[19]
            elif self.image_url == self.imageList[19]:
                self.image_url = self.imageList[20]
            elif self.image_url == self.imageList[20]:
                self.image_url = self.imageList[21]
            elif self.image_url == self.imageList[21]:
                self.image_url = self.imageList[22]
            elif self.image_url == self.imageList[22]:
                self.image_url = self.imageList[23]
            elif self.image_url == self.imageList[23]:
                self.image_url = self.imageList[24]
            elif self.image_url == self.imageList[24]:
                self.image_url = self.imageList[25]
            elif self.image_url == self.imageList[25]:
                self.image_url = self.imageList[26]
            elif self.image_url == self.imageList[26]:
                self.image_url = self.imageList[27]
            elif self.image_url == self.imageList[27]:
                self.image_url = self.imageList[28]
            elif self.image_url == self.imageList[28]:
                self.image_url = self.imageList[29]
            elif self.image_url == self.imageList[29]:
                self.image_url = self.imageList[30]
            elif self.image_url == self.imageList[30]:
                self.image_url = self.imageList[31]
            elif self.image_url == self.imageList[31]:
                self.image_url = self.imageList[32]
            elif self.image_url == self.imageList[32]:
                self.image_url = self.imageList[33]
            elif self.image_url == self.imageList[33]:
                self.image_url = self.imageList[34]
            elif self.image_url == self.imageList[34]:
                self.image_url = self.imageList[35]
            elif self.image_url == self.imageList[35]:
                self.image_url = self.imageList[36]
            elif self.image_url == self.imageList[36]:
                self.image_url = self.imageList[37]
            elif self.image_url == self.imageList[37]:
                self.image_url = self.imageList[38]
            elif self.image_url == self.imageList[38]:
                self.image_url = self.imageList[39]
            elif self.image_url == self.imageList[39]:
                self.image_url = self.imageList[40]
            elif self.image_url == self.imageList[40]:
                self.image_url = self.imageList[41]
            elif self.image_url == self.imageList[41]:
                self.image_url = self.imageList[42]
            elif self.image_url == self.imageList[42]:
                self.image_url = self.imageList[43]
            elif self.image_url == self.imageList[43]:
                self.image_url = self.imageList[44]
            elif self.image_url == self.imageList[44]:
                self.image_url = self.imageList[45]
            elif self.image_url == self.imageList[45]:
                self.image_url = self.imageList[46]
            elif self.image_url == self.imageList[46]:
                self.image_url = self.imageList[47]
            elif self.image_url == self.imageList[47]:
                self.image_url = self.imageList[48]
            elif self.image_url == self.imageList[48]:
                self.image_url = self.imageList[49]
            elif self.image_url == self.imageList[49]:
                self.image_url = self.imageList[50]
            elif self.image_url == self.imageList[50]:
                self.image_url = self.imageList[51]
            elif self.image_url == self.imageList[51]:
                self.image_url = self.imageList[52]
            elif self.image_url == self.imageList[52]:
                self.image_url = self.imageList[53]
            elif self.image_url == self.imageList[53]:
                self.image_url = self.imageList[54]
            elif self.image_url == self.imageList[54]:
                self.image_url = self.imageList[55]
            elif self.image_url == self.imageList[55]:
                self.image_url = self.imageList[56]
            elif self.image_url == self.imageList[56]:
                self.image_url = self.imageList[57]
            elif self.image_url == self.imageList[57]:
                self.image_url = self.imageList[58]
            elif self.image_url == self.imageList[58]:
                self.image_url = self.imageList[59]
            elif self.image_url == self.imageList[59]:
                self.image_url = self.imageList[60]
            elif self.image_url == self.imageList[60]:
                self.image_url = self.imageList[61]
            elif self.image_url == self.imageList[61]:
                self.image_url = self.imageList[62]
            elif self.image_url == self.imageList[62]:
                self.image_url = self.imageList[63]
            elif self.image_url == self.imageList[63]:
                self.image_url = self.imageList[64]
            elif self.image_url == self.imageList[64]:
                self.image_url = self.imageList[65]
            elif self.image_url == self.imageList[65]:
                self.image_url = self.imageList[66]
            elif self.image_url == self.imageList[66]:
                self.image_url = self.imageList[67]
            elif self.image_url == self.imageList[67]:
                self.image_url = self.imageList[68]
            elif self.image_url == self.imageList[68]:
                self.image_url = self.imageList[69]
            elif self.image_url == self.imageList[69]:
                self.image_url = self.imageList[70]
            elif self.image_url == self.imageList[70]:
                self.image_url = self.imageList[71]
            self.width = 128
            self.height = 124

class RedCircle(game.scene2d.MyActor):

    def __init__(self,x:int,y:int):
        super().__init__("redcircle.png")
        self.x = x
        self.y = y
        self.width = 128
        self.height = 124
