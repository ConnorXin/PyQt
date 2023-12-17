# -*- coding: utf-8 -*-
# @time    : 2023-12-16 11:34
# @file    : 3_LayoutAlignDemo.py
# @software: PyCharm

"""
设置控件对齐方式
左对齐
右对齐
顶端对齐
低端对其
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import *


class LayoutAlignDemo(QWidget):

    def __init__(self):

        super(LayoutAlignDemo, self).__init__()

        self.setWindowTitle('Layout Align Demo')

        hbox = QHBoxLayout()
        # stretch: 控件的比例
        # Qt.AlignLeft | Qt.AlignTop: 多个对齐方式用 |
        hbox.addWidget(QPushButton('button_1'), stretch=2, alignment=Qt.AlignLeft | Qt.AlignTop)
        hbox.addWidget(QPushButton('button_2'), stretch=1, alignment=Qt.AlignLeft | Qt.AlignTop)
        hbox.addWidget(QPushButton('button_3'), stretch=4, alignment=Qt.AlignLeft | Qt.AlignTop)
        hbox.addWidget(QPushButton('button_4'), stretch=1, alignment=Qt.AlignLeft | Qt.AlignBottom)
        hbox.addWidget(QPushButton('button_5'), stretch=1, alignment=Qt.AlignLeft | Qt.AlignBottom)

        hbox.setSpacing(40)

        self.setLayout(hbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = LayoutAlignDemo()
    main.show()
    sys.exit(app.exec_())