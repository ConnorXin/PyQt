# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/7/28 16:11
# @File    :  ToCsv.py
# @IDE     :  PyCharm


import os
import sys
import time
import json

import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Data2Csv(QWidget):

    def __init__(self):

        super(Data2Csv, self).__init__()

        self.initUI()


    def initUI(self):


        self.setWindowTitle('保存CSV')
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
        layout.addWidget(self.buttonNext, 5, 4)
        self.setLayout(layout)

        self.buttonNext.clicked.connect(self.nextonClick)


    def nextonClick(self):

        self.hide()
        self.next = NextClick(self.pathEdit, self.fileCoverNameEdit,
                              self.saveNameEdit, self.keyNumEdit)
        self.next.show()


class NextClick(QWidget):

    def __init__(self, pathEdit, fileCoverNameEdit, saveNameEdit, keyNumEdit):
        
        super(NextClick, self).__init__()
        self.pathEdit = pathEdit
        self.fileCoverNameEdit = fileCoverNameEdit
        self.saveNameEdit = saveNameEdit
        self.keyNumEdit = keyNumEdit
        self.initNextUI()


    def initNextUI(self):


        keyNum = self.keyNumEdit.text()
        if int(keyNum) == 1:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            layout.addWidget(self.buttonNext, 5, 4)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
        elif int(keyNum) == 2:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            layout.addWidget(self.buttonNext, 5, 4)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
        elif int(keyNum) == 31:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()
            self.dic_3Label = QLabel('字典3')
            self.dic_3Edit = QLineEdit()

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)
            layout.addWidget(self.dic_3Label, 3, 0)
            layout.addWidget(self.dic_3Edit, 3, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            layout.addWidget(self.buttonNext, 5, 4)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)
        elif int(keyNum) == 32:
            self.setWindowTitle('保存CSV')
            self.resize(500, 300)

            self.dic_1Label = QLabel('字典1')
            self.dic_1Edit = QLineEdit()
            self.dic_2Label = QLabel('字典2')
            self.dic_2Edit = QLineEdit()
            self.dic_3Label = QLabel('字典3')
            self.dic_3Edit = QLineEdit()

            layout = QGridLayout()
            layout.addWidget(self.dic_1Label, 1, 0)
            layout.addWidget(self.dic_1Edit, 1, 1, 1, 4)
            layout.addWidget(self.dic_2Label, 2, 0)
            layout.addWidget(self.dic_2Edit, 2, 1, 1, 4)
            layout.addWidget(self.dic_3Label, 3, 0)
            layout.addWidget(self.dic_3Edit, 3, 1, 1, 4)

            self.buttonNext = QPushButton('下一步')
            layout.addWidget(self.buttonNext, 5, 4)

            self.setLayout(layout)

            self.buttonNext.clicked.connect(self.nextonClick)


    def nextonClick(self):

        self.hide()
        if int(self.keyNumEdit.text()) == 1:
            self.save = ToSave(self.pathEdit, self.fileCoverNameEdit,
                               self.saveNameEdit, self.keyNumEdit, self.dic_1Edit)
        elif int(self.keyNumEdit.text()) == 2:
            self.save = ToSave(self.pathEdit, self.fileCoverNameEdit,
                               self.saveNameEdit, self.keyNumEdit,
                               (self.dic_1Edit, self.dic_2Edit))

        elif int(self.keyNumEdit.text()) == 31:
            self.save = ToSave(self.pathEdit, self.fileCoverNameEdit,
                               self.saveNameEdit, self.keyNumEdit, (self.dic_1Edit,
                               self.dic_2Edit, self.dic_3Edit))
        elif int(self.keyNumEdit.text()) == 32:
            self.save = ToSave(self.pathEdit, self.fileCoverNameEdit,
                               self.saveNameEdit, self.keyNumEdit, (self.dic_1Edit,
                               self.dic_2Edit, self.dic_3Edit))
        self.save.show()



mutex = QMutex()

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

        with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
            f.write(fail_file)
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

        with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
            f.write(fail_file)
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

        with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
            f.write(fail_file)
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

        with open(f'{savePath}/{self.saveName}_failFile.txt', 'w', encoding='utf-8') as f:
            f.write(fail_file)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{self.saveName}.csv', encoding='utf-8-sig', index=False)
        self.textEdit.append(f'{self.saveName}.csv save successfully.')

        mutex.unlock()





