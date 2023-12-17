# -*- coding: utf-8 -*-
# @time    : 2023-12-16 12:26
# @file    : 9_QFormLayoutDemo.py
# @software: PyCharm

"""
表单布局
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QTextEdit


class QFormLayoutDemo(QWidget):

    def __init__(self):

        super(QFormLayoutDemo, self).__init__()

        self.setWindowTitle('QFormLayout Demo')
        self.resize(350, 300)

        formLayout = QFormLayout()

        label_title = QLabel('title')
        label_author = QLabel('author')
        label_content = QLabel('content')

        edit_title = QLineEdit()
        edit_author = QLineEdit()
        edit_content = QTextEdit()

        formLayout.addRow(label_title, edit_title)
        formLayout.addRow(label_author, edit_author)
        formLayout.addRow(label_content, edit_content)

        self.setLayout(formLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QFormLayoutDemo()
    main.show()
    sys.exit(app.exec_())
