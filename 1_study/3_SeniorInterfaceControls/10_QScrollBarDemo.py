# -*- coding: utf-8 -*-
# @time    : 2023/10/28 12:31
# @file    : 10_QScrollBarDemo.py
# @software: PyCharm

"""
QScrollBar 滚动条控件
作用:
1 通过滚动条可以通过滑动控制值的变化 从而可以控制某些组件状态的变化
2 通过滚动条值的变化控制控件位置的变化
"""
import sys

from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import *


class QScrollBarDemo(QWidget):

    def __init__(self):

        super(QScrollBarDemo, self).__init__()
        self.setWindowTitle('QScrollBar Demo')

        hbox = QHBoxLayout()
        self.label = QLabel('拖动滚动条改变文本颜色')  # 控制文本颜色和位置

        hbox.addWidget(self.label)

        # 创建滚动条控件 以改变控件颜色
        self.scrollbar_1 = QScrollBar()
        self.scrollbar_1.setMaximum(255)  # 颜色最大值是 255
        # 设置 slotb  滚动条移动
        self.scrollbar_1.sliderMoved.connect(self.sliderMoved)

        self.scrollbar_2 = QScrollBar()
        self.scrollbar_2.setMaximum(255)  # 颜色最大值是 255
        # 设置 slotb  滚动条移动
        self.scrollbar_2.sliderMoved.connect(self.sliderMoved)

        self.scrollbar_3 = QScrollBar()
        self.scrollbar_3.setMaximum(255)  # 颜色最大值是 255
        # 设置 slotb  滚动条移动
        self.scrollbar_3.sliderMoved.connect(self.sliderMoved)

        # 创建滚动条 改变控件位置
        self.scrollbar_4 = QScrollBar()
        self.scrollbar_4.setMaximum(255)
        self.scrollbar_4.sliderMoved.connect(self.controlMoved)

        hbox.addWidget(self.scrollbar_1)
        hbox.addWidget(self.scrollbar_2)
        hbox.addWidget(self.scrollbar_3)
        hbox.addWidget(self.scrollbar_4)

        self.setGeometry(300, 300, 300, 200)

        self.setLayout(hbox)

        # 记录控件位置
        self.y = self.label.pos().y()


    def sliderMoved(self):

        print(self.scrollbar_1.value(), self.scrollbar_2.value(), self.scrollbar_3.value())
        # 设置文字颜色
        palette = QPalette()
        c = QColor(self.scrollbar_1.value(), self.scrollbar_2.value(), self.scrollbar_3.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self.label.setPalette(palette)

    def controlMoved(self):

        # x 保持不变  y 增加
        self.label.move(self.label.x(), self.y - self.scrollbar_4.value())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QScrollBarDemo()
    main.show()
    sys.exit(app.exec_())
