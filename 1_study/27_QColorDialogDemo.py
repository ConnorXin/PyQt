# -*- coding: utf-8 -*-
# @time    : 2023/8/5 20:38
# @author  : w-xin
# @file    : 27_QColorDialogDemo.py
# @software: PyCharm

"""
QColorDialog 设置颜色对话框
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QColorDialogDemo(QWidget):

    def __init__(self):

        super(QColorDialogDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QColorDialog Demo')
        self.resize(400, 200)

        layout = QVBoxLayout()
        self.colorButton = QPushButton('Select Color')
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)

        self.colorBGButton = QPushButton('Select BGColor')
        self.colorBGButton.clicked.connect(self.getBGColor)
        layout.addWidget(self.colorBGButton)

        self.colorLabel = QLabel('Test Color Example')

        layout.addWidget(self.colorLabel)

        self.setLayout(layout)


    def getColor(self):

        color = QColorDialog.getColor()
        # 设置文字颜色
        t = QPalette()
        t.setColor(QPalette.WindowText, color)
        self.colorLabel.setPalette(t)


    def getBGColor(self):
        """
        设置背景色
        :return:
        """
        color = QColorDialog.getColor()
        t = QPalette()
        t.setColor(QPalette.Window, color)
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(t)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QColorDialogDemo()
    main.show()
    sys.exit(app.exec_())