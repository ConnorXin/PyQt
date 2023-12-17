# -*- coding: utf-8 -*-
# @time    : 2023-12-16 12:19
# @file    : 8_QGridLayoutFormMultiRowColDemo.py
# @software: PyCharm

"""
栅格布局
跨行跨列的表单布局
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QTextEdit


class QGridLayoutFormMultiRowColDemo(QWidget):

    def __init__(self):

        super(QGridLayoutFormMultiRowColDemo, self).__init__()

        self.setWindowTitle('QGridLayoutFormMultiRowCol Demo')
        self.resize(350, 300)

        label_title = QLabel('title')
        label_author = QLabel('author')
        label_content = QLabel('content')

        edit_title = QLineEdit()
        edit_author = QLineEdit()
        edit_content = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(label_title, 1, 0)
        grid.addWidget(edit_title, 1, 1)
        grid.addWidget(label_author, 2, 0)
        grid.addWidget(edit_author, 2, 1)
        grid.addWidget(label_content, 3, 0)
        # 在3行1列的位置，占据5行1列的空间
        grid.addWidget(edit_content, 3, 1, 5, 1)

        self.setLayout(grid)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QGridLayoutFormMultiRowColDemo()
    main.show()
    sys.exit(app.exec_())

