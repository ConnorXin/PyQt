# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/16 18:44
# @File    :  40_StatusDemo.py
# @IDE     :  PyCharm

"""
状态栏
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StatusDemo(QMainWindow):

    def __init__(self):

        super(StatusDemo, self).__init__()

        self.setWindowTitle('Status Demo')
        self.resize(300, 200)

        menuBar = self.menuBar()
        file = menuBar.addMenu('File')
        file.addAction('show')
        file.triggered.connect(self.processTrigger)

        # 创建状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)


    def processTrigger(self, control):

        if control.text() == 'show':
            self.statusBar.showMessage(control.text() + '菜单被点击了', 5000)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StatusDemo()
    main.show()
    sys.exit(app.exec_())