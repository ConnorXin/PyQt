# -*- coding: utf-8 -*-
# @time    : 2023/7/29 15:41
# @author  : w-xin
# @file    : 2_ui2py.py
# @software: PyCharm

"""
ui 文件转为 py 文件
要将 ui 中的功能嵌在 pycharm 中
"""
import sys
from stats import *
from PySide2.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QMainWindow


if __name__ == '__main__':

    # 1 在 cmd 中使用命令行  python -m PyQt5.uic.pyuic xxx.ui -o xxx.py
    # 2 pyuic5 xxx.ui -o xxx.py

    # 从文件中加载 UI 定义
    # qfile_stats = QFile('stats.ui')
    # qfile_stats.open(QFile.ReadOnly)
    # qfile_stats.close()  # 最终要记得 close


    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_Form()
    ui.setupUi(mainWindow)

    mainWindow.show()
    sys.exit(app.exec_())