class ToSave(QWidget):

    def __init__(self, pathEdit, fileCoverNameEdit, saveNameEdit, keyNumEdit, dic):

        super(ToSave, self).__init__()

        self.pathEdit = pathEdit
        self.fileCoverNameEdit = fileCoverNameEdit
        self.saveNameEdit = saveNameEdit
        self.keyNumEdit = keyNumEdit


        if int(self.keyNumEdit.text())  == 1:
            self.dic_1Edit = dic
        elif int(self.keyNumEdit.text())  == 2:
            self.dic_1Edit, self.dic_2Edit = dic
        elif int(self.keyNumEdit.text())  == 31:
            self.dic_1Edit, self.dic_2Edit, self.dic_3Edit = dic
        elif int(self.keyNumEdit.text())  == 32:
            self.dic_1Edit, self.dic_2Edit, self.dic_3Edit = dic


        self.toSaveUI()


    def toSaveUI(self):

        self.setWindowTitle('保存CSV')
        self.resize(500, 300)

        self.textLabel = QLabel('读取详情')
        self.textEdit = QTextEdit()

        layout = QGridLayout()
        layout.addWidget(self.textLabel, 1, 0)
        layout.addWidget(self.textEdit, 2, 0, 1, 4)

        self.buttonRead = QPushButton('读取')
        layout.addWidget(self.buttonRead, 5, 4)
        self.setLayout(layout)

        self.buttonRead.clicked.connect(self.onClickButtonTextThread)


    def onClickButtonTextThread(self):

        path = self.pathEdit.text().replace('\\', '/')
        fileCoverName = self.fileCoverNameEdit.text()
        saveName = self.saveNameEdit.text()
        keyNum = self.keyNumEdit.text()

        if int(self.keyNumEdit.text())  == 1:
            dic_1 = self.dic_1Edit.text()
            self.thread = MyThread_1(path, fileCoverName, saveName, self.textEdit, dic_1)
        elif int(self.keyNumEdit.text())  == 2:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            self.thread = MyThread_2(path, fileCoverName, saveName, keyNum, self.textEdit, dic_1, dic_2)
        elif int(self.keyNumEdit.text())  == 31:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            dic_3 = self.dic_3Edit.text()
            self.thread = MyThread_31(path, fileCoverName, saveName, self.textEdit, dic_1, dic_2, dic_3)
        elif int(self.keyNumEdit.text())  == 32:
            dic_1 = self.dic_1Edit.text()
            dic_2 = self.dic_2Edit.text()
            dic_3 = self.dic_3Edit.text()
            self.thread = MyThread_32(path, fileCoverName, saveName, self.textEdit, dic_1, dic_2, dic_3)


        # self.thread.signal.connect(self.txt2csv)
        self.thread.start()



    def txt2csv(self):



        path = self.pathEdit.text().replace('\\', '/')
        fileCoverName = self.fileCoverNameEdit.text()
        saveName = self.saveNameEdit.text()
        keyNum = self.keyNumEdit.text()


        result = []
        fail_file = ''
        for i in os.listdir(path):  # 获取 path 中所有的文件列表
            if f'{fileCoverName}' in i:
                file = f"{path}/{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    if int(keyNum) == 1:
                        result += data[self.dic_1Edit.text()]
                        print(f'{i} read successfully.')
                    elif int(keyNum) == 2:
                        result += data[self.dic_1Edit.text()][self.dic_2Edit.text()]

                        # dicValue['entryId'] = i.split('.')[0]
                        # result += [dicValue]
                        self.textEdit.append(f'{i} read successfully.')
                        self.textEdit.moveCursor(self.textEdit.textCursor().End)
                        # print(f'{i} read successfully.')
                        # if i == '438107198.txt':
                        #     df = pd.DataFrame(result)
                        #     break
                    elif int(keyNum) == 31:
                        result += data[self.dic_1Edit.text()][self.dic_2Edit.text()][self.dic_3Edit.text()]
                    elif int(keyNum) == 32:
                        if (len(data[dic['dic_1']][dic['dic_2']]) != 0) and (len(data[dic['dic_1']][dic['dic_3']]) == 0):
                            for d1 in data[dic['dic_1']][dic['dic_2']]:
                                d1['userId'] = i.split('-')[0]
                                d1List = [d1]
                                result += d1List
                            print(f'{i} read successfully.')
                        elif (len(data[dic['dic_1']][dic['dic_2']]) == 0) and (len(data[dic['dic_1']][dic['dic_3']]) != 0):
                            for d2 in data[dic['dic_1']][dic['dic_3']]:
                                d2['userId'] = i.split('-')[0]
                                d2List = [d2]
                                result += d2List
                            print(f'{i} read successfully.')
                        elif (len(data[dic['dic_1']][dic['dic_2']]) != 0) and (len(data[dic['dic_1']][dic['dic_3']]) != 0):
                            for d1 in data[dic['dic_1']][dic['dic_2']]:
                                d1['userId'] = i.split('-')[0]
                                d1List = [d1]
                                result += d1List
                            for d2 in data[dic['dic_1']][dic['dic_3']]:
                                d2['userId'] = i.split('-')[0]
                                d2List = [d2]
                                result += d2List
                            print(f'{i} read successfully.')
                except:
                    fail_file += i + '\n'
        self.textEdit.append('All file read completely.')
        savePathList = path.split('/')[: -1]
        savePath = '/'.join(savePathList)

        with open(f'{savePath}/{saveName}_failFile.txt', 'w', encoding = 'utf-8') as f:
            f.write(fail_file)
        df = pd.DataFrame(result)
        df.to_csv(f'{savePath}/{saveName}.csv', encoding = 'utf-8-sig', index = False)
        self.textEdit.append(f'{saveName}.csv save successfully.')





if __name__ == '__main__':

    app = QApplication(sys.argv)

    save = Data2Csv()
    save.show()

    sys.exit(app.exec_())
