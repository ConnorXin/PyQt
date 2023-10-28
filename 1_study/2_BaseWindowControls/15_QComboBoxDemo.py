# -*- coding: utf-8 -*-
# @time    : 2023/8/4 10:01
# @author  : w-xin
# @file    : 15_QComboBoxDemo.py
# @software: PyCharm

"""
QComboBoxDemo 下拉框选项

1 如何将列表项添加到 QComboBox 控件中
2 如何获取选中的列表项
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QComboBoxDemo(QWidget):

    def __init__(self):

        super(QComboBoxDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QComboBox Demo')
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.label = QLabel('Please Select Language')

        self.cb = QComboBox()
        # 添加选项
        self.cb.addItem('C++')
        self.cb.addItem('Python')
        self.cb.addItems(['Java', 'C#', 'Golong', 'Ruby'])

        # currentIndexChanged 是当前的索引变化  每一个项都有一个索引
        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)


        self.setLayout(layout)


    def selectionChange(self, i):
        """

        :param i: 索引
        :return:
        """
        self.label.setText(self.cb.currentText())  # 得到当前选择的文本
        self.label.adjustSize()  # 根据设置文本调节尺寸

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index', i, 'selection changed', self.cb.currentText())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QComboBoxDemo()
    main.show()

    sys.exit(app.exec_())

