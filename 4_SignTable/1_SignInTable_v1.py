# -*- coding: utf-8 -*-
# @time    : 2023/8/22 4:15
# @author  : w-xin
# @file    : 1_SignInTable_v1.py
# @software: PyCharm

"""
分离签到表
"""
import os
import pandas as pd
import openpyxl
import xlrd
import xlwt
from xlutils.copy import copy

if __name__ == '__main__':

    # 加载已知文件
    path = 'E:\\Desktop\\2022-2023-2\\公共课\\复变函数与积分变换.xls'
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
            screen2.drop(labels = ['轮次', '组号'], axis = 1, inplace = True)
            screen2['学号'] = screen2['学号'].astype(str)
            worksheet = xlsWrite.add_sheet(f'{cla}')
            workcolumns = screen2.columns
            values = screen2.apply(lambda x: tuple(x), axis=1).values.tolist()
            # 写入 columns
            for col in range(len(workcolumns)):
                worksheet.write(0, col, workcolumns[col])
            # 写入数据
            for rowlen in range(len(values)):
                row = values[rowlen]
                for collen in range(len(workcolumns)):
                    worksheet.write(rowlen + 1, collen, row[collen])
    xlsWrite.save(path)
