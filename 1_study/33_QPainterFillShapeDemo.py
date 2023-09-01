# -*- coding: utf-8 -*-
# @time    : 2023/8/6 10:25
# @author  : w-xin
# @file    : 33_QPainterFillShapeDemo.py
# @software: PyCharm

"""
QPainter 填充图形区域
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPainterFillShapeDemo(QWidget):

    def __init__(self):

        super(QPainterFillShapeDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QPainterFillShape Demo')
        self.resize(500, 600)


    def paintEvent(self, event):

        painter = QPainter(self)
        painter.begin(self)

        # 创建画刷对象
        brush = QBrush(Qt.SolidPattern)
        # 设置画刷
        painter.setBrush(brush)
        # 填充
        painter.drawRect(QRect(10, 15, 90, 60))
        
        # 再设置一个画刷
        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(QRect(130, 15, 90, 60))

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(QRect(250, 15, 90, 60))

        brush = QBrush(Qt.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(QRect(10, 105, 90, 60))

        brush = QBrush(Qt.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(QRect(130, 105, 90, 60))

        painter.end()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QPainterFillShapeDemo()
    main.show()
    sys.exit(app.exec_())
