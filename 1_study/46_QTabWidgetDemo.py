# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 14:36
# @File    :  46_QTabWidgetDemo.py
# @IDE     :  PyCharm

"""
选项卡控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTabWidgetDemo(QTabWidget):

    def __init__(self):

        super(QTabWidgetDemo, self).__init__()

        self.setWindowTitle('QTabWidget Demo')
        self.resize(600, 400)

        # 先创建窗口
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # 添加 Tab
        # 为被一个 tab 写一个方法
        self.addTab(self.tab1, 'tab1')
        self.addTab(self.tab2, 'tab2')
        self.addTab(self.tab3, 'tab3')

        self.lay_tab1()
        self.lay_tab2()
        self.lay_tab3()

    def lay_tab1(self):

        layout = QFormLayout()
        layout.addRow('name', QLineEdit())
        layout.addRow('address', QLineEdit())
        # 修改 tab title
        self.setTabText(0, 'login')

        self.tab1.setLayout(layout)


    def lay_tab2(self):

        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('male'))
        sex.addWidget(QRadioButton('female'))
        layout.addRow(QLabel('sex'), sex)
        layout.addRow('birthday', QLineEdit())
        self.setTabText(1, 'user_info')
        self.tab2.setLayout(layout)


    def lay_tab3(self):

        layout = QHBoxLayout()
        layout.addWidget(QLabel('subject'))
        layout.addWidget(QCheckBox('physics'))
        layout.addWidget(QCheckBox('math_plus'))
        self.setTabText(2, 'extent_eduate')
        self.tab3.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTabWidgetDemo()
    main.show()
    sys.exit(app.exec_())