# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 12:05
# @File    :  4_QTableWidgetDemo.py
# @IDE     :  PyCharm

"""
QListWidget
扩展的表格控件

每一个 Cell 是一个 QTableWidgetItem
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTableWidgetDemo(QWidget):

    def __init__(self):

        super(QTableWidgetDemo, self).__init__()

        self.setWindowTitle('QTableWidget Demo')
        self.resize(600, 400)

        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)  # 设置行数
        tableWidget.setColumnCount(3)  # 设置列数

        tableWidget.setHorizontalHeaderLabels(['name', 'age', 'address'])  # 字段名
        nameItem = QTableWidgetItem('connor')
        tableWidget.setItem(0, 0, nameItem)

        ageItem = QTableWidgetItem('21')
        tableWidget.setItem(0, 1, ageItem)

        addressItem = QTableWidgetItem('Shenzhen')
        tableWidget.setItem(0, 2, addressItem)

        # 设置禁止编辑
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置整行选择
        tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 根据数据长度调整单元格大小
        tableWidget.resizeColumnsToContents()
        tableWidget.resizeRowsToContents()

        # 表头 索引 隐藏
        tableWidget.horizontalHeader().setVisible(False)
        tableWidget.verticalHeader().setVisible(False)

        # 隐藏表格线
        tableWidget.setShowGrid(False)

        layout.addWidget(tableWidget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QTableWidgetDemo()
    main.show()
    sys.exit(app.exec_())