# -*- coding: utf-8 -*-
# @time    : 2023-12-16 11:58
# @file    : 6_btnAlwaysRightBottom.py
# @software: PyCharm

"""
让按钮永远在窗口右下角的布局技巧
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class ButtonAlwaysRightBottomDemo(QWidget):

    def __init__(self):

        super(ButtonAlwaysRightBottomDemo, self).__init__()

        self.setWindowTitle('Button Always in Right Bottom')
        self.resize(400, 300)

        btn_ok = QPushButton('ok')
        btn_cancel = QPushButton('cancel')

        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(btn_ok)
        hbox.addWidget(btn_cancel)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addStretch()

        vbox.addLayout(hbox)

        self.setLayout(vbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = ButtonAlwaysRightBottomDemo()
    main.show()
    sys.exit(app.exec_())

