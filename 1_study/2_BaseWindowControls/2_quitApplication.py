# -*- coding: utf-8 -*-
# @time    : 2023/7/29 22:29
# @author  : w-xin
# @file    : 2_quitApplication.py
# @software: PyCharm

"""
退出整个应用程序
"""
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QWidget, QPushButton


class QuitApplication(QMainWindow):

    def __init__(self):

        super(QuitApplication, self).__init__()

        self.resize(300, 120)

        self.setWindowTitle('quit application')

        # 添加 Button
        self.button1 = QPushButton('quit application')
        self.button1.clicked.connect(self.buttonClick)  # 与事件绑定

        # 创建布局
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        # 窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)  # 充满整个屏幕


    def buttonClick(self):
        """
        button 被按下的事件
        :return:
        """

        sender = self.sender()  # 通过 sender 获取 button
        print(sender.text() + 'button is clicked.')  # sender.text() 获取 button 的文本

        app = QApplication.instance()
        app.quit()  # 推出应用程序


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())