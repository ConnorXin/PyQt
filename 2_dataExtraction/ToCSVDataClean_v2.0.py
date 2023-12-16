# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 13:37
# @File    :  ToCSVDataClean_v2.0.py
# @IDE     :  PyCharm


"""
add
1 添加功能选择窗口
2 字体 大小 设置
3 添加 Html 提取数据功能
4 提取时添加线程睡眠时间
5 添加清洗模块
"""
import os
import sys
import time
import json
import traceback

import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


# Head Window
class HeadWindow(QWidget):

    def __init__(self):

        super(HeadWindow, self).__init__()

        self.setWindowTitle('功能选择')
        self.resize(300, 100)
        layout = QVBoxLayout()

        buttonDataExtract = QPushButton('数据提取')
        buttonDataExtract.setFont(QFont('幼圆', 13))

        buttonDataClean = QPushButton('数据清洗')
        buttonDataClean.setFont(QFont('幼圆', 13))

        layout.addWidget(buttonDataExtract)
        layout.addWidget(buttonDataClean)
        self.setLayout(layout)

        buttonDataExtract.clicked.connect(self.ExtractClicked)
        buttonDataClean.clicked.connect(self.CleanClicked)

    def ExtractClicked(self):

        self.hide()
        self.tocsv = SelectType()
        self.tocsv.show()

    def CleanClicked(self):

        self.hide()
        self.handle = HandleUI()
        self.handle.show()


# to csv window1
class SelectType(QWidget):

    def __init__(self):

        super(SelectType, self).__init__()

        self.setWindowTitle('数据选择')
        self.resize(300, 100)

        layout = QVBoxLayout()

        buttonJson = QPushButton('Json')
        buttonJson.setFont(QFont('幼圆', 13))

        buttonHtml = QPushButton('Html')
        buttonHtml.setFont(QFont('幼圆', 13))

        layout.addWidget(buttonJson)
        layout.addWidget(buttonHtml)
        self.setLayout(layout)

        buttonJson.clicked.connect(self.JsonClicked)
        buttonHtml.clicked.connect(self.HtmlClicked)

    def JsonClicked(self):

        self.hide()
        self.tocsv = Json2Csv()
        self.tocsv.show()

    def HtmlClicked(self):

        self.hide()
        self.tocsv = Html2Csv()
        self.tocsv.show()


# to csv window2
class Json2Csv(QWidget):

    def __init__(self):
        super(Json2Csv, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('数据提取')
        self.resize(500, 300)

        self.pathLabel = QLabel('文件路径')
        self.pathEdit = QLineEdit()
        self.fileCoverNameLabel = QLabel('文件判断')
        self.fileCoverNameEdit = QLineEdit()
        self.saveNameLabel = QLabel('文件名称')
        self.saveNameEdit = QLineEdit()
        self.keyNumLabel = QLabel('字典键数')
        self.keyNumEdit = QLineEdit()
        self.keyNumEdit.setValidator(QIntValidator())

        self.pathLabel.setFont(QFont('幼圆', 12))
        self.pathEdit.setFont(QFont('幼圆', 12))
        self.fileCoverNameLabel.setFont(QFont('幼圆', 12))
        self.fileCoverNameEdit.setFont(QFont('幼圆', 12))
        self.saveNameLabel.setFont(QFont('幼圆', 12))
        self.saveNameEdit.setFont(QFont('幼圆', 12))
        self.keyNumLabel.setFont(QFont('幼圆', 12))
        self.keyNumEdit.setFont(QFont('幼圆', 12))

        layout = QGridLayout()
        # layout.setSpacing(10)
        layout.addWidget(self.pathLabel, 1, 0)
        layout.addWidget(self.pathEdit, 1, 1, 1, 4)
        layout.addWidget(self.fileCoverNameLabel, 2, 0)
        layout.addWidget(self.fileCoverNameEdit, 2, 1, 1, 4)
        layout.addWidget(self.saveNameLabel, 3, 0)
        layout.addWidget(self.saveNameEdit, 3, 1, 1, 4)
        layout.addWidget(self.keyNumLabel, 4, 0)
        layout.addWidget(self.keyNumEdit, 4, 1, 1, 4)

        self.buttonNext = QPushButton('下一步')
        self.buttonNext.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonNext, 5, 4)

        self.buttonReturn = QPushButton('返回')
        self.buttonReturn.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonReturn, 5, 3)
        self.setLayout(layout)

        self.buttonNext.clicked.connect(self.nextonClick)
        self.buttonReturn.clicked.connect(self.returnonClick)

    def nextonClick(self):
        self.hide()
        self.next = JsonNextClick(self.pathEdit, self.fileCoverNameEdit,
                              self.saveNameEdit, self.keyNumEdit)
        self.next.show()

    def returnonClick(self):

        self.hide()
        self.returnWin = HeadWindow()
        self.returnWin.show()


