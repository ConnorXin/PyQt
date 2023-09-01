# -*- coding: utf-8 -*-
# @time    : 2023/7/30 16:45
# @author  : w-xin
# @file    : 16_QTextEditDemo.py
# @software: PyCharm

"""
QTextEdit 输入多行文本
"""
import sys
import time
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QThread


class MyThread(QThread):

    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self):

        super(MyThread, self).__init__()


    def __del__(self):

        self.wait()


    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """

        for i in range(10):
            time.sleep(0.5)
            self.signal.emit(str("hello world" + str(i)))  # 发射信号


class QTextEditDemo(QWidget):

    def __init__(self):

        super(QTextEditDemo, self).__init__()

        self.initUI()



    def initUI(self):

        self.setWindowTitle('QTextEditDemo')

        self.resize(300, 280)

        self.textEdit = QTextEdit()

        self.buttonText = QPushButton('show Text')
        self.buttonHTML = QPushButton('show HTML')

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)

        self.setLayout(layout)

        # 绑定事件
        self.buttonText.clicked.connect(self.onClickButtonTextThread)
        self.buttonHTML.clicked.connect(self.onClickButtonHTML)


    def onClickButtonTextThread(self):

        self.thread = MyThread()
        self.thread.signal.connect(self.onClickButtonText)
        self.thread.start()


    def onClickButtonText(self):

        for i in range(100):
            self.textEdit.append(f'Hello PyQt5-{i}')
            self.textEdit.moveCursor(self.textEdit.textCursor().End)


    def onClickButtonHTML(self):

        self.textEdit.setHtml('<font color="blue" size="5">Hello PyQt</font>')

if __name__ == '__main__':

    app =QApplication(sys.argv)

    main = QTextEditDemo()
    main.show()

    sys.exit(app.exec_())