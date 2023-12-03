# -*- coding: utf-8 -*-
# @time    : 2023/11/13 15:11
# @file    : 3_MathSignInTable_MajorCourse_v2.py
# @software: PyCharm

"""
plus pyqt version
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget


class MathMajorCourseSignTable(QWidget):

    def __init__(self):

        super(MathMajorCourseSignTable, self).__init__()
        self.setWindowTitle('专业课签到表')
        self.resize(500, 300)





if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MathMajorCourseSignTable()
    main.show()
    sys.exit(app.exec_())
