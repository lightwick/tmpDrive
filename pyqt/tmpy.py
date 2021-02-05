from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer

import sys
import random

class myWidget(QtWidgets.QWidget):
    class character:
        def __init__(self, parent, row, col, SpriteSheetPath, TimeInterval=50):
            self.parent = parent
            self.row_num = row
            self.col_num = col
            self.frame_x = 0
            self.frame_y = 0
            self.SpriteSheet = QPixmap(SpriteSheetPath)
            self.xDist = self.SpriteSheet.width()/self.col_num
            self.yDist = self.SpriteSheet.height()/self.row_num
            self.CharX=500
            
            self.go = True
            
            self.timer = QTimer(self.parent)
            self.timer.setInterval(TimeInterval)
            self.timer.timeout.connect(self.timeout)
            self.timer.start()
            
        def draw(self, painter):
            painter.drawPixmap(self.CharX,585, self.SpriteSheet, self.frame_x, self.frame_y, self.xDist, self.yDist)
                
        def timeout(self):
            self.CharSetNextFrame()
            self.parent.update()

        def BackNForth(self):
            self.frame_x += self.xDist

            if self.go:
                self.frame_y = self.yDist*7
                self.CharX +=15
            else:
                self.frame_y = self.yDist*5
                self.CharX -=15
            if self.CharX > self.parent.width()-self.xDist:
                self.go=False
            if self.CharX<=0:
                self.go=True
                
            if self.frame_x >= self.xDist*self.col_num:
                self.frame_x=0
        
        def CharSetNextFrame(self):
            self.frame_x += self.xDist
            if self.frame_x >= self.xDist*self.col_num:
                self.frame_x=0
            
    class MainCharacter(character):
        def __init__(self, **kwargv):
            super().__init__(**kwargv)
            #self.timer.stop()
            self.frame_y = 0
            self.CharX = 0
            self.count = 0
        
        def keyPressEvent(self, event):
            if event.key()==Qt.Key_Right:
                self.frame_y = self.yDist*7
                self.CharX += 10
            elif event.key()==Qt.Key_Left:
                self.frame_y = self.yDist*5
                self.CharX -= 10
            elif event.key()==Qt.Key_Up:
                self.frame_y = self.yDist * 6
            elif event.key()==Qt.Key_Down:
                self.frame_y = self.yDist * 4
            
            self.CharSetNextFrame()

        def keyReleaseEvent(self, event):
            if not event.isAutoRepeat():
                print("released")
                self.frame_x = 0
                if self.frame_y >= self.yDist*4:
                    self.frame_y -= self.yDist*4
            
        def timeout(self):
            self.BackNForth()
            self.parent.update()
            
    class Monster(character):
        def __init__(self, **kwargv):
            super().__init__(**kwargv)              
            #DEBUG
            self.frame_y = 0
            self.count=0
            self.CharX = 500
        
        def CharSetNextFrame(self):
            self.frame_x += self.xDist
            #self.CharX +=5
            if self.frame_y==0 and self.frame_x >= self.xDist*5:
                self.frame_x=0
                self.count+=1
            elif self.frame_y==self.yDist*2 and self.frame_x >= self.xDist*8:
                self.frame_y=0
                self.frame_x=0
            
            if self.count==5 and self.frame_y!=self.yDist*2 and self.frame_x==0:
                self.count=0
                self.frame_y=self.yDist*2
                self.frame_x=0

            
    def __init__(self):
        super(myWidget,self).__init__()
        self.initCharacter()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setWindowTitle("walking animation test")
        self.resize(1500, 900)
    
    def initCharacter(self):
        # machine = QtCore.QStateMachine()
        self.frame_x=0
        
        #DEBUG
        self.count = 0
        self.monster = self.Monster(parent = self, row = 4, col = 8, SpriteSheetPath = "./img/monster.png", TimeInterval = 75)
        self.link = self.MainCharacter(parent = self, row = 8, col = 10, SpriteSheetPath = "./img/link.png", TimeInterval = 10)            
        
    def paintEvent(self, event): # when redrawn
        painter = QtGui.QPainter()
        painter.begin(self)
        pixmap = QPixmap("./img/bg.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
        self.link.draw(painter)
        self.monster.draw(painter)
    
    def keyPressEvent(self, event):
        self.link.keyPressEvent(event)
        self.update()
        
    def keyReleaseEvent(self, event):
        self.link.keyReleaseEvent(event)
        self.update()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = myWidget()
    sys.exit(app.exec_())
