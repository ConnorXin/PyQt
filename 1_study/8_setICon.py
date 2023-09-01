# -*- coding: utf-8 -*-
# @time    : 2023/7/30 13:47
# @author  : w-xin
# @file    : 8_setICon.py
# @software: PyCharm

"""
设置图标
"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget


class SetICon(QMainWindow):

    def __init__(self, parent = None):

        super(SetICon, self).__init__(parent)

        self.initUI()

    def initUI(self):

        # 设置坐标系
        self.setGeometry(300, 300, 250, 250)

        # 主窗口标题
        self.setWindowTitle('设置图标')

        # 窗口尺寸
        # self.resize(400, 300)

        #设置窗口图标
        self.setWindowIcon(QIcon('./images/Basilisk.icon'))




if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./'))
    main = SetICon()

    main.show()

    sys.exit(app.exec_())
