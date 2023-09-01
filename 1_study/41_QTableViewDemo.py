# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/17 12:46
# @File    :  41_QTableViewDemo.py
# @IDE     :  PyCharm

"""
显示关系型二维表数据
需要创建 QTableView 实例和一个数据源 (Model) 然后将两者关联
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTableViewDemo(QWidget):

    def __init__(self):

        super(QTableViewDemo, self).__init__()

        self.setWindowTitle('QTableView Demo')
        self.resize(600, 400)

        # 使用一个最标准的 Model
        self.model = QStandardItemModel(4, 3)  # 4 行 3 列
        self.model.setHorizontalHeaderLabels(['id', 'name', 'age', 'id', 'name', 'age', 'id', 'name', 'age', 'id', 'name', 'age'])  # 字段
        self.tableView = QTableView()
        self.tableView.setModel(self.model)  # 关联模型

        # 添加数据
        item11 = QStandardItem('10')
        item12 = QStandardItem('connor')
        item13 = QStandardItem('2000')
        self.model.setItem(0, 0, item11)
        self.model.setItem(0, 1, item12)
        self.model.setItem(0, 2, item13)

        layout = QVBoxLayout()
        layout.addWidget(self.tableView)

        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableViewDemo()
    main.show()
    sys.exit(app.exec_())