# to csv window3
class JsonNextClick(QWidget):

    def __init__(self, pathEdit, fileCoverNameEdit, saveNameEdit, keyNumEdit):

        super(JsonNextClick, self).__init__()
        self.pathEdit = pathEdit
        self.fileCoverNameEdit = fileCoverNameEdit
        self.saveNameEdit = saveNameEdit
        self.keyNumEdit = keyNumEdit
        self.initNextUI()

    def initNextUI(self):

        keyNum = self.keyNumEdit.text()
        if int(keyNum) == 1:
            self.setWindowTitle('数据提取')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_1Label.setFont(QFont('幼圆', 12))
            self.dic_1Edit.setFont(QFont('幼圆', 12))

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            self.buttonNext.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonNext, 5, 4)

            self.buttonReturn = QPushButton('返回')
            self.buttonReturn.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonReturn, 5, 3)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
            self.buttonReturn.clicked.connect(self.returnonClick)
        elif int(keyNum) == 2:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()
            self.dic_1Label.setFont(QFont('幼圆', 12))
            self.dic_1Edit.setFont(QFont('幼圆', 12))
            self.dic_2Label.setFont(QFont('幼圆', 12))
            self.dic_2Edit.setFont(QFont('幼圆', 12))

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            self.buttonNext.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonNext, 5, 4)

            self.buttonReturn = QPushButton('返回')
            self.buttonReturn.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonReturn, 5, 3)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
            self.buttonReturn.clicked.connect(self.returnonClick)
        elif int(keyNum) == 31:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()
            self.dic_3Label = QLabel('字典3')
            self.dic_3Edit = QLineEdit()
            self.dic_1Label.setFont(QFont('幼圆', 12))
            self.dic_1Edit.setFont(QFont('幼圆', 12))
            self.dic_2Label.setFont(QFont('幼圆', 12))
            self.dic_2Edit.setFont(QFont('幼圆', 12))
            self.dic_3Label.setFont(QFont('幼圆', 12))
            self.dic_3Edit.setFont(QFont('幼圆', 12))

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)
            layout.addWidget(self.dic_3Label, 3, 0)
            layout.addWidget(self.dic_3Edit, 3, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            self.buttonNext.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonNext, 5, 4)

            self.buttonReturn = QPushButton('返回')
            self.buttonReturn.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonReturn, 5, 3)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
            self.buttonReturn.clicked.connect(self.returnonClick)
        elif int(keyNum) == 32:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()
            self.dic_3Label = QLabel('字典3')
            self.dic_3Edit = QLineEdit()
            self.dic_1Label.setFont(QFont('幼圆', 12))
            self.dic_1Edit.setFont(QFont('幼圆', 12))
            self.dic_2Label.setFont(QFont('幼圆', 12))
            self.dic_2Edit.setFont(QFont('幼圆', 12))
            self.dic_3Label.setFont(QFont('幼圆', 12))
            self.dic_3Edit.setFont(QFont('幼圆', 12))

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)
            layout.addWidget(self.dic_3Label, 3, 0)
            layout.addWidget(self.dic_3Edit, 3, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            self.buttonNext.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonNext, 5, 4)

            self.buttonReturn = QPushButton('返回')
            self.buttonReturn.setFont(QFont('幼圆', 10))
            layout.addWidget(self.buttonReturn, 5, 3)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
            self.buttonReturn.clicked.connect(self.returnonClick)

    def nextonClick(self):

        self.hide()
        if int(self.keyNumEdit.text()) == 1:
            self.save = JsonToSave(self.pathEdit, self.fileCoverNameEdit,
                                   self.saveNameEdit, self.keyNumEdit, self.dic_1Edit)
        elif int(self.keyNumEdit.text()) == 2:
            self.save = JsonToSave(self.pathEdit, self.fileCoverNameEdit,
                                   self.saveNameEdit, self.keyNumEdit,
                                   (self.dic_1Edit, self.dic_2Edit))

        elif int(self.keyNumEdit.text()) == 31:
            self.save = JsonToSave(self.pathEdit, self.fileCoverNameEdit,
                                   self.saveNameEdit, self.keyNumEdit, (self.dic_1Edit,
                                                                        self.dic_2Edit, self.dic_3Edit))
        elif int(self.keyNumEdit.text()) == 32:
            self.save = JsonToSave(self.pathEdit, self.fileCoverNameEdit,
                                   self.saveNameEdit, self.keyNumEdit, (self.dic_1Edit, self.dic_2Edit, self.dic_3Edit))
        self.save.show()


    def returnonClick(self):

        self.hide()
        self.head = Json2Csv()
        self.head.show()


