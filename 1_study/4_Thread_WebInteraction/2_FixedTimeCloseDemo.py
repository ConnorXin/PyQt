# -*- coding: utf-8 -*-
# @time    : 2023/10/29 12:53
# @file    : 2_FixedTimeCloseDemo.py
# @software: PyCharm

"""
程序自动关闭
QTimer.singleShot: 在指定时间后只调用一次
"""
import sys

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import *


class FixedTimeCloseDemo(QWidget):

    def __init__(self):

        super(FixedTimeCloseDemo, self).__init__()
        self.setWindowTitle('FixedTimeClose Demo')

        self.label = QLabel('<font color=blue size=140><b>Hello World, windows will be close after 5s<b></font>')
        # self.label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
        self.label.show()

        # 静态方法 不用实例化
        QTimer.singleShot(5000, app.quit)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = FixedTimeCloseDemo()
    sys.exit(app.exec_())
