# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 11:59
# @File    :  3_QListWidgetDemo.py
# @IDE     :  PyCharm

"""
QListWidget
扩展的列表控件

QListWidget 是 QListView 的子类
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QListWidgetDemo(QMainWindow):

    def __init__(self):

        super(QListWidgetDemo, self).__init__()

        self.setWindowTitle('QListWidget Demo')
        self.resize(600, 400)

        self.listWidget = QListWidget()
        self.listWidget.resize(300, 120)

        # add items
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')
        self.listWidget.addItem('item4')
        self.listWidget.addItem('item5')

        self.setCentralWidget(self.listWidget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListWidgetDemo()
    main.show()
    sys.exit(app.exec_())