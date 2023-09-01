# -*- coding: utf-8 -*-
# @time    : 2023/8/6 14:11
# @author  : w-xin
# @file    : 35_PasteDemo.py
# @software: PyCharm

"""
使用剪贴板
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class PasteDemo(QDialog):

    def __init__(self):

        super(PasteDemo, self).__init__()

        self.setWindowTitle('Paste Demo')
        self.resize(300, 400)

        layout = QGridLayout()

        textCopyButton = QPushButton('Copy Text')
        textPasteButton = QPushButton('Paste Text')

        htmlCopyButton = QPushButton('Copy HTML')
        htmlPasteButton = QPushButton('Paste HTML')

        imageCopyButton = QPushButton('Copy IMG')
        imagePasteButton = QPushButton('Paste IMG')

        self.textLabel = QLabel('默认文本')
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(QPixmap('./images_3/book1.png'))

        layout.addWidget(textCopyButton, 0, 0)
        layout.addWidget(htmlCopyButton, 0, 1)
        layout.addWidget(imageCopyButton, 0, 2)

        layout.addWidget(textPasteButton, 1, 0)
        layout.addWidget(htmlPasteButton, 1, 1)
        layout.addWidget(imagePasteButton, 1, 2)

        layout.addWidget(self.textLabel, 2, 0)
        layout.addWidget(self.imageLabel, 2, 1)

        self.setLayout(layout)

        # signal
        textCopyButton.clicked.connect(self.copyText)
        textPasteButton.clicked.connect(self.pasteText)
        htmlCopyButton.clicked.connect(self.copyHtml)
        htmlPasteButton.clicked.connect(self.pasteHtml)
        imageCopyButton.clicked.connect(self.copyImg)
        imagePasteButton.clicked.connect(self.pasteImg)


    def copyText(self):

        clipboard = QApplication.clipboard()
        clipboard.setText('Hello World')


    def pasteText(self):

        clipboard = QApplication.clipboard()
        self.textLabel.setText(clipboard.text())


    def copyHtml(self):

        mimeData = QMimeData()
        mimeData.setHtml('<b>Bold and <font color=red>Red</font></b>')
        clipboard = QApplication.clipboard()
        clipboard.setMimeData(mimeData)


    def pasteHtml(self):

        clipboard = QApplication.clipboard()
        mimeData = clipboard.mimeData()
        if mimeData.hasHtml():
            self.textLabel.setText(mimeData.html())


    def copyImg(self):

        clipboard = QApplication.clipboard()
        clipboard.setPixmap(QPixmap('./images_1/python.png'))


    def pasteImg(self):

        clipboard = QApplication.clipboard()
        self.imageLabel.setPixmap(clipboard.pixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = PasteDemo()
    main.show()
    sys.exit(app.exec_())