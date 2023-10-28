# -*- coding: utf-8 -*-
# @time    : 2023/8/5 12:38
# @author  : w-xin
# @file    : 17_QSpinBoxDemo.py
# @software: PyCharm

"""
QSpinBox 计数器控件
控制一个数字的增加和减少
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QSpinBoxDemo(QWidget):

    def __init__(self):

        super(QSpinBoxDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QSpinBox Demo')
        self.resize(400, 100)

        layout = QVBoxLayout()
        self.label = QLabel('当前值')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.spinBox = QSpinBox()
        self.spinBox.setValue(18)  # 设置默认值
        self.spinBox.setRange(8, 50)  # 设置范围
        self.spinBox.setSingleStep(6)  # 设置步长
        layout.addWidget(self.spinBox)

        self.spinBox.valueChanged.connect(self.valueChange)

        self.setLayout(layout)


    def valueChange(self):

        self.label.setText('当前值' + str(self.spinBox.value()))



if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QSpinBoxDemo()
    main.show()

    sys.exit(app.exec_())