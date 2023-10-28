# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/16 18:14
# @File    :  33_MenuDemo.py
# @IDE     :  PyCharm

"""
创建顶层菜单
"""
import sys
from PyQt5.QtWidgets import *


class MenuDemo(QMainWindow):

    def __init__(self):

        super(MenuDemo, self).__init__()

        bar = self.menuBar()  # 获取菜单栏

        # 向菜单栏中添加子菜单栏
        file = bar.addMenu('文件')
        file.addAction('新建')  # 创建方法一

        save = QAction('保存', self)  # 创建方法二
        save.setShortcut('Ctrl + S')  # 设置快捷键
        file.addAction(save)

        # 绑定 slot
        save.triggered.connect(self.process)


    def process(self):

        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MenuDemo()
    main.show()
    sys.exit(app.exec_())

