# -*- coding: utf-8 -*-
# @time    : 2023/10/26 9:38
# @file    : 49_MultiWindowsDemo.py
# @software: PyCharm

"""
容纳多文档的窗口
在一个窗口中 可以创建多个子窗口
子窗口不能离开主窗口范围
QMdiArea: 窗口的容器
QMdiSubWindow: 容纳多文档的窗口
"""
import sys
from PyQt5.QtWidgets import *


class MultiWindowsDemo(QMainWindow):

    # 计数当前窗口
    count = 0

    def __init__(self):

        super(MultiWindowsDemo, self).__init__()
        self.setWindowTitle('MultiWindows Demo')

        # 容纳多文档的容器对象
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)  # 添加到布局
        # 添加菜单
        bar = self.menuBar()
        file = bar.addMenu('File')
        file.addAction('New')
        # 多文档有层叠 平铺两种排列方式
        file.addAction('cascade')  # 层叠
        file.addAction('Tiled')  # 平铺

        # 槽
        file.triggered.connect(self.windowaction)


    def windowaction(self, q):

        if q.text() == 'New':
            MultiWindowsDemo.count += 1
            # 创建子窗口
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle('window_son_' + str(MultiWindowsDemo.count))
            # 将子窗口添加到容器
            self.mdi.addSubWindow(sub)
            # 显示子窗口
            sub.show()
            print(MultiWindowsDemo.count)
        elif q.text() == 'cascade':
            self.mdi.cascadeSubWindows()
        elif q.text() == 'Tiled':
            self.mdi.tileSubWindows()




if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MultiWindowsDemo()
    main.show()
    sys.exit(app.exec_())
