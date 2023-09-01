# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 11:52
# @File    :  42_QListViewDemo.py
# @IDE     :  PyCharm

"""
QListView
显示列表数据
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QListViewDemo(QWidget):

    def __init__(self):

        super(QListViewDemo, self).__init__()

        self.setWindowTitle('QListView Demo')
        self.resize(600, 400)

        layout = QVBoxLayout()

        listView = QListView()
        listModel = QStringListModel()
        self.list = ['list1', 'list2', 'list3', 'list4']

        # 数据放入模型
        listModel.setStringList(self.list)
        listView.setModel(listModel)

        # 绑定 slot
        listView.clicked.connect(self.clicked)

        layout.addWidget(listView)
        self.setLayout(layout)


    def clicked(self, item):

        QMessageBox.information(self, 'QListView', 'selected ' + self.list[item.row()])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QListViewDemo()
    main.show()
    sys.exit(app.exec_())