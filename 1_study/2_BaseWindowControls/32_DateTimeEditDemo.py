# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/16 17:33
# @File    :  32_DateTimeEditDemo.py
# @IDE     :  PyCharm

"""

"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DateTimeEditDemo(QWidget):

    def __init__(self):

        super(DateTimeEditDemo, self).__init__()

        vlayout = QVBoxLayout()
        dateTimeEdit1 = QDateTimeEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())  # 传入当前时间

        dateEdit = QDateTimeEdit(QDate.currentDate())  # 传入当前日期
        timeEdit = QDateTimeEdit(QTime.currentTime())  # 仅传入当前时间

        # 设置格式
        dateTimeEdit1.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        dateTimeEdit2.setDisplayFormat('yyyy/MM/dd HH-mm-ss')
        dateEdit.setDisplayFormat('yyyy.MM.dd')
        timeEdit.setDisplayFormat('HH:mm:ss')

        # 设置范围
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit1.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit = dateTimeEdit1

        # 设置样式
        dateTimeEdit2.setCalendarPopup(True)  # 设置成下拉框选项

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)

        # 获取设置的日期和时间
        self.btn = QPushButton('Get Date And Time')
        self.btn.clicked.connect(self.onBtnClicked)

        self.setLayout(vlayout)

        dateTimeEdit1.dateChanged.connect(self.onDateChanged)
        dateTimeEdit1.timeChanged.connect(self.onTimeChanged)
        dateTimeEdit1.dateTimeChanged.connect(self.onDateTimeChanged)


    def onDateChanged(self, date):
        """
        日期变化的 slot
        :return:
        """
        print(date)


    def onTimeChanged(self, time):
        """
        时间变化的 slot
        :return:
        """
        print(time)


    def onDateTimeChanged(self, datetime):
        """
        日期和时间变化的 slot
        :return:
        """
        print(datetime)


    def onBtnClicked(self):

        dateTime = self.dateTimeEdit.dateTime()
        print(dateTime)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = DateTimeEditDemo()
    main.show()
    sys.exit(app.exec_())