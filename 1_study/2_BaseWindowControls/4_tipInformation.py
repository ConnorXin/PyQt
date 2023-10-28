# -*- coding: utf-8 -*-
# @time    : 2023/7/30 13:58
# @author  : w-xin
# @file    : 4_tipInformation.py
# @software: PyCharm

"""
控件提示信息
"""
import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QPushButton, QWidget, QHBoxLayout


class TipInformation(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 12))
        # 设置提示信息 鼠标悬停窗口会出现
        self.setToolTip('今天是<b>周日</b>')  # <b></b> 设置粗体

        self.resize(400, 200)

        self.setWindowTitle('控件提示信息')


        # 设置按钮
        self.button1 = QPushButton('button')
        # 设置按钮中提示信息
        self.button1.setToolTip('this is button')


        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)





if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = TipInformation()
    main.show()

    sys.exit(app.exec_())