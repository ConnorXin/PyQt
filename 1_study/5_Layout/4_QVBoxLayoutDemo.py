# -*- coding: utf-8 -*-
# @time    : 2023-12-16 11:43
# @file    : 4_QVBoxLayoutDemo.py
# @software: PyCharm

"""
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class QVBoxLayoutDemo(QWidget):

    def __init__(self):

        super(QVBoxLayoutDemo, self).__init__()

        self.setWindowTitle('QVBoxLayout Demo')

        vbox = QVBoxLayout()
        vbox.addWidget(QPushButton('button_1'))
        vbox.addWidget(QPushButton('button_2'))
        vbox.addWidget(QPushButton('button_3'))
        vbox.addWidget(QPushButton('button_4'))
        vbox.addWidget(QPushButton('button_5'))

        vbox.setSpacing(40)

        self.setLayout(vbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QVBoxLayoutDemo()
    main.show()
    sys.exit(app.exec_())
