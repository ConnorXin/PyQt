# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/3 16:25
# @File    :  QCheckBoxDemo.py
# @IDE     :  PyCharm

"""
QCheckBox 复选框控件
多选控件

有三种状态
1 未选中: 0
2 半选中: 1
3 选中: 2
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class QCheckBoxDemo(QWidget):

    def __init__(self):

        super(QCheckBoxDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QCheckBox Demo')
        self.resize(300, 400)

        layout = QHBoxLayout()

        # QCheckBox1
        self.checkBox1 = QCheckBox('checkBox1')
        self.checkBox1.setChecked(True)  # 默认选中状态
        # signal
        self.checkBox1.stateChanged.connect(self.checkBoxStatu)
        layout.addWidget(self.checkBox1)

        # QCheckBox2
        self.checkBox2 = QCheckBox('checkBox2')
        # self.checkBox2.stateChanged.connect(lambda: self.checkBoxStatu(self.checkBox2))
        layout.addWidget(self.checkBox2)

        # QCheckBox3
        self.checkBox3 = QCheckBox('checkBox3')
        # self.checkBox3.stateChanged.connect(lambda: self.checkBoxStatu(self.checkBox3))
        # 设置以下两个能够让复选框处于半选中状态
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)


    def checkBoxStatu(self):

        cb = self.sender()

        checkStatus = cb.text() + ', isChecked = ' + str(cb.isChecked()) + ', checkState = ' + str(cb.checkStatu()) + '\n'
        print(checkStatus)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QCheckBoxDemo()
    main.show()

    sys.exit(app.exec_())

