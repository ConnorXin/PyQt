# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/16 17:08
# @File    :  31_QCalendarWidgetDemo.py
# @IDE     :  PyCharm

"""
日历控件
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QCalendarWidgetDemo(QWidget):

    def __init__(self):

        super(QCalendarWidgetDemo, self).__init__()

        self.setWindowTitle('QCalendarWidget Demo')
        self.resize(600, 400)

        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(1988, 1, 1))  # 设置最小日期
        self.cal.setMaximumDate(QDate(2088, 1, 1))  # 设置最大日期

        self.cal.setGridVisible(True)  # 日历以网格形式显示
        self.cal.move(20, 20)
        self.cal.clicked.connect(self.showDate)

        # 设置 slot
        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20, 260)


    def showDate(self):

        self.label.setText((self.cal.selectedDate().toString('yyyy-MM-dd dddd')))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QCalendarWidgetDemo()
    main.show()
    sys.exit(app.exec_())
