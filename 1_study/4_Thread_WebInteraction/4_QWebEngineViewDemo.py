# -*- coding: utf-8 -*-
# @time    : 2023/10/29 14:35
# @file    : 4_QWebEngineViewDemo.py
# @software: PyCharm

"""
QWebEngineView
Web 浏览器控件显示网页
PyQt5 与 Web 交互技术
同时使用 Python 和 Web 开发程序 混合开发
即 Python + JavaScript + HTML5 + CSS
"""
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *


class QWebEngineViewDemo(QWidget):

    def __init__(self):

        super(QWebEngineViewDemo, self).__init__()
        self.setWindowTitle('QWebEngineView Demo')
        self.setGeometry(5, 30, 1355, 730)

        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.baidui.com'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QWebEngineViewDemo()
    main.show()
    sys.exit(app.exec_())
