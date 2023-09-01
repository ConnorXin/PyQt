# -*- coding: utf-8 -*-
# @time    : 2023/8/5 21:19
# @author  : w-xin
# @file    : 29_QPainterDrawTextDemo.py
# @software: PyCharm

"""
PyQt5 的绘图 API

能够绘制
1 文本
2 各种图形  直线 点 椭圆 弧线 扇形 多边形等
3 图像

QPainter 绘图流程
painter = QPainter()
painter.begin()

painter.end()

注意 必须在 paintEvent 事件方法中绘制各种元素
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPainterDrawTextDemo(QWidget):

    def __init__(self):

        super(QPainterDrawTextDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QPainterDrawText Demo')
        self.resize(800, 200)

        self.text = 'Python Hello 入门到精通'


    def paintEvent(self, event):

        painter = QPainter(self)
        painter.begin(self)

        painter.setPen(QColor('#63EBE9'))  # 设置画笔以及颜色
        painter.setFont(QFont('SimSun', 25))

        painter.drawText(event.rect(), Qt.AlignCenter, self.text)

        painter.end()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QPainterDrawTextDemo()
    main.show()
    sys.exit(app.exec_())