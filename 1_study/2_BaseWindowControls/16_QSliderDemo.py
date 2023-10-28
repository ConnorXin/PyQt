# -*- coding: utf-8 -*-
# @time    : 2023/8/4 10:14
# @author  : w-xin
# @file    : 16_QSliderDemo.py
# @software: PyCharm

"""
QSlider 滑块控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QSliderDemo(QWidget):

    def __init__(self):

        super(QSliderDemo, self).__init__()

        # self.initHUI()
        self.initVUI()


    def initHUI(self):

        self.setWindowTitle('QSlider Demo')
        self.resize(300, 400)

        layout = QVBoxLayout()

        self.label = QLabel('hello pyqt')
        self.label.setAlignment(Qt.AlignCenter)  # 居中显示
        layout.addWidget(self.label)
        # 水平滑块
        self.HSlider = QSlider(Qt.Horizontal)
        # 设置最小值
        self.HSlider.setMaximum(12)
        # 设置最大值
        self.HSlider.setMaximum(48)
        # 设置步长
        self.HSlider.setSingleStep(3)
        # 设置当前值
        self.HSlider.setValue(18)
        # 设置刻度位置 设置刻度在下方
        self.HSlider.setTickPosition(QSlider.TicksBelow)
        # 控制刻度的间隔
        self.HSlider.setTickInterval(6)
        layout.addWidget(self.HSlider)
        self.HSlider.valueChanged.connect(self.valueChange)

        self.setLayout(layout)


    def initVUI(self):

        self.setWindowTitle('QSlider Demo')
        self.resize(300, 700)

        layout = QVBoxLayout()

        self.label = QLabel('hello pyqt')
        self.label.setAlignment(Qt.AlignCenter)  # 居中显示
        layout.addWidget(self.label)
        # 水平滑块
        self.VSlider = QSlider(Qt.Vertical)
        # 设置最小值
        self.VSlider.setMaximum(10)
        # 设置最大值
        self.VSlider.setMaximum(60)
        # 设置步长
        self.VSlider.setSingleStep(5)
        # 设置当前值
        self.VSlider.setValue(30)
        # 设置刻度位置 设置刻度在下方
        self.VSlider.setTickPosition(QSlider.TicksLeft)
        # 控制刻度的间隔
        self.VSlider.setTickInterval(2)
        layout.addWidget(self.VSlider)
        self.VSlider.valueChanged.connect(self.valueChange)

        self.setLayout(layout)




    def valueChange(self):
        """
        根据滑块所指大小改变字体大小
        :return:
        """

        print(f'当前值: {self.VSlider.value()}')
        size = self.VSlider.value()
        self.label.setFont(QFont('Arial', size))





if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QSliderDemo()
    main.show()

    sys.exit(app.exec_())