# -*- coding: utf-8 -*-
# @time    : 2023-12-16 11:47
# @file    : 5_addStretchDemo.py
# @software: PyCharm

"""
设置伸缩量: addStretch
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class SetStretchDemo(QWidget):

    def __init__(self):

        super(SetStretchDemo, self).__init__()

        self.setWindowTitle('Set Stretch Demo')
        self.resize(800, 300)

        btn1 = QPushButton(self)
        btn2 = QPushButton(self)
        btn3 = QPushButton(self)
        btn1.setText('button 1')
        btn2.setText('button 2')
        btn3.setText('button 3')

        layout = QHBoxLayout()
        layout.addStretch(0)
        layout.addWidget(btn1)
        layout.addStretch(2)
        layout.addWidget(btn2)
        layout.addStretch(1)
        layout.addWidget(btn3)
        self.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = SetStretchDemo()
    main.show()
    sys.exit(app.exec_())
