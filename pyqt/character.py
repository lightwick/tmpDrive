from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QRect, QTimer

STEP_SIZE=2

class character:
    def __init__(self, parent, row, col, SpriteSheetPath, TimeInterval=50):
        self.parent = parent
        self.row_num = row
        self.col_num = col
        self.frame_x = 0
        self.frame_y = 0
        self.SpriteSheet = QPixmap(SpriteSheetPath)
        self.xDist = self.SpriteSheet.width()/self.col_num # sprite_width
        self.yDist = self.SpriteSheet.height()/self.row_num # sprite_height
        self.go = True
        
        self.timer = QTimer(self.parent)
        self.timer.setInterval(TimeInterval)
        self.timer.timeout.connect(self.timeout)
        self.timer.start()

            
    def timeout(self):
        self.CharSetNextFrame()
        self.parent.update()
    
    def CharSetNextFrame(self):
        self.frame_x += self.xDist
        if self.frame_x >= self.xDist*self.col_num:
            self.frame_x=0
        
class MainCharacter(character):
    def __init__(self, **kwargv):
        super().__init__(**kwargv)
        self.timer.stop()
        self.frame_y = 0
        
        # mid-point coordinate as 0,0
        self.CharX = 0
        self.CharY = 0
        
        self.pressedKey = None
        
        self.walkTimer=QTimer(self.parent)
        self.background_size = 50
        self.walkTimer.setInterval(15)
        self.walkTimer.timeout.connect(self.move)
        self.walkTimerCount=0
        
        self.AnimationTimer = QTimer(self.parent)
        self.AnimationTimer.setInterval(20)
        self.AnimationTimer.timeout.connect(self.movingAnimation)
        self.position = "down"
        
    def done(self): # just a place holder for now
        print("done")
        
    def draw(self, painter):
        painter.drawPixmap(self.parent.width()/2-self.xDist/2, self.parent.height()/2-self.yDist/2, self.SpriteSheet, self.frame_x, self.frame_y, self.xDist, self.yDist)
        
    def move(self):
        if self.walkTimerCount==0 or self.walkTimerCount%(self.background_size/STEP_SIZE)!=0:
            if self.pressedKey=="right":
                self.position="right"
                self.frame_y = self.yDist*7
                self.CharX += STEP_SIZE
            elif self.pressedKey=="left":
                self.position="left"
                self.frame_y = self.yDist*5
                self.CharX += -STEP_SIZE
            elif self.pressedKey=="up":
                self.position="up"
                self.frame_y = self.yDist * 6
                self.CharY += -STEP_SIZE
            elif self.pressedKey=="down":
                self.position="down"
                self.frame_y = self.yDist * 4
                self.CharY += STEP_SIZE
            self.parent.update()
            self.walkTimerCount+=1
        else:
            self.walkTimerCount=0
            self.walkTimer.stop()
            self.AnimationTimer.stop()
            
            self.frame_x = 0
            if self.frame_y >= self.yDist*4:
                self.frame_y -= self.yDist*4
            
    def movingAnimation(self):
        self.CharSetNextFrame()
        self.parent.update()
    
    '''
    def checkInput(self):
        if self.pressedKey != None:
            if self.pressedKey=="right":
                self.position="right"
                self.frame_y = self.yDist*7
                self.CharX += STEP_SIZE
            elif self.pressedKey=="left":
                self.position="left"
                self.frame_y = self.yDist*5
                self.CharX += -STEP_SIZE
            elif self.pressedKey=="up":
                self.position="up"
                self.frame_y = self.yDist * 6
                self.CharY += -STEP_SIZE
            elif self.pressedKey=="down":
                self.position="down"
                self.frame_y = self.yDist * 4
                self.CharY += STEP_SIZE
            
            if not self.AnimationTimer.isActive():
                self.AnimationTimer.start()
        self.parent.update()
        '''
        
    def keyPressEvent(self, event):
        if not self.walkTimer.isActive(): # if is not walking
            if event.key()==Qt.Key_Right:
                self.pressedKey="right"
            elif event.key()==Qt.Key_Left:
                self.pressedKey="left"
            elif event.key()==Qt.Key_Up:
                self.pressedKey="up"
            elif event.key()==Qt.Key_Down:
                self.pressedKey="down"
            
            self.walkTimer.start()
            self.AnimationTimer.start()
        
    def keyReleaseEvent(self, event):
        #self.walkTimer.stop()
        if not event.isAutoRepeat():
            self.frame_x = 0
            if self.frame_y >= self.yDist*4:
                self.frame_y -= self.yDist*4
        
class Monster(character):
    def __init__(self, **kwargv):
        super().__init__(**kwargv)              
        #DEBUG
        self.frame_y = 0
        self.count=0
        
        # relative to image
        self.CharX = 500
        self.CharY = 450
        
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
            
    def draw(self, painter):
        painter.drawPixmap(self.CharX-self.parent.link.CharX/self.parent.background.factor, self.CharY-self.parent.link.CharY/self.parent.background.factor, self.SpriteSheet, self.frame_x, self.frame_y, self.xDist, self.yDist)
        