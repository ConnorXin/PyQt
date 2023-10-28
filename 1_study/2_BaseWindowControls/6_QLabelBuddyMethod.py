# -*- coding: utf-8 -*-
# @time    : 2023/7/30 15:12
# @author  : w-xin
# @file    : 6_QLabelBuddyMethod.py
# @software: PyCharm

"""
QLabel 设置伙伴关系

"""
import sys
from PyQt5.QtWidgets import *


class QLabelBuddy(QDialog):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QLabel Buddy')

        self.nameLabel = QLabel('&Name', self)  # &N 代表快捷键

        self.nameLineEdit = QLineEdit(self)

        # 设置 nameLabel 与 nameLineEdit 的伙伴关系
        self.nameLabel.setBuddy(self.nameLineEdit)


        self.passwardLabel = QLabel('&Passward', self)
        self.passwardLineEdit = QLineEdit(self)

        self.passwardLabel.setBuddy(self.passwardLineEdit)


        btnOk = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        # 网格布局
        mainLayout = QGridLayout(self)
        mainLayout.addWidget(self.nameLabel, 0, 0)  # 0, 0: 第一行第一列
        mainLayout.addWidget(self.nameLineEdit, 0, 1, 1, 2)  # 1, 2: 占用一行两列
        mainLayout.addWidget(self.passwardLabel, 1, 0)
        mainLayout.addWidget(self.passwardLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOk, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())
