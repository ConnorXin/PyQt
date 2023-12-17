# -*- coding: utf-8 -*-
# @time    : 2023-12-16 12:45
# @file    : 10_QSplitterDemo.py
# @software: PyCharm

"""
控制控件之间的边界
QSplitter
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QSplitter, QTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt


class QSplitterDemo(QWidget):

    def __init__(self):

        super(QSplitterDemo, self).__init__()

        self.setWindowTitle('QSplitter Demo')
        self.resize(700, 300)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter_1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter_1.addWidget(topleft)
        splitter_1.addWidget(textedit)

        splitter_2 = QSplitter(Qt.Vertical)
        splitter_2.addWidget(splitter_1)
        splitter_2.addWidget(bottom)

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter_2)
        self.setLayout(hbox)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QSplitterDemo()
    main.show()
    sys.exit(app.exec_())
