from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer
from character import character, STEP_SIZE

class attackParticle:
    main = None
    background = None
    def __init__(self, parent,  mainChar):
        self.img = QPixmap("./img/heart.webp")
        self.x = 0
        self.y = 0
        attackParticle.main = mainChar
        
        # could seperate increment function by which direction it should be going
        # could cut down 1 Hz / 20ms, which isn't alot
        self.direction = mainChar.position
        
        self.parent = parent
        
        self.timer=QTimer(self.parent)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.reposition)
        self.timer.start()
        
    def draw(self, painter):
        painter.drawPixmap(self.parent.width()/2+self.x, self.parent.height()/2+self.y, 20, 20, self.img)
        
    def reposition(self):
        # have to note that this code only works becuase
        # the timer interval for attackParticle.reposition is the same as the key input busy waiting for character movement
        if self.main.pressedKey=="right":
            self.x -= STEP_SIZE/self.background.factor
        elif self.main.pressedKey=="left":
            self.x += STEP_SIZE/self.background.factor
        elif self.main.pressedKey=="up":
            self.y += STEP_SIZE/self.background.factor
        elif self.main.pressedKey=="down":
            self.y -= STEP_SIZE/self.background.factor
        # end condition
        
        if self.direction=="right":
            self.x+=10
        elif self.direction=="left":
            self.x-=10
        elif self.direction=="up":
            self.y-=10
        elif self.direction=="down":
            self.y+=10
        self.parent.update()