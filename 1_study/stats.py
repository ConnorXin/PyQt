# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.textEdit = QtWidgets.QPlainTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 201, 281))
        self.textEdit.setObjectName("textEdit")
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(310, 260, 75, 31))
        self.button.setObjectName("button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "薪资统计"))
        self.textEdit.setPlaceholderText(_translate("Form", "请输入薪资信息"))
        self.button.setText(_translate("Form", "统计"))
