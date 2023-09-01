# -*- coding: utf-8 -*-
# @time    : 2023/8/5 20:30
# @author  : w-xin
# @file    : 26_QFontDialogDemo.py
# @software: PyCharm

"""
QFontDialog 字体对话框
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QFontDialogDemo(QWidget):

    def __init__(self):

        super(QFontDialogDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QFontDialog Demo')
        self.resize(400, 200)

        layout = QVBoxLayout()
        self.fontButton = QPushButton('Select Font')
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontLabel = QLabel('Test Font Example')

        layout.addWidget(self.fontLabel)

        self.setLayout(layout)


    def getFont(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())
