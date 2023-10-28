# -*- coding: utf-8 -*-
# @time    : 2023/10/26 9:26
# @file    : 8_QDockWidgetDemo.py
# @software: PyCharm

"""
QDockWidget
停靠控件 是一个窗口
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QDockWidgetDemo(QMainWindow):

    def __init__(self):

        super(QDockWidgetDemo, self).__init__()
        self.setWindowTitle('QDockWidget Demo')

        layout = QHBoxLayout()
        self.items = QDockWidget('Dockable', self)
        self.listWidget = QListWidget()
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        # 将 list 放入停靠窗口
        self.items.setWidget(self.listWidget)

        self.setCentralWidget(QLineEdit())

        # 默认状态是停靠状态 可更改
        self.items.setFloating(True)
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QDockWidgetDemo()
    main.show()
    sys.exit(app.exec_())
