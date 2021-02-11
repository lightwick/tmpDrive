from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer

class background:
    def __init__(self, parent, path, initX, initY, factor):
        self.factor=factor
        self.pixmap=QPixmap(path)
        self.parent=parent
        self.x = initX
        self.y = initY
        self.width=parent.width()*factor
        self.height=parent.height()*factor
        
    def draw(self, painter):
        painter.drawPixmap(self.parent.rect(), self.pixmap, 
                           QRect(self.x-self.width/2+self.parent.link.CharX, 
                                 self.y-self.height/2+self.parent.link.CharY, 
                                 self.width, self.height))
        