# -*- coding: utf-8 -*-
# @time    : 2023/7/30 14:15
# @author  : w-xin
# @file    : 10_QLabelMethod.py
# @software: PyCharm

"""
QLabel 控件基础使用

QLabel 常用信号/实践
1 鼠标滑过控件时触发  linkHovered
2 鼠标单机控件时触发  linkActivated
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap

class QLabelMethod(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.label1.setText('<font color = yellow>文本标签</font>')  # 可以添加 html 标签
        self.label1.setAutoFillBackground(True)  # 自动添加背景
        self.palette =QPalette()  # 调色板
        self.palette.setColor(QPalette.Window, Qt.blue)
        self.label1.setPalette(self.palette)
        self.label1.setAlignment(Qt.AlignCenter)  # 设置文本居中对齐


        self.label2.setText("<a href='#'>Pythont GUI 程序</a>")

        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setToolTip('This is image label')
        self.label3.setPixmap(QPixmap('./images_2/python.jpg'))

        self.label4.setOpenExternalLinks(True)  # 单击 label4 直接打开链接
        self.label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注</a>")
        self.label4.setAlignment(Qt.AlignRight)  # 右对齐
        self.label4.setToolTip('超链接')

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.label4)

        # 绑定事件
        self.label2.linkHovered.connect(self.linkHovered)
        # self.label4.linkActivated.connect(self.linkClicked)  # 上边设置打开链接 这一步就不会执行可以注释掉

        # 设置布局
        self.setLayout(vbox)
        self.setWindowTitle('QLabels')


    def linkHovered(self):

        print('当鼠标滑过 label2 触发')


    def linkClicked(self):

        print('当鼠标单击 label4 触发')






if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLabelMethod()
    main.show()

    sys.exit(app.exec_())
