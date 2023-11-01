# -*- coding: utf-8 -*-
# @time    : 2023/10/29 15:25
# @file    : 1_AbsoluteLayoutDemo.py
# @software: PyCharm

"""
绝对布局
通过坐标控制组件位置
"""
import sys

from PyQt5.QtWidgets import *


class AbsoluteLayoutDemo(QWidget):

    def __init__(self):

        super(AbsoluteLayoutDemo, self).__init__()
        self.setWindowTitle('AbsoluteLayout Demo')

        self.label_1 = QLabel('label_1', self)  # self: 直接将控件放置到窗口上 不需要添加到布局中
        # 通过 move 来移动控件
        self.label_1.move(15, 20)  # x: 15, y: 20

        self.label_2 = QLabel('label_2', self)
        self.label_2.move(35, 40)

        self.label_3 = QLabel('label_3', self)
        self.label_3.move(55, 80)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = AbsoluteLayoutDemo()
    main.show()
    sys.exit(app.exec_())

