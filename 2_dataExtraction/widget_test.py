# -*- coding: utf-8 -*-
# @Time    :  2023/12/12 14:32
# @File    :  widget_test.py
# @IDE     :  PyCharm

"""
"""

from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')  # 初始状态栏消息

        # left_label = QLabel('Left side message', self)  # 左侧消息
        right_label = QLabel('Right side message', self)  # 右侧消息

        # self.statusBar().addWidget(left_label)  # 在状态栏左侧添加小部件
        self.statusBar().addPermanentWidget(right_label)  # 在状态栏右侧添加小部件
        self.statusBar().showMessage(status_info)

        self.setGeometry(300, 200, 500, 300)
        self.setWindowTitle('Status Bar Example')


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
