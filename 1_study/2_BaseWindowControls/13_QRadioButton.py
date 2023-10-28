# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/3 15:56
# @File    :  13_QRadioButton.py
# @IDE     :  PyCharm

"""
QRadioButton 单选控件

多个单选控件若想只能选择一个
那么需要将多个单选控件放置到一个容器里面
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QRadioButtonDemo(QWidget):

    def __init__(self):

        super(QRadioButtonDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QRadioButton Demo')
        self.resize(400, 300)

        layout = QHBoxLayout()

        # button1
        self.button1 = QRadioButton('Button1')
        self.button1.setChecked(True)  # 设置默认情况下按钮是选中状态
        # signal  使用 toggle 判断是否选中
        self.button1.toggled.connect(self.buttonStatu)
        layout.addWidget(self.button1)

        # button2
        self.button2 = QRadioButton('Button2')
        self.button2.toggled.connect(self.buttonStatu)
        layout.addWidget(self.button2)

        self.setLayout(layout)


    def buttonStatu(self):

        # 获取控件
        radioButton = self.sender()
        if radioButton.isChecked() == True:  # 判断是否被选中
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 未被选中')




if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QRadioButtonDemo()
    main.show()

    sys.exit(app.exec_())
