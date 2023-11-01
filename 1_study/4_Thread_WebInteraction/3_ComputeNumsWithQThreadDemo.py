# -*- coding: utf-8 -*-
# @time    : 2023/10/29 13:05
# @file    : 3_ComputeNumsWithQThreadDemo.py
# @software: PyCharm

"""
QThread
使用线程编写计数器

QThread 派生一个子类
在子类中定义 run() 方法
class claname(QThread):
    def run(self):
        实现想要的功能
        while True:
            self.sleep(1)  休眠一秒
            if sec == 5:
                break

QLCDNumber: 模拟 LED 效果的显示控件
用到自定义信号
"""
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *


# 当前计数从0开始
sec = 0

class WorkThread(QThread):

    timer = pyqtSignal()  # 每隔一秒发送一次信号
    end = pyqtSignal()  # 计数完成发送信号

    def __init__(self):

        super(WorkThread, self).__init__()

    def run(self):

        while True:
            self.sleep(1)
            if sec == 5:
                # emit 相当于触发了 connect 调用一次与信号相关的 slot
                self.end.emit()  # 发送 end 信号
                break
            self.timer.emit()


class ComputeNumsWithQThreadDemo(QWidget):

    def __init__(self):

        super(ComputeNumsWithQThreadDemo, self).__init__()
        self.setWindowTitle('ComputeNumsWithQThread Demo')
        self.resize(300, 120)

        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        btn = QPushButton('count begin')
        layout.addWidget(btn)

        self.setLayout(layout)

        self.thread = WorkThread()
        # 自定义信号绑定
        self.thread.timer.connect(self.countTime)
        self.thread.end.connect(self.end)
        btn.clicked.connect(self.work)


    def countTime(self):

        global sec
        sec += 1
        self.lcdNumber.display(sec)  # 显示


    def end(self):

        QMessageBox.information(self, 'message', 'count end', QMessageBox.Ok)


    def work(self):

        self.thread.start()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = ComputeNumsWithQThreadDemo()
    main.show()
    sys.exit(app.exec_())


