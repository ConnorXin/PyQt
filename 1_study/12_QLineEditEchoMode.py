# -*- coding: utf-8 -*-
# @time    : 2023/7/30 15:28
# @author  : w-xin
# @file    : 12_QLineEditEchoMode.py
# @software: PyCharm

"""
QLineEdit 的回显模式 EchoMode
可以输入单行文本

回显模式 EchoMode
支持4钟回显模式
1 Normal: 输入文本后能够在输入框中正常显示
2 NoEcho: 输入文本不在输入框中显示 即不回显
3 Password: 密码输入全程会隐藏密码
4 PasswordEchoOnEdit: 密码输入时会显示 编辑完成然后再隐藏
"""
import sys
from PyQt5.QtWidgets import *


class QLineEditEchoMode(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QLineEditEchoMode')

        formLayout = QFormLayout()  # 表单布局

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoEditLineEdit = QLineEdit()

        formLayout.addRow('Normal', normalLineEdit)
        formLayout.addRow('NoEcho', noEchoLineEdit)
        formLayout.addRow('Password', passwordLineEdit)
        formLayout.addRow('PasswordEchoOnEdit', passwordEchoEditLineEdit)

        # 未输入时显示提示
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoEditLineEdit.setPlaceholderText('passwordEcho')

        # 设置 Echo 模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 应用表单布局
        self.setLayout(formLayout)




if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())
