# -*- coding: utf-8 -*-
# @time    : 2023/8/22 4:15
# @author  : w-xin
# @file    : 1_SignInTable_v2.py
# @software: PyCharm

"""
分离签到表
"""
import os
import pandas as pd
import xlrd
import numpy as np
import xlwt
from xlutils.copy import copy


def titleStyle():

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


def minTitleStyle():

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


def contentStyle():

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


if __name__ == '__main__':

    curpath = os.path.abspath(os.curdir)
    oriPath = curpath + '\\' + 'system'
    if os.path.exists(curpath + '\\' + 'splited'):
        pass
    else:
        os.mkdir(curpath + '\\' + 'splited')
    for file in os.listdir(oriPath):
        if '.xls' in file:
            path = f'{oriPath}\\{file}'
            dfOriginal = pd.read_excel(path)
            xlsdata = xlrd.open_workbook(path, formatting_info = True)
            xlsWrite = copy(wb = xlsdata)  # 完成 xlrd 对象向 xlwt 对象转换
            courseSerial = dfOriginal['课程序号'].unique()
            for course in courseSerial:
                screen1 = dfOriginal[dfOriginal['课程序号'] == course]
                classes = screen1['班级'].unique()
                for cla in classes:
                    screen2 = screen1[screen1['班级'] == cla]
                    screen2 = screen2.sort_values(by = '学号')
                    screen2['学号'] = screen2['学号'].astype(str)
                    screen2['班级'] = screen2['班级'].astype(str)
                    courseName = file.split('.')[0]
                    academic = screen2['开课院系'].values[0]
                    teachers = screen2['教师'].values[0]
                    screen2.drop(labels = ['课程序号', '课程代码', '课程名称', '学分', '课程类别', '院系', '开课院系', '教师',
                                           '轮次', '组号'], axis = 1, inplace = True)
                    idx = np.arange(1, len(screen2) + 1)
                    screen2.insert(loc = 0, column = '序号', value = idx)
                    row2 = f'专业:  班级:{cla}  课程名称:{courseName}  授课教师:{teachers}'
                    sign = ['' for i in range(len(screen2))]
                    screen2.insert(loc = 5, column = '签到', value = sign)
                    try:
                        worksheet = xlsWrite.add_sheet(f'{cla}')
                        workcolumns = screen2.columns
                        values = screen2.apply(lambda x: tuple(x), axis=1).values.tolist()
                        # 写入标题以及详细信息
                        worksheet.write(0, 0, academic, titleStyle())
                        worksheet.write(1, 0, row2, minTitleStyle())
                        # 写入 columns
                        for col in range(len(workcolumns)):
                            worksheet.write(2, col, workcolumns[col], contentStyle())
                        # 写入数据
                        for rowlen in range(len(values)):
                            row = values[rowlen]
                            for collen in range(len(workcolumns)):
                                worksheet.write(rowlen + 3, collen, row[collen], contentStyle())
                    except:
                        worksheet = xlsWrite.add_sheet(f'{cla}_')
                        workcolumns = screen2.columns
                        values = screen2.apply(lambda x: tuple(x), axis=1).values.tolist()
                        # 写入 columns
                        for col in range(len(workcolumns)):
                            worksheet.write(2, col, workcolumns[col], contentStyle())
                        # 写入数据
                        for rowlen in range(len(values)):
                            row = values[rowlen]
                            for collen in range(len(workcolumns)):
                                worksheet.write(rowlen + 3, collen, row[collen], contentStyle())
            xlsWrite.save(curpath + '\\' + 'splited' + '\\' + file)
