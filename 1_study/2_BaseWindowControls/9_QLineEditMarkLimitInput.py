# -*- coding: utf-8 -*-
# @time    : 2023/7/30 16:07
# @author  : w-xin
# @file    : 9_QLineEditMarkLimitInput.py
# @software: PyCharm

"""
使用掩码限制 QLineEdit 输入

A    ASCII字母字符是必须输入的(A-Z、a-z)
a    ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)
N    ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n    ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)
X    任何字符都是必须输入的
x    任何字符都是允许输入的,但不是必需的
9    ASCII数字字符是必须输入的(0-9)
0    ASCII数字字符是允许输入的,但不是必需的(0-9)
D    ASCII数字字符是必须输入的(1-9)
d    ASCII数字字符是允许输入的,但不是必需的(1-9)
#    ASCI数字字符或加减符号是允许输入的,但不是必需的
H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
B    二进制格式字符是必须输入的(0,1)
b    二进制格式字符是允许输入的,但不是必需的(0,1)
>    所有的字母字符都大写
<    所有的字母字符都小写
!    关闭大小写转换
\    使用"\"转义上面列出的字符
"""
import sys
from PyQt5.QtWidgets import *


class QLineEditMarkLimitInput(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('Mark to limit input')

        formLayout = QFormLayout()

        ipLineEdit = QLineEdit()
        macLineEdit = QLineEdit()
        dateLineEdit = QLineEdit()
        licenseLineEdit = QLineEdit()

        # 设置掩码限制 ip  192.168.21.45 每一段至多3位数字
        ipLineEdit.setInputMask('000.000.000.000;_')  # _ 表示没有输入时显示下划线

        # mac 地址一般是两位 六段
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')

        # 限制日期
        dateLineEdit.setInputMask('0000-00-00')

        # 限制许可验证
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')

        formLayout.addRow('ipMark', ipLineEdit)
        formLayout.addRow('macMark', macLineEdit)
        formLayout.addRow('dateMark', dateLineEdit)
        formLayout.addRow('licenseMark', licenseLineEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLineEditMarkLimitInput()
    main.show()

    sys.exit(app.exec_())