# to csv window4
class Html2Csv(QWidget):

    def __init__(self):

        super(Html2Csv, self).__init__()

        self.setWindowTitle('数据提取')
        self.resize(500, 300)

        self.pathLabel = QLabel('文件路径')
        self.pathEdit = QLineEdit()
        self.fileCoverNameLabel = QLabel('文件判断')
        self.fileCoverNameEdit = QLineEdit()
        self.saveNameLabel = QLabel('文件名称')
        self.saveNameEdit = QLineEdit()

        self.pathLabel.setFont(QFont('幼圆', 12))
        self.pathEdit.setFont(QFont('幼圆', 12))
        self.fileCoverNameLabel.setFont(QFont('幼圆', 12))
        self.fileCoverNameEdit.setFont(QFont('幼圆', 12))
        self.saveNameLabel.setFont(QFont('幼圆', 12))
        self.saveNameEdit.setFont(QFont('幼圆', 12))

        layout = QGridLayout()
        layout.addWidget(self.pathLabel, 1, 0)
        layout.addWidget(self.pathEdit, 1, 1, 1, 4)
        layout.addWidget(self.fileCoverNameLabel, 2, 0)
        layout.addWidget(self.fileCoverNameEdit, 2, 1, 1, 4)
        layout.addWidget(self.saveNameLabel, 3, 0)
        layout.addWidget(self.saveNameEdit, 3, 1, 1, 4)

        self.buttonNext = QPushButton('下一步')
        self.buttonNext.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonNext, 5, 4)

        self.buttonReturn = QPushButton('返回')
        self.buttonReturn.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonReturn, 5, 3)
        self.setLayout(layout)

        self.buttonNext.clicked.connect(self.nextonClick)
        self.buttonReturn.clicked.connect(self.returnonClick)

    def nextonClick(self):
        self.hide()
        self.next = HtmlToSave(self.pathEdit, self.fileCoverNameEdit, self.saveNameEdit)
        self.next.show()

    def returnonClick(self):

        self.hide()
        self.returnWin = HeadWindow()
        self.returnWin.show()


