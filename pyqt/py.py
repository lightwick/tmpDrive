from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer

import sys

class myWidget(QtWidgets.QWidget):
    def __init__(self):
        super(myWidget,self).__init__()
        self.initCharacter()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setWindowTitle("walking animation test")
        self.resize(900, 600)
    
    def initCharacter(self):
        # machine = QtCore.QStateMachine()
        self.col_num=10
        self.row_num=8
        self.frame_x=0
        self.frame_y=0
        self.SpriteSheet = QPixmap("./img/link.png")
        self.xDist = self.SpriteSheet.width()/self.col_num
        self.yDist = self.SpriteSheet.height()/self.row_num
        
        self.CharX = 0
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timeout)
    
    def CharSetNextFrame(self):
        self.frame_x += self.xDist
        if self.frame_x >= self.xDist*self.col_num:
            self.frame_x=0
            
    def timeout(self):
        self.CharSetNextFrame()
        self.update()
        
    def paintEvent(self, event): # when redrawn
        painter = QtGui.QPainter()
        painter.begin(self)
        pixmap = QPixmap("./img/bg.jpg")
        painter.drawPixmap(self.rect(), pixmap)
        
        painter.drawPixmap(self.CharX,360, self.SpriteSheet, self.frame_x, self.frame_y, self.xDist, self.yDist)
    
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Right:
            self.frame_y = self.yDist*7
            self.CharX += 5
        elif event.key()==Qt.Key_Left:
            self.frame_y = self.yDist*5
            self.CharX -= 5
        elif event.key()==Qt.Key_Up:
            self.frame_y = self.yDist * 6
        elif event.key()==Qt.Key_Down:
            self.frame_y = self.yDist * 4
        
        self.CharSetNextFrame()
        
        self.update()
    
    def keyReleaseEvent(self, event):
        if not event.isAutoRepeat():
            print("released")
            self.frame_x = 0
            if self.frame_y >= self.yDist*4:
                self.frame_y -= self.yDist*4
            self.update()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = myWidget()
    sys.exit(app.exec_())