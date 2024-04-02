from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QPoint, QRect, QRectF
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QTextOption, QFont, QCursor
from loguru import logger

# This class is a subclass of QLabel and is used to display images on the GUI
class Image(QtWidgets.QLabel):
    def __init__(self, parent):
        super(Image, self).__init__(parent=parent)
        self.setPixmap(QtGui.QPixmap(":/Icons/whiteBG.jpg"))
        self.img = None
        self.image = QPixmap(":/Icons/whiteBG.jpg")
        self.begin = QPoint()
        self.end = QPoint()
        self.flag = False
        self.pages = {}
        self.connectDict = {}
        self.translated = {}
        self.japanese = {}
        self.color = {
            "White" : QColor(255, 255, 255),
            "Black" : QColor(0, 0, 0),
            "Red" : QColor(255, 0, 0),
            "Blue" : QColor(0, 0, 255),
            "Green" : QColor(0, 255, 0)
        }
        self.bg = "White"
        self.textColor = "Red"
        self.fontNum = 6