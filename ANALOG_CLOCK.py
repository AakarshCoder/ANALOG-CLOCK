#Importing Libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore , QtGui
from PyQt5.QtGui import*
from PyQt5.QtCore import*
import sys

#creating class clock
class Clock(QMainWindow):
    #constructor
    def __init__(self):
        super().__init__()
        

        #creating timer object
        timer=QTimer(self)

        #giving action to timer
        timer.timeout.connect(self.update)
        #setting timer miliseconds
        timer.start(1000)
        #window title 
        self.setWindowTitle("Analog Clock")
        #setting windows geometry
        self.setGeometry(200,200,300,300)
        #background
        self.setStyleSheet("background : purple;")
        #hour hand
        self.hPointer = QtGui.QPolygon([QPoint(6,7),
                                      QPoint(-6,7),
                                      QPoint(0,-50)])
        #minute hand
        self.mPointer = QPolygon([QPoint(6,7),
                                QPoint(-6,7),
                                QPoint(0,-70)])
        #second hand
        self.sPointer = QPolygon([QPoint(1,1),
                                QPoint(-1,1),
                                QPoint(0,-90)])
        #color
        self.bColor= Qt.yellow
        self.sColor= Qt.red


    def paintEvent(self,event):
        #setting width and height
        rec = min(self.width(), self.height())
        #curent time
        tik = QTime.currentTime()
        #painter object
        painter= QPainter(self)
        def drawPointer(color,rotation, pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2, self.height()/2)
        painter.scale(rec/200, rec/200)
        painter.setPen(QtCore.Qt.NoPen)
        drawPointer(self.bColor,(30*(tik.hour()+tik.minute()/60)),self.hPointer)
        drawPointer(self.bColor,(6*(tik.minute()+tik.second()/60)),self.mPointer)
        drawPointer(self.sColor,(6*tik.second()),self.sPointer)

        painter.setPen(QPen(self.bColor))
        for i in range(0,60):
            if(i%5)==0:
                painter.drawLine(87,0,97,0)
            painter.rotate(6)
        painter.end()
#main code
if __name__== '__main__':
    app= QApplication(sys.argv)
    #creating clock object
    win = Clock()
#show
win.show()
exit(app.exec_())












