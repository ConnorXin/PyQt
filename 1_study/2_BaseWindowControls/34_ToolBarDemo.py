# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/16 18:28
# @File    :  34_ToolBarDemo.py
# @IDE     :  PyCharm

"""
创建 使用工具栏
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ToolBarDemo(QMainWindow):

    def __init__(self):

        super(ToolBarDemo, self).__init__()

        self.setWindowTitle('ToolBar Demo')
        self.resize(300, 200)

        tb1 = self.addToolBar('File')  # 创建工具栏
        # 添加控件
        new = QAction(QIcon('./images/new.png'), 'new', self)
        tb1.addAction(new)  # 工具栏默认按钮是只显示图标 将文本作为悬停提示

        open = QAction(QIcon('./images/open.png'), 'open', self)
        tb1.addAction(open)

        save = QAction(QIcon('./images/save.png'), 'save', self)
        tb1.addAction(save)

        # 想让文本和图标都显示
        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)  # 图标在左 文本在右

        # 绑定 slot
        tb1.actionTriggered.connect(self.toolbtnPressed)

        # 第二个工具栏
        tb2 = self.addToolBar('Handle')
        newHandle = QAction(QIcon('./images/new.png'), '新建', self)
        tb2.addAction(newHandle)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


    def toolbtnPressed(self):

        print(self.sender().text(), 'be pressed.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ToolBarDemo()
    main.show()
    sys.exit(app.exec_())