# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/3 13:26
# @File    :  12_QPushButton.py
# @IDE     :  PyCharm

"""
按钮控件都有一个父类叫 QAbstractButton

按钮控件有
按钮：QPushButton
工具按钮：AToolButton
单选按钮：QRadioButton
多选按钮：QCheckBox

12_QPushButton.py
QPushButton 也要 QCheckBox 的特性
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPushButtonDemo(QDialog):

    def __init__(self):

        super(QPushButtonDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QPushButton Demo')
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.button1 = QPushButton('First Button')
        self.button1.setText('FirstButton')  # 设置 (修改) 文本
        # 设置可复选
        self.button1.setCheckable(True)
        self.button1.toggle()  # 按钮按下就处于选中状态
        # signal
        self.button1.clicked.connect(lambda: self.whichButtonMethod1(self.button1))  # 使用 lambda 表达式进行传参 不然会报错
        self.button1.clicked.connect(self.buttonStatu)

        layout.addWidget(self.button1)


        # TODO 在文本前面显示图像
        self.button2 = QPushButton('IMG PushButton')
        self.button2.setIcon(QIcon(QPixmap('./images_1/python.png')))  # 添加图像
        # signal
        self.button2.clicked.connect(lambda: self.whichButtonMethod1(self.button2))

        layout.addWidget(self.button2)

        # TODO 设置按钮不可用
        self.button3 = QPushButton('Set PushButton Unenable')
        self.button3.setEnabled(False)
        layout.addWidget(self.button3)

        # TODO 设置默认按钮
        # 即按 Enter 键自动调用默认按钮
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)  # 默认按钮一个窗口只能有一个
        self.button4.clicked.connect(lambda: self.whichButtonMethod1(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)


    def buttonStatu(self):

        if self.button1.isChecked():
            print(self.button1.text() + '已被选中')
        else:
            print(self.button1.text() + '未被选中')


    def whichButtonMethod1(self, btn):
        """
        多个按钮的单击 signal 同时使用这个 slot
        直接传参 def whichButton(self, btn):
        :return:
        """
        print('被单击的按钮是<' + btn.text() + '>')


    def whichButtonMethod2(self):
        """
        方法二  直接在方法里面使用 self.sender 进行获取当前控件
        :return:
        """
        button = self.sender()



if __name__ == '__main__':

    app = QApplication(sys.argv)

    main = QPushButtonDemo()
    main.show()

    sys.exit(app.exec_())
