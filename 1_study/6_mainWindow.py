# -*- coding: utf-8 -*-
# @time    : 2023/7/29 22:11
# @author  : w-xin
# @file    : 6_mainWindow.py
# @software: PyCharm

"""
mainWindow.py
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget


class FirstMainWin(QMainWindow):

    def __init__(self, parent = None):
        super(FirstMainWin, self).__init__(parent)

        # 主窗口标题
        self.setWindowTitle('第一个主窗口应用')

        # 窗口尺寸
        self.resize(400, 300)

        # 状态栏
        self.status = self.statusBar()

        # 状态栏上的信息
        self.status.showMessage('只存在5秒的消息', 5000)  # 5000 为停留的时间 单位是毫秒

        self.center()


    def center(self):
        """
        窗口居中
        :return:
        """

        screen = QDesktopWidget().screenGeometry()  # 得到屏幕的坐标系
        size = self.geometry()  # 获取窗口坐标系
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2

        self.move(newLeft, newTop)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = FirstMainWin()

    main.show()

    sys.exit(app.exec_())
