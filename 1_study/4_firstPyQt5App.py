# -*- coding: utf-8 -*-
# @time    : 2023/7/29 15:12
# @author  : w-xin
# @file    : 4_firstPyQt5App.py
# @software: PyCharm

"""
firstPyQt5.py
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget



if __name__ == '__main__':

    # 创建 QApplication 类的实例
    app = QApplication(sys.argv)  # sys.argv 获得命令行参数

    # 创建窗口
    window = QWidget()

    # 设置窗口尺寸
    window.resize(400, 200)

    # 移动窗口
    window.move(300, 300)

    # 设置窗口标题
    window.setWindowTitle('The First app from PyQt5')

    # 显示窗口
    window.show()

    # 进入程序的主循环 并通过 exit 确保主循环安全结束
    sys.exit(app.exec_())