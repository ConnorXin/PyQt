# -*- coding: utf-8 -*-
# @time    : 2023/8/5 13:25
# @author  : w-xin
# @file    : 23_QDialogDemo.py
# @software: PyCharm

"""
QDialog 对话框窗口

QDialog 是基类 是父类 是普通的对话框
在基类的基础上扩展了5个对话框
1 QMessageBox: 显示消息对话框
2 QColorDialog: 显示颜色对话框
3 QFileDialog: 打开/保存文件对话框
4 QFontDialog: 设置字体对话框
5 QInputDialog: 获取用户输入信息对话框
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QDialogDemo(QMainWindow):

    def __init__(self):

        super(QDialogDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QDialog Demo')
        self.resize(300, 200)

        self.button = QPushButton(self)  # 传入 self 直接把 button 放到窗口上
        self.button.setText('弹出对话框')
        self.button.move(50, 50)  # 设置 button 位置
        # click signal
        self.button.clicked.connect(self.showDialog)


    def showDialog(self):

        dialog = QDialog()
        # 在弹出的对话框中放置 button
        button = QPushButton('确定', dialog)
        # 绑定 slot 单击之后会关闭  自带的 slot
        button.clicked.connect(dialog.close)
        button.move(50, 50)
        dialog.setWindowTitle('Dialog')
        # 对话框以模式的状态显示
        # 当对话框显示时 MainWindow 所有的东西都是不可用的 除非将对话框关闭
        dialog.setWindowModality(Qt.ApplicationModal)
        # 显示对话框
        dialog.exec()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QDialogDemo()
    main.show()

    sys.exit(app.exec_())