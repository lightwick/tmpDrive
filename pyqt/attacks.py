from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer

class attackParticle:
    main = None
    def __init__(self, parent,  mainChar):
        self.img = QPixmap("./img/heart.webp")
        self.x = 0
        attackParticle.main = mainChar
        
        # could seperate increment function by which direction it should be going
        # could cut down 1 Hz / 20ms, which isn't alot
        self.direction = mainChar.position
        
        self.parent = parent
        
        self.timer=QTimer(self.parent)
        self.timer.setInterval(20)
        self.timer.timeout.connect(self.increment)
        self.timer.start()
        
    def draw(self, painter):
        painter.drawPixmap(self.parent.width()/2+self.x, self.parent.height()/2, 20, 20, self.img)
        
    def increment(self):
        if self.direction=="right":
            self.x+=10
        elif self.direction=="left":
            self.x-=10
        self.parent.update()