# -*- coding: utf-8 -*-
# @time    : 2023/11/5 19:24
# @file    : 2_MaSignInTable_v2.py
# @software: PyCharm

"""
"""
import os
import sys
import warnings

import numpy as np
import pandas as pd
import xlwt
from PyQt5.QtWidgets import *


class SignTable(QWidget):

    def __init__(self):

        super(SignTable, self).__init__()
        self.setWindowTitle('马院签到表')
        self.resize(400, 150)

        layout = QVBoxLayout()
        label = QLabel('系统名单文件所在路径')
        self.line = QLineEdit()
        btn = QPushButton('生成')

        layout.addWidget(label)
        layout.addWidget(self.line)
        layout.addWidget(btn)

        self.setLayout(layout)

        btn.clicked.connect(self.generate)


    def titleStyle(self):
        style = xlwt.XFStyle()

        font = xlwt.Font()
        font.name = '宋体'
        font.bold = True
        # 定义字体大小  220就是11号字体，基数 20 * 号数，11号字体就是 20 * 11 = 220
        font.height = 20 * 16
        style.font = font

        alignment = xlwt.Alignment()
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment

        return style

    def minTitleStyle(self):
        style = xlwt.XFStyle()

        font = xlwt.Font()
        font.name = 'Arial'
        font.bold = False
        font.height = 20 * 10
        style.font = font

        alignment = xlwt.Alignment()
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment

        return style

    def contentStyle(self):
        style = xlwt.XFStyle()

        font = xlwt.Font()
        font.name = 'Arial'
        font.bold = False
        font.height = 20 * 10
        style.font = font

        alignment = xlwt.Alignment()  # 设置字体在单元格的位置
        # 水平方向 居中：HORZ_CENTER  左对齐：HORZ_LEFT  右对齐：HORZ_RIGHT
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = xlwt.Alignment.VERT_CENTER
        style.alignment = alignment

        border = xlwt.Borders()  # 给单元格加框线
        border.left = xlwt.Borders.THIN  # 左
        border.top = xlwt.Borders.THIN  # 上
        border.right = xlwt.Borders.THIN  # 右
        border.bottom = xlwt.Borders.THIN  # 下
        style.borders = border

        return style

    def generate(self):

        path = rf'{self.line.text()}'
        file_stu = [dir for dir in os.listdir(path) if '上课名单' in dir][0]
        file_cla = [dir for dir in os.listdir(path) if '教学任务列表' in dir][0]
        df_stu = pd.read_excel(file_stu, dtype=str)
        df_cla = pd.read_excel(file_cla, dtype=str)

        df_stu_filter = df_stu.loc[df_stu['课程名称'].isin(['思想道德与法治', '中国近现代史纲要', '习近平新时代中国特色社会主义思想概论', '马克思主义基本原理'])]
        df_cla_filter = df_cla.loc[df_cla['课程名称'].isin(['思想道德与法治', '中国近现代史纲要', '习近平新时代中国特色社会主义思想概论', '马克思主义基本原理'])]
        df_stu_filter = df_stu_filter[['课程名称', '学号', '姓名', '班级', '院系', '修读类别', '教师']]
        df_cla_filter = df_cla_filter[['课程名称', '教学班名称']]
        df_cla_filter['教学班名称'] = df_cla_filter['教学班名称'].map(lambda x: str(x).replace('班级:', '').replace(';', ' '))

        for name, data in df_cla_filter.groupby('课程名称'):
            xlsWrite = xlwt.Workbook()
            df_stu_filter_single = df_stu_filter[df_stu_filter['课程名称'] == name]
            for cla in data['教学班名称'].values:
                if ' ' in cla:
                    clas = cla.split(' ')
                    df_stu_filter_single_cla = df_stu_filter_single.loc[df_stu_filter_single['班级'].isin(clas)]
                    df_stu_filter_single_cla['学号'] = df_stu_filter_single_cla['学号'].astype('int64')
                    dept = df_stu_filter_single_cla['院系'].values[0]
                    teacher = df_stu_filter_single_cla['教师'].values[0]
                    df_stu_filter_single_cla.sort_values(by=['学号', '修读类别'], inplace=True)
                    df_stu_filter_single_cla['学号'] = df_stu_filter_single_cla['学号'].astype(str)
                    df_stu_filter_single_cla.drop(labels=['院系', '教师'], axis=1, inplace=True)
                    idx = np.arange(1, df_stu_filter_single_cla.shape[0] + 1)
                    df_stu_filter_single_cla.insert(loc=0, column='序号', value=idx)
                    row2 = f'班级:{cla}  课程名称:{name}  授课教师:{teacher}'
                    df_stu_filter_single_cla['备注'] = None
                    str_cla = clas[0] + '等'
                    worksheet = xlsWrite.add_sheet(str_cla)
                    workcolumns = df_stu_filter_single_cla.columns
                    values = df_stu_filter_single_cla.apply(lambda x: tuple(x), axis=1).values.tolist()
                    # 写入标题以及详细信息
                    worksheet.write(0, 0, dept, self.titleStyle())
                    worksheet.write(1, 0, row2, self.minTitleStyle())
                    # 写入 columns
                    content_style = self.contentStyle()
                    for col in range(len(workcolumns)):
                        worksheet.write(2, col, workcolumns[col], content_style)
                    # 写入数据
                    for rowlen in range(len(values)):
                        row = values[rowlen]
                        for collen in range(len(workcolumns)):
                            worksheet.write(rowlen + 3, collen, row[collen], content_style)
                else:
                    df_stu_filter_single_cla = df_stu_filter_single[df_stu_filter_single['班级'] == cla]
                    df_stu_filter_single_cla['学号'] = df_stu_filter_single_cla['学号'].astype('int64')
                    dept = df_stu_filter_single_cla['院系'].values[0]
                    teacher = df_stu_filter_single_cla['教师'].values[0]
                    df_stu_filter_single_cla.sort_values(by=['学号', '修读类别'], inplace=True)
                    df_stu_filter_single_cla['学号'] = df_stu_filter_single_cla['学号'].astype(str)
                    df_stu_filter_single_cla.drop(labels=['院系', '教师'], axis=1, inplace=True)
                    idx = np.arange(1, df_stu_filter_single_cla.shape[0] + 1)
                    df_stu_filter_single_cla.insert(loc=0, column='序号', value=idx)
                    row2 = f'班级:{cla}  课程名称:{name}  授课教师:{teacher}'
                    df_stu_filter_single_cla['备注'] = None
                    worksheet = xlsWrite.add_sheet(f'{cla}')
                    workcolumns = df_stu_filter_single_cla.columns
                    values = df_stu_filter_single_cla.apply(lambda x: tuple(x), axis=1).values.tolist()
                    # 写入标题以及详细信息
                    worksheet.write(0, 0, dept, self.titleStyle())
                    worksheet.write(1, 0, row2, self.minTitleStyle())
                    # 写入 columns
                    content_style = self.contentStyle()
                    for col in range(len(workcolumns)):
                        worksheet.write(2, col, workcolumns[col], content_style)
                    # 写入数据
                    for rowlen in range(len(values)):
                        row = values[rowlen]
                        for collen in range(len(workcolumns)):
                            worksheet.write(rowlen + 3, collen, row[collen], content_style)
            xlsWrite.save(os.path.join(path, 'splited', f'{name}.xls'))
        reply = QMessageBox.information(self, '提示', '完成')


if __name__ == '__main__':

    warnings.filterwarnings('ignore')

    app = QApplication(sys.argv)
    main = SignTable()
    main.show()
    sys.exit(app.exec_())