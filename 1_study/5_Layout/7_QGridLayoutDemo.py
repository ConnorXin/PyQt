# -*- coding: utf-8 -*-
# @time    : 2023-12-16 12:07
# @file    : 7_QGridLayoutDemo.py
# @software: PyCharm

"""
栅格布局
实现计算器 ui
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton


class QGridLayoutDemo(QWidget):

    def __init__(self):

        super(QGridLayoutDemo, self).__init__()

        self.setWindowTitle('QGridLayout Demo')

        grid = QGridLayout()
        self.setLayout(grid)

        btn_names = ['Cls', 'Back', '', 'Close', '7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '.', '=', '+']

        # 通过列表二重循环设置位置 (5, 4)
        positions = [(i, j) for i in range(5) for j in range(4)]

        # 通过 zip 将 position 和 btn_names 合并一起
        for position, btn_name in zip(positions, btn_names):
            if btn_name == '':
                continue
            btn = QPushButton(btn_name, self)
            # 将 position 元组转换为单个值 可以只用切片
            # 也可以在 position 前面加 *
            # grid.addWidget(btn, position[0], position[1])
            grid.addWidget(btn, *position)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QGridLayoutDemo()
    main.show()
    sys.exit(app.exec_())
