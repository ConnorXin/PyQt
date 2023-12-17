# -*- coding: utf-8 -*-
# @time    : 2023-12-16 13:00
# @file    : 2_CustomSignalDemo.py
# @software: PyCharm

"""
自定义信号
类型: 创建一个 pyqtSignal() 对象
"""
import sys

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget


class CustomSignal(QObject):

    # 定义信号 接收 object 类型 可以传入 list 类型的数据
    send_msg = pyqtSignal(object)
    # 传递多个参数
    send_multi_msg = pyqtSignal(str, int, int)
    # 可以传入 int 和 str, 或者只传 str 类型
    send_multi_type = pyqtSignal([int, str], [str])

    def __init__(self):

        super(CustomSignal, self).__init__()

    def run(self):

        self.send_msg.emit('signal already commit')

    def multi_run(self):

        self.send_multi_msg.emit('pyqt', 3, 6)


class CustomSignalDemo(QObject):

    def __init__(self):

        super(CustomSignalDemo, self).__init__()

    def get(self, msg):

        print('information ' + msg)

    def multi_get(self, msg, a, b):

        print(msg)
        print(a + b)


if __name__ == '__main__':

    send = CustomSignal()
    slot = CustomSignalDemo()

    send.send_msg.connect(slot.get)
    send.send_multi_msg.connect(slot.multi_get)

    send.run()
    send.multi_run()
