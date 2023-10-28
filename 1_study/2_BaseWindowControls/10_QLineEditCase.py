# -*- coding: utf-8 -*-
# @time    : 2023/7/30 16:25
# @author  : w-xin
# @file    : 10_QLineEditCase.py
# @software: PyCharm

"""
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class QLineEditCase(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QLineEdit 综合案例')

        edit1 = QLineEdit()

        # int 校验
        edit1.setValidator(QIntValidator())  # 所有 int 都可
        edit1.setMaxLength(4)  # 最大长度为4
        edit1.setAlignment(Qt.AlignRight)
        # edit1.setFont(QFont('Arial', 10))

        # double 校验
        edit2 = QLineEdit()
        # 0.99-99.99 精度为2
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # mark 校验
        edit3 = QLineEdit()
        edit3.setInputMask('99_9999_999999;#')

        edit4 = QLineEdit()
        edit4.textChanged().connect(self.textChang)

        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished().connect(self.enterPress)

        edit6 = QLineEdit('Hello PyQt5')
        edit6.setReadOnly(True)  # 设置只读


        # 表单布局
        formLayout = QFormLayout()
        formLayout.addRow('整数校验', edit1)
        formLayout.addRow('浮点数校验', edit2)
        formLayout.addRow('掩码校验', edit3)
        formLayout.addRow('改变文本', edit4)
        formLayout.addRow('密码', edit5)
        formLayout.addRow('只读文本', edit6)

        self.setLayout(formLayout)


    def textChange(self, text):

        print('输入的内容' + text)


    def enterPress(self):

        print('已输入')


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLineEditCase()
    main.show()

    sys.exit(app.exec_())
