# -*- coding: utf-8 -*-
# @time    : 2023/8/6 13:50
# @author  : w-xin
# @file    : 29_ControlDragDemo.py
# @software: PyCharm

"""
让控件支持拖拽动作

A.setDragEnabled(True)
B.setAcceptDrops(True)

B 需要两个事件
1 dragEnterEvent  将 A 拖到 B 触发
2 dropEvent       在 B 的区域放下 A 时触发

Demo
给出文本输入框 将文本拖到 QComboBox 控件里面追加内容
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyComboBox(QComboBox):

    def __init__(self):

        super(MyComboBox, self).__init__()

        self.setAcceptDrops(True)  # 就可以接收别的控件了


    def dragEnterEvent(self, control):
        """
        将控件拖入
        :param control:
        :return:
        """
        print(control)
        if control.mimeData().hasText():
            control.accept()
        else:
            control.ignore()


    def dropEvent(self, control):
        """
        将控件放下
        :param control:
        :return:
        """
        self.addItem(control.mimeData().text())


class ControlDragDemo(QWidget):

    def __init__(self):

        super(ControlDragDemo, self).__init__()

        self.setWindowTitle('ControlDrag Demo')
        self.resize(600, 100)

        layout = QFormLayout()
        layout.addRow(QLabel('请将左边的文本拖拽到右边的下拉列表中'))

        lineEdit = QLineEdit()
        # 还需要将文本设置允许被拖动的设置
        lineEdit.setDragEnabled(True)

        comboBox = MyComboBox()
        layout.addRow(lineEdit, comboBox)

        self.setLayout(layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = ControlDragDemo()
    main.show()
    sys.exit(app.exec_())