# to csv window5
class JsonToSave(QWidget):

    def __init__(self, pathEdit, fileCoverNameEdit, saveNameEdit, keyNumEdit, dic):

        super(JsonToSave, self).__init__()

        self.pathEdit = pathEdit
        self.fileCoverNameEdit = fileCoverNameEdit
        self.saveNameEdit = saveNameEdit
        self.keyNumEdit = keyNumEdit


        if int(self.keyNumEdit.text()) == 1:
            self.dic_1Edit = dic
        elif int(self.keyNumEdit.text()) == 2:
            self.dic_1Edit, self.dic_2Edit = dic
        elif int(self.keyNumEdit.text()) == 31:
            self.dic_1Edit, self.dic_2Edit, self.dic_3Edit = dic
        elif int(self.keyNumEdit.text()) == 32:
            self.dic_1Edit, self.dic_2Edit, self.dic_3Edit = dic

        self.toSaveUI()

    def toSaveUI(self):

        self.setWindowTitle('数据提取')
        self.resize(500, 300)

        self.textLabel = QLabel('读取详情')
        self.textEdit = QTextEdit()
        self.textLabel.setFont(QFont('幼圆', 12))
        self.textEdit.setFont(QFont('幼圆', 12))

        layout = QGridLayout()
        layout.addWidget(self.textLabel, 1, 0)
        layout.addWidget(self.textEdit, 2, 0, 1, 3)

        self.buttonReturnHead = QPushButton('返回首页')
        self.buttonReturnHead.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonReturnHead, 3, 4)

        self.buttonRead = QPushButton('开始读取')
        self.buttonRead.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonRead, 4, 4)

        self.setLayout(layout)

        self.buttonRead.clicked.connect(self.onClickButtonTextThread)
        self.buttonReturnHead.clicked.connect(self.onClickButtonReturn)

    def onClickButtonTextThread(self):

        path = self.pathEdit.text().replace('\\', '/')
        fileCoverName = self.fileCoverNameEdit.text()
        saveName = self.saveNameEdit.text()
        keyNum = self.keyNumEdit.text()

        if int(self.keyNumEdit.text()) == 1:
            dic_1 = self.dic_1Edit.text()
            self.thread = MyThread_1(path, fileCoverName, saveName, self.textEdit, dic_1)
        elif int(self.keyNumEdit.text()) == 2:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            self.thread = MyThread_2(path, fileCoverName, saveName, keyNum, self.textEdit, dic_1, dic_2)
        elif int(self.keyNumEdit.text()) == 31:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            dic_3 = self.dic_3Edit.text()
            self.thread = MyThread_31(path, fileCoverName, saveName, self.textEdit, dic_1, dic_2, dic_3)
        elif int(self.keyNumEdit.text()) == 32:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            dic_3 = self.dic_3Edit.text()
            self.thread = MyThread_32(path, fileCoverName, saveName, self.textEdit, dic_1, dic_2, dic_3)

        # self.thread.signal.connect(self.txt2csv)
        self.thread.start()


    def onClickButtonReturn(self):

        self.hide()
        self.head = HeadWindow()
        self.head.show()


# to csv window6
class HtmlToSave(QWidget):

    def __init__(self, pathEdit, fileCoverNameEdit, saveNameEdit):

        super(HtmlToSave, self).__init__()

        self.pathEdit = pathEdit
        self.fileCoverNameEdit = fileCoverNameEdit
        self.saveNameEdit = saveNameEdit

        self.setWindowTitle('数据提取')
        self.resize(500, 300)

        self.textLabel = QLabel('读取详情')
        self.textEdit = QTextEdit()
        self.textLabel.setFont(QFont('幼圆', 12))
        self.textEdit.setFont(QFont('幼圆', 12))

        layout = QGridLayout()
        layout.addWidget(self.textLabel, 1, 0)
        layout.addWidget(self.textEdit, 2, 0, 1, 3)

        self.buttonReturnHead = QPushButton('返回首页')
        self.buttonReturnHead.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonReturnHead, 3, 2)

        self.buttonStop = QPushButton('停止读取')
        self.buttonStop.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonStop, 3, 1)

        self.buttonRead = QPushButton('开始读取')
        self.buttonRead.setFont(QFont('幼圆', 10))
        layout.addWidget(self.buttonRead, 3, 0)


        self.setLayout(layout)

        self.buttonRead.clicked.connect(self.onClickButtonTextThread)
        self.buttonReturnHead.clicked.connect(self.onClickButtonReturn)
        self.buttonStop.clicked.connect(self.onClickButtonStop)

    def onClickButtonTextThread(self):

        path = self.pathEdit.text().replace('\\', '/')
        fileCoverName = self.fileCoverNameEdit.text()
        saveName = self.saveNameEdit.text()

        self.thread = MyThread_HtmlTable(path, fileCoverName, saveName, self.textEdit)

        self.thread.start()

    def onClickButtonStop(self):

        self.thread.stop()

    def onClickButtonReturn(self):

        self.hide()
        self.head = HeadWindow()
        self.head.show()


