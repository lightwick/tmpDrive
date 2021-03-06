from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer
from background import background
from character import *
from attacks import *

import sys
import random

class myWidget(QWidget):
    def __init__(self):
        super(myWidget,self).__init__()
        self.attack=[]
        self.initCharacter()
        self.initUI()
        self.initBackground()
        self.show()
        
    def initBackground(self):
        bgPath="./img/tile.png"
        tmp = QPixmap(bgPath)
        self.background = background(self, bgPath, tmp.width()/2, tmp.height()/2, 1/3)
        attackParticle.background = self.background
        
    def initUI(self):
        self.setWindowTitle("walking animation test")
        self.setFixedSize(1500, 900)
        
    
    def initCharacter(self):
        # machine = QtCore.QStateMachine()
        self.monster = Monster(parent = self, row = 4, col = 8, SpriteSheetPath = "./img/monster.png", TimeInterval = 75)
        self.link = MainCharacter(parent = self, row = 8, col = 10, SpriteSheetPath = "./img/link.png", TimeInterval = 10)            
        
    def paintEvent(self, event): # when redrawn
        painter = QtGui.QPainter()
        painter.begin(self)
        self.background.draw(painter)
        self.link.draw(painter)
        self.monster.draw(painter)
        for i in self.attack:
            i.draw(painter)
            
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Control:
            _attack = attackParticle(self, self.link)
            self.attack.append(_attack)
        self.link.keyPressEvent(event)
        self.update()
    
    def keyReleaseEvent(self, event):
        self.link.keyReleaseEvent(event)
        self.update()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = myWidget()
    sys.exit(app.exec_())