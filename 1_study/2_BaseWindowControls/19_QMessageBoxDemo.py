# -*- coding: utf-8 -*-
# @time    : 2023/8/5 16:27
# @author  : w-xin
# @file    : 19_QMessageBoxDemo.py
# @software: PyCharm

"""
QDialog 基类下的 QMessageBox 对话框
主要用于软件的版本以及作者的其他信息

常用消息对话框
1 关于对话框
2 错误对话框
3 警告对话框
4 提问对话框
5 消息对话框

其中有2点差异
1 显示的对话框图标可能不一样
2 对话框显示的按钮不一样
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QMessageBoxDemo(QWidget):

    def __init__(self):

        super(QMessageBoxDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QMessageBox Demo')
        self.resize(300, 600)

        layout = QVBoxLayout()

        # 1 关于对话框
        self.buttonAbout = QPushButton('About Box')
        self.buttonAbout.clicked.connect(self.showDialog)
        layout.addWidget(self.buttonAbout)
        # 2 错误对话框
        self.buttonError = QPushButton('Error Box')
        self.buttonError.clicked.connect(self.showDialog)
        layout.addWidget(self.buttonError)
        # 3 警告对话框
        self.buttonWarning = QPushButton('Warning Box')
        self.buttonWarning.clicked.connect(self.showDialog)
        layout.addWidget(self.buttonWarning)
        # 4 提问对话框  提问用户是否确定关闭某窗口
        self.buttonQuestion = QPushButton('Question Box')
        self.buttonQuestion.clicked.connect(self.showDialog)
        layout.addWidget(self.buttonQuestion)
        # 5 消息对话框
        self.buttonMessage = QPushButton('Message Box')
        self.buttonMessage.clicked.connect(self.showDialog)
        layout.addWidget(self.buttonMessage)

        self.setLayout(layout)


    def showDialog(self):

        text = self.sender().text()
        if text == 'About Box':
            # about 是窗口标题  This is About Dialog. 是对话框内容
            QMessageBox.about(self, 'about', 'This is About Dialog.')
        elif text == 'Error Box':
            # Error: 窗口标题
            # This is Error Dialog.: 窗口内容
            # QMessageBox.Yes | QMessageBox.No: 按照业务而定 对话框按钮是 Yes, No
            # 也可以返回值
            QMessageBox.critical(self, 'Error', 'This is Error Dialog.',
                                 QMessageBox.Yes | QMessageBox.No)
        elif text == 'Warning Box':
            # Warning: 窗口标题
            # This is Warning Dialog.: 窗口内容
            # QMessageBox.Yes | QMessageBox.No: 按照业务而定 对话框按钮是 Yes, No
            # 也可以返回值
            QMessageBox.warning(self, 'Warning', 'This is Warning Dialog.',
                                QMessageBox.Yes | QMessageBox.No)
        elif text == 'Question Box':
            # Question: 窗口标题
            # This is Question Dialog.: 窗口内容
            # QMessageBox.Yes | QMessageBox.No: 按照业务而定 对话框按钮是 Yes, No
            # 也可以返回值
            QMessageBox.question(self, 'Question', 'This is Question Dialog.',
                                 QMessageBox.Yes | QMessageBox.No)
        elif text == 'Message Box':
            # Message: 窗口标题
            # This is Message Dialog.: 窗口内容
            # QMessageBox.Yes | QMessageBox.No: 按照业务而定 对话框按钮是 Yes, No
            # QMessageBox.Yes: 按回车默认按钮
            reply = QMessageBox.information(self, 'Message', 'This is Message Dialog.',
                                            QMessageBox.Yes | QMessageBox.No,
                                            QMessageBox.Yes)
            print(reply == QMessageBox.Yes)  # 输出按钮值  可以判断


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QMessageBoxDemo()
    main.show()
    sys.exit(app.exec_())