class HandleUI(QWidget):

    def __init__(self):

        super(HandleUI, self).__init__()

        self.setWindowTitle('数据清洗')
        self.resize(1100, 700)

        layout = QGridLayout()
        # self.listWidget = QListWidget()
        self.listView = QListView()
        self.listModel = QStringListModel()
        self.list = ['list1', 'list2', 'list3', 'list4']

        # 数据放入模型
        self.listModel.setStringList(self.list)
        self.listView.setModel(self.listModel)
        self.listView.setFixedSize(QSize(100, 700))

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)  # 设置行数
        self.tableWidget.setColumnCount(3)  # 设置列数
        self.tableWidget.setHorizontalHeaderLabels(['name', 'age', 'address'])  # 字段名
        nameItem = QTableWidgetItem('connor')
        self.tableWidget.setItem(0, 0, nameItem)
        ageItem = QTableWidgetItem('21')
        self.tableWidget.setItem(0, 1, ageItem)
        addressItem = QTableWidgetItem('Shenzhen')
        self.tableWidget.setItem(0, 2, addressItem)

        self.button1 = QPushButton('clean1')
        # self.button1.setFixedSize(QSize(70, 30))
        self.button2 = QPushButton('clean2')
        # self.button2.setFixedSize(QSize(70, 30))

        layout.addWidget(self.listView, 0, 0, 2, 1)
        layout.addWidget(self.tableWidget, 0, 1, 1, 2)
        layout.addWidget(self.button1, 1, 1)
        layout.addWidget(self.button2, 1, 2)
        self.setLayout(layout)




mutex = QMutex()

# 功能实现区
class MyThread_1(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, path, fileCoverName, saveName, textEdit, dic_1):

        super(MyThread_1, self).__init__()

        self.path = path
        self.fileCoverName = fileCoverName
        self.saveName = saveName
        self.textEdit = textEdit
        self.dic_1 = dic_1

    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """
        mutex.lock()

        result = []
        fail_file = ''
        for i in os.listdir(self.path):  # 获取 path 中所有的文件列表
            time.sleep(0.08)
            if f'{self.fileCoverName}' in i:
                file = f"{self.path}/{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    result += data[self.dic_1]
                    self.textEdit.append(f'{i} read successfully.')
                    self.textEdit.moveCursor(self.textEdit.textCursor().End)
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = self.path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        if fail_file != '':
            with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
                f.write(fail_file)

        self.textEdit.append('-' * 60)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()


class MyThread_2(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, path, fileCoverName, saveName, keyNum, textEdit, dic_1, dic_2):

        super(MyThread_2, self).__init__()

        self.path = path
        self.fileCoverName = fileCoverName
        self.saveName = saveName
        self.keyNum = keyNum
        self.textEdit = textEdit
        self.dic_1 = dic_1
        self.dic_2 = dic_2

    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """

        # for i in range(10):
        #     time.sleep(0.5)
        #     self.signal.emit(str("hello world" + str(i)))  # 发射信号
        mutex.lock()

        result = []
        fail_file = ''
        for i in os.listdir(self.path):  # 获取 path 中所有的文件列表
            time.sleep(0.08)
            if f'{self.fileCoverName}' in i:
                file = f"{self.path}/{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    result += data[self.dic_1][self.dic_2]

                    self.textEdit.append(f'{i} read successfully.')
                    self.textEdit.moveCursor(self.textEdit.textCursor().End)
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = self.path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        if fail_file != '':
            with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
                f.write(fail_file)
        self.textEdit.append('-' * 60)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()


