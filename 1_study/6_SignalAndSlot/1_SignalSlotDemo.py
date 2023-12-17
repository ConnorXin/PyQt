# -*- coding: utf-8 -*-
# @time    : 2023-12-16 12:53
# @file    : 1_SignalSlotDemo.py
# @software: PyCharm

"""
信号 Signal
槽 Slot
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class SignalSlotDemo(QWidget):

    def __init__(self):

        super(SignalSlotDemo, self).__init__()

        self.btn = QPushButton('My Button', self)
        self.btn.clicked.connect(self.onClick)

    def onClick(self):

        self.btn.setText('Signal already commit')
        self.btn.setStyleSheet('QPushButton(max-width:200px;min0width:200px')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = SignalSlotDemo()
    main.show()
    sys.exit(app.exec_())

