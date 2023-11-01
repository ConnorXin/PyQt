# -*- coding: utf-8 -*-
# @time    : 2023/10/29 12:36
# @file    : 1_ShowTimeDemo.py
# @software: PyCharm

"""
动态显示当前时间
QTimer: 定时器 每隔一段时间调用一次
QThread

多线程: 用于同时完成多个任务
"""
import sys

from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtWidgets import *


class ShowTimeDemo(QWidget):

    def __init__(self):

        super(ShowTimeDemo, self).__init__()
        self.setWindowTitle('Show Time Demo')

        self.label = QLabel('show current time')
        self.startBtn = QPushButton('start')
        self.endBtn = QPushButton('end')

        layout = QGridLayout()
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)

        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)
        self.setLayout(layout)


    def showTime(self):

        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label.setText(timeDisplay)


    def startTimer(self):

        self.timer.start(1000)  # 参数设置时间间隔 1000 == 1000ms == 1s
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)


    def endTimer(self):

        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = ShowTimeDemo()
    main.show()
    sys.exit(app.exec_())