class MyThread_31(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, path, fileCoverName, saveName, textEdit, dic_1, dic_2, dic_3):

        super(MyThread_31, self).__init__()

        self.path = path
        self.fileCoverName = fileCoverName
        self.saveName = saveName
        self.textEdit = textEdit
        self.dic_1 = dic_1
        self.dic_2 = dic_2
        self.dic_3 = dic_3

    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """

        # for i in range(10):
        #     time.sleep(0.5)
        #     self.signal.emit(str("hello world" + str(i)))  # 发射信号
        mutex.lock()

        result = []
        fail_file = ''
        for i in os.listdir(self.path):  # 获取 path 中所有的文件列表
            time.sleep(0.08)
            if f'{self.fileCoverName}' in i:
                file = f"{self.path}/{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    result += data[self.dic_1][self.dic_2][self.dic_3]
                    self.textEdit.append(f'{i} read successfully.')
                    self.textEdit.moveCursor(self.textEdit.textCursor().End)
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = self.path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        if fail_file != '':
            with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
                f.write(fail_file)

        self.textEdit.append('-' * 60)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()


class MyThread_32(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, path, fileCoverName, saveName, textEdit, dic_1, dic_2, dic_3):

        super(MyThread_32, self).__init__()

        self.path = path
        self.fileCoverName = fileCoverName
        self.saveName = saveName
        self.textEdit = textEdit
        self.dic_1 = dic_1
        self.dic_2 = dic_2
        self.dic_3 = dic_3

    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """
        mutex.lock()

        result = []
        fail_file = ''
        for i in os.listdir(self.path):  # 获取 path 中所有的文件列表
            time.sleep(0.08)
            if f'{self.fileCoverName}' in i:
                file = f"{self.path}/{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    if (len(data[self.dic_1][self.dic_2]) != 0) and (len(data[self.dic_1][self.dic_3]) == 0):
                        for d1 in data[self.dic_1][self.dic_2]:
                            d1['userId'] = i.split('-')[0]
                            d1List = [d1]
                            result += d1List
                        self.textEdit.append(f'{i} read successfully.')
                        self.textEdit.moveCursor(self.textEdit.textCursor().End)
                    elif (len(data[self.dic_1][self.dic_2]) == 0) and (len(data[self.dic_1][self.dic_3]) != 0):
                        for d2 in data[self.dic_1][self.dic_3]:
                            d2['userId'] = i.split('-')[0]
                            d2List = [d2]
                            result += d2List
                        self.textEdit.append(f'{i} read successfully.')
                        self.textEdit.moveCursor(self.textEdit.textCursor().End)
                    elif (len(data[self.dic_1][self.dic_2]) != 0) and (len(data[self.dic_1][self.dic_3]) != 0):
                        for d1 in data[self.dic_1][self.dic_2]:
                            d1['userId'] = i.split('-')[0]
                            d1List = [d1]
                            result += d1List
                        for d2 in data[self.dic_1][self.dic_3]:
                            d2['userId'] = i.split('-')[0]
                            d2List = [d2]
                            result += d2List
                        self.textEdit.append(f'{i} read successfully.')
                        self.textEdit.moveCursor(self.textEdit.textCursor().End)
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = self.path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        if fail_file != '':
            with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
                f.write(fail_file)

        self.textEdit.append('-' * 60)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()


class MyThread_HtmlTable(QThread):
    signal = pyqtSignal(str)  # 括号里填写信号传递的参数

    def __init__(self, path, fileCoverName, saveName, textEdit):

        super(MyThread_HtmlTable, self).__init__()

        self.path = path
        self.fileCoverName = fileCoverName
        self.saveName = saveName
        self.textEdit = textEdit


    def run(self):
        """
        进行任务操作 主要的逻辑操作 返回结果
        :return:
        """
        mutex.lock()

        self.result = []
        fail_file = ''
        for i in os.listdir(self.path):  # 获取 path 中所有的文件列表
            time.sleep(0.08)
            if f'{self.fileCoverName}' in i:
                file = f"{self.path}/{i}"
                try:
                    data = pd.read_html(file)
                    table = data[0]
                    self.result.append(table)
                    self.textEdit.append(f'{i} read successfully.')
                    self.textEdit.moveCursor(self.textEdit.textCursor().End)
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = self.path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        if fail_file != '':
            with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
                f.write(fail_file)

        self.textEdit.append('-' * 60)
        df = pd.concat(self.result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()

    def stop(self):
        try:
            self.is_running=False
            df = pd.concat(self.result)
            df.to_csv(f'{"/".join(self.path.split("/")[: -1])}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
            self.textEdit.append(f'{self.saveName}.csv save successfully.')
            self.terminate()
        except:
            self.is_running = False
            self.textEdit.append('-' * 60)
            self.textEdit.append(traceback.format_exc())
            self.terminate()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    save = HeadWindow()
    save.show()
    sys.exit(app.exec_())