# -*- coding: utf-8 -*-
# @time    : 2023/8/5 21:34
# @author  : w-xin
# @file    : 25_QPainterDrawSinDemo.py
# @software: PyCharm

"""
QPainter 用像素点绘制正弦曲线

绘制两个周期的正弦函数

drawPoint 绘制像素点
drawPoint(x, y)
"""
import sys, math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QPainterDrawSinDemo(QWidget):

    def __init__(self):

        super(QPainterDrawSinDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QPainterDrawSin Demo')
        self.resize(300, 300)


    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.blue)
        size = self.size()  # 获得窗口的尺寸

        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            painter.drawPoint(x, y)

        painter.end()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QPainterDrawSinDemo()
    main.show()
    sys.exit(app.exec_())
