# -*- coding: utf-8 -*-
# @time    : 2023/8/5 20:50
# @author  : w-xin
# @file    : 28_QFileDialogDemo.py
# @software: PyCharm

"""
QFileDialog 文件对话框

打开/保存文件对话框
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QFileDialogDemo(QWidget):

    def __init__(self):

        super(QFileDialogDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QFileDialog Demo')
        self.resize(600, 400)

        layout = QVBoxLayout()

        # 图像加载
        self.buttonLoadIMG = QPushButton('Load IMG')
        self.buttonLoadIMG.clicked.connect(self.loadIMG)
        layout.addWidget(self.buttonLoadIMG)

        # 加载图像并且显示到 label 上
        self.labelIMG = QLabel()
        layout.addWidget(self.labelIMG)

        # 文本加载
        self.buttonLoadText = QPushButton('Load Text')
        self.buttonLoadText.clicked.connect(self.loadText)
        layout.addWidget(self.buttonLoadText)

        # 加载文本文件并且加载到 QTextEdit 上
        self.contexts = QTextEdit()
        layout.addWidget(self.contexts)

        self.setLayout(layout)


    def loadIMG(self):

        # '打开文件': 窗口标题
        # './': 打开后默认路径
        # 'IMG File (*.jpg *.png)': 可选择的文件类型
        # fname: 返回文件路径
        # _: 是否取消的参数  不想返回即用 _ 表示
        fname, _ = QFileDialog.getOpenFileName(self, '打开文件', './', 'IMG File (*.jpg *.png)')
        self.labelIMG.setPixmap(QPixmap(fname))
        self.labelIMG.setAlignment(Qt.AlignCenter)


    def loadText(self):
        """
        直接创建 FileDialog 进行打开文件
        :return:
        """
        dialog = QFileDialog()
        # 设置打开文件类型
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            filenames = dialog.selectedFiles()
            f = open(filenames[0], mode = 'r', encoding = 'utf-8')
            with f:
                data = f.read()
                self.contexts.setText(data)


if __name__ == '__main__':

    app =QApplication(sys.argv)
    main = QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())