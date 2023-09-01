# -*- coding: utf-8 -*-
# @time    : 2023/8/5 21:45
# @author  : w-xin
# @file    : 31_QPainterDrawVariousLinesDemo.py
# @software: PyCharm

"""
QPainter 绘制不同类型的直线
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QPainterDrawVariousLinesDemo(QWidget):

    def __init__(self):

        super(QPainterDrawVariousLinesDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.resize(300, 450)
        self.setWindowTitle('QPaintDrawVariousLines Demo')


    def paintEvent(self, event):

        painter = QPainter()
        painter.begin(self)

        # Qt.red: 画笔颜色
        # 3: 画笔粗细
        # Qt.SolidLine: 画笔类型为实线
        pen = QPen(Qt.red, 3, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 40, 260, 40)

        # 虚线
        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 80, 260, 80)

        # 长短点横线
        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 260, 120)

        # 点线
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 160, 260, 160)

        # 自定义
        pen.setStyle(Qt.CustomDashLine)
        # 设置线的模式
        pen.setDashPattern([1, 4, 5, 4])
        painter.setPen(pen)
        painter.drawLine(20, 200, 260, 200)

        painter.end()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QPainterDrawVariousLinesDemo()
    main.show()
    sys.exit(app.exec_())