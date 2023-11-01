# -*- coding: utf-8 -*-
# @time    : 2023/10/29 15:32
# @file    : 2_QHBoxLayoutDemo.py
# @software: PyCharm

"""
QHBoxLayout
水平盒布局
将控件按照水平方向按照一定规则进行排列
"""
import sys

from PyQt5.QtWidgets import *


class QHBoxLayoutDemo(QWidget):

    def __init__(self):

        super(QHBoxLayoutDemo, self).__init__()
        self.setWindowTitle('QHBoxLayout Demo')

        hbox = QHBoxLayout()
        # 默认情况下 五个控件会水平等距进行排列
        hbox.addWidget(QPushButton('button_1'))
        hbox.addWidget(QPushButton('button_2'))
        hbox.addWidget(QPushButton('button_3'))
        hbox.addWidget(QPushButton('button_4'))
        hbox.addWidget(QPushButton('button_5'))

        self.setLayout(hbox)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QHBoxLayoutDemo()
    main.show()
    sys.exit(app.exec_())


