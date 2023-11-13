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

    pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = MathMajorCourseSignTable()
    main.show()
    sys.exit(app.exec_())
