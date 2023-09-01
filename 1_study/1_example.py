# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/7/28 13:59
# @File    :  1_example.py
# @IDE     :  PyCharm

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


def handleCalc():


    info = textEdit.toPlainText()  # 获取用户输入文本

    # 薪资 20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    QMessageBox.about(window, '统计结果',  # 弹出结果对话框
                      f'''薪资20000 以上的有：\n{salary_above_20k}\n薪资20000 以下的有：\n{salary_below_20k}''')



if __name__ == '__main__':


    app = QApplication()
    # QApplication 提供了整个图形界面程序的底层管理功能
    # 比如：初始化、程序入口参数的处理，用户事件（对界面的点击、输入、拖拽）分发给各个对应的控件，等等...
    # QApplication 要做如此重要的初始化操作，因此必须在任何界面控件对象创建前先创建它

    # QMainWindow、QPlainTextEdit、QPushButton 是3个控件类，分别对应界面的主窗口、文本框、按钮
    # 他们都是控件基类对象 QWidget 的子类
    window = QMainWindow()
    window.resize(500, 400)
    window.move(300, 310)
    window.setWindowTitle('薪资统计')  # 标题栏

    textEdit = QPlainTextEdit(window)  # window 是对应的父控件
    # 在 Qt 系统中，控件 (widget) 是层层嵌套 的，除了最顶层的控件，其他的控件都有父控件
    textEdit.setPlaceholderText("请输入薪资表")  # 输入提示
    textEdit.move(10, 25)  # 相对父控件的位置
    textEdit.resize(300, 350)

    button = QPushButton('统计', window)
    button.move(380, 80)
    button.clicked.connect(handleCalc)  # 点击信号 连接到 handleCalc 函数

    window.show()

    app.exec_()
