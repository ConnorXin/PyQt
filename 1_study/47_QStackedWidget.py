# -*- coding: utf-8 -*-
# @time    : 2023/10/24 9:48
# @file    : 47_QStackedWidget.py
# @software: PyCharm

"""
堆栈窗口控件
"""
import sys

from PyQt5.QtWidgets import *


class StackedDemo(QWidget):

    def __init__(self):

        super(StackedDemo, self).__init__()
        self.setGeometry(300, 500, 10, 10)
        self.setWindowTitle('QStacked Demo')

        self.list = QListWidget()
        self.list.insertItem(0, 'contact')
        self.list.insertItem(1, 'person_info')
        self.list.insertItem(2, 'extent_edu')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.lay_stack1()
        self.lay_stack2()
        self.lay_stack3()

        # 堆栈窗口控件的对象
        self.stack = QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)

        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)

        # 将右侧的 list 设立点击事件
        self.list.currentRowChanged.connect(self.display)


    def lay_stack1(self):
        layout = QFormLayout()
        layout.addRow('name', QLineEdit())
        layout.addRow('address', QLineEdit())

        self.stack1.setLayout(layout)


    def lay_stack2(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('male'))
        sex.addWidget(QRadioButton('female'))
        layout.addRow(QLabel('sex'), sex)
        layout.addRow('birthday', QLineEdit())
        self.stack2.setLayout(layout)


    def lay_stack3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel('subject'))
        layout.addWidget(QCheckBox('physics'))
        layout.addWidget(QCheckBox('math_plus'))
        self.stack3.setLayout(layout)


    def display(self, index):

        # 根据栈切换页面
        self.stack.setCurrentIndex(index)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = StackedDemo()
    main.show()
    sys.exit(app.exec_())