# -*- coding: utf-8 -*-
# @time    : 2023/7/30 15:49
# @author  : w-xin
# @file    : 8_QLineEditLimitInput.py
# @software: PyCharm

"""
QLineEdit 控件的校验器
可以限制 QLineEdit 的输入

如限制只能输入整数、浮点数或满足一定条件的字符串
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditLimitInput(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('LimitInput')

        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('IntType', intLineEdit)
        formLayout.addRow('DoubleType', doubleLineEdit)
        formLayout.addRow('ValidatorType', validatorLineEdit)

        # 整数校验
        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)  # 设置范围 1-99

        # 浮点数校验
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 标准表示法
        doubleValidator.setDecimals(2)  # 设置精度 小数点后两位

        # 字符和数字 传入正则表达式
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 校验器与输入框绑定
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        # 放入表单布局
        self.setLayout(formLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLineEditLimitInput()
    main.show()

    sys.exit(app.exec_())