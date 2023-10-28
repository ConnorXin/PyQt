# -*- coding: utf-8 -*-
# @time    : 2023/8/5 16:57
# @author  : w-xin
# @file    : 20_QInputDialogDemo.py
# @software: PyCharm

"""
QInputDialog 用户输入对话框

一些静态方法
QInputDialog.getItem: 显示输入列表 需要传入列表或者元组 然后显示 QComboBox 下拉框
QInputDialog.getText: 输入字符串对话框
QInputDialog.getInt: 输入数字 显示计数器控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QInputDialogDemo(QWidget):

    def __init__(self):

        super(QInputDialogDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QInputDialog Demo')
        self.resize(400, 150)

        layout = QFormLayout()

        self.buttonList = QPushButton('getItem')
        self.buttonList.clicked.connect(self.getItem)
        self.lineEditList = QLineEdit()
        layout.addRow(self.buttonList, self.lineEditList)

        self.buttonStr = QPushButton('getText')
        self.buttonStr.clicked.connect(self.getText)
        self.lineEditStr = QLineEdit()
        layout.addRow(self.buttonStr, self.lineEditStr)

        self.buttonInt = QPushButton('getInt')
        self.buttonInt.clicked.connect(self.getInt)
        self.lineEditInt = QLineEdit()
        layout.addRow(self.buttonInt, self.lineEditInt)


        self.setLayout(layout)


    def getItem(self):

        items = ('C', 'C++', 'Python', 'Java')
        # 'Please Select Language': 对话框标题
        # 'Language List': 对话框内小标题
        # items: 输入列表
        # item: 返回用户所选择的值
        # ok: 是否取消选择 Bool
        item, ok = QInputDialog.getItem(self, 'Please Select Language', 'Language List', items)
        if ok and item:
            self.lineEditList.setText(item)


    def getText(self):

        # 'Text Input Box': 对话框标题
        # 'Text': 对话框内小标题
        text, ok = QInputDialog.getText(self, 'Text Input Box', 'Text')
        if ok and text:
            self.lineEditStr.setText(text)


    def getInt(self):

        # 'Int Input Box': 对话框标题
        # 'Int': 对话框内小标题
        num, ok = QInputDialog.getInt(self, 'Int Input Box', 'Int')
        if ok and num:
            self.lineEditInt.setText(str(num))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())