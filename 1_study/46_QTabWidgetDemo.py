# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 14:36
# @File    :  46_QTabWidgetDemo.py
# @IDE     :  PyCharm

"""
选项卡控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTabWidgetDemo(QTabWidget):

    def __init__(self):

        super(QTabWidgetDemo, self).__init__()

        self.setWindowTitle('QTabWidget Demo')
        self.resize(600, 400)

        # 先创建窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # 添加 Tab
        self.addTab(self.tab1)
        self.addTab(self.tab2)
        self.addTab(self.tab3)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTabWidgetDemo()
    main.show()
    sys.exit(app.exec_())