# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 13:25
# @File    :  45_QTreeWidgetDemo.py
# @IDE     :  PyCharm

"""
QTreeWidget
树控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTreeWidgetDemo(QMainWindow):

    def __init__(self):

        super(QTreeWidgetDemo, self).__init__()

        self.setWindowTitle('QTreeWidget Demo')
        self.resize(600, 400)

        self.tree = QTreeWidget()

        # 指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(['key', 'value'])

        root = QTreeWidgetItem(self.tree)
        root.setText(0, 'root')
        self.tree.setColumnWidth(0, 120)  # 设定列宽

        # 添加子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '子节点1的数据')


        self.setCentralWidget(self.tree)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTreeWidgetDemo()
    main.show()
    sys.exit(app.exec_())