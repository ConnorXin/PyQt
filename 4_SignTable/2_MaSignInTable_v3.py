# -*- coding: utf-8 -*-
# @time    : 2023/11/5 20:15
# @file    : 2_MaSignInTable_v3.py
# @software: PyCharm

"""
"""
import os
import warnings

import numpy as np
import pandas as pd
import xlwt
from tqdm import tqdm


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


def write(write_object, df, sheet_name, dept, row):

    worksheet = write_object.add_sheet(sheet_name)
    work_columns = df.columns
    values = df.apply(lambda x: tuple(x), axis=1).values.tolist()
    # 写入标题以及详细信息
    worksheet.write(0, 0, dept, titleStyle())
    worksheet.write(1, 0, row, minTitleStyle())
    # 写入 columns
    content_style = contentStyle()
    for col in range(len(work_columns)):
        worksheet.write(2, col, work_columns[col], content_style)
    # 写入数据
    for rowlen in range(len(values)):
        row = values[rowlen]
        for collen in range(len(work_columns)):
            worksheet.write(rowlen + 3, collen, row[collen], content_style)

    return write_object


def main(path):

    file_stu = [dir for dir in os.listdir(path) if '上课名单' in dir][0]
    df_stu = pd.read_excel(file_stu, dtype=str)

    df_stu_filter = df_stu.loc[df_stu['课程名称'].isin(['思想道德与法治', '中国近现代史纲要', '习近平新时代中国特色社会主义思想概论', '马克思主义基本原理'])]
    df_stu_filter = df_stu_filter[['课程名称', '学号', '姓名', '班级', '院系', '修读类别', '教师']]

    for course_name, course_data in df_stu_filter.groupby('课程名称'):
        xls_write = xlwt.Workbook()
        str_type = ''.join(course_data['修读类别'])
        flag = 0
        if '重修' in str_type or '补修' in str_type:
            rebuil = course_data.loc[course_data['修读类别'].isin(['重修', '重修免听', '补修'])]
            course_data = course_data[course_data['修读类别'] == '正常']
            flag = 1
        for class_name, class_data in course_data.groupby('班级'):
            dept = class_data['院系'].values[0]
            teacher = class_data['教师'].values[0]
            if flag == 1:
                retrieve = rebuil.loc[rebuil.院系.str.contains(dept)]
                if retrieve.shape[0] != 0:
                    rebuil = rebuil[rebuil['院系'] != dept]
                    rebuil_merge = pd.concat([retrieve, class_data], ignore_index=True)
                    rebuil_merge['学号'] = rebuil_merge['学号'].astype('int64')
                    rebuil_merge.sort_values(by=['学号', '修读类别'], inplace=True)
                    rebuil_merge['学号'] = rebuil_merge['学号'].astype(str)
                    rebuil_merge.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                    idx = np.arange(1, rebuil_merge.shape[0] + 1)
                    rebuil_merge.insert(loc=0, column='序号', value=idx)
                    row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                    rebuil_merge['签到'] = None
                    xls_write = write(xls_write, rebuil_merge, class_name, dept, row)
                else:
                    class_data['学号'] = class_data['学号'].astype('int64')
                    class_data.sort_values(by=['学号', '修读类别'], inplace=True)
                    class_data['学号'] = class_data['学号'].astype(str)
                    class_data.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                    idx = np.arange(1, class_data.shape[0] + 1)
                    class_data.insert(loc=0, column='序号', value=idx)
                    row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                    class_data['签到'] = None
                    xls_write = write(xls_write, class_data, class_name, dept, row)
            else:
                class_data['学号'] = class_data['学号'].astype('int64')
                class_data.sort_values(by=['学号', '修读类别'], inplace=True)
                class_data['学号'] = class_data['学号'].astype(str)
                class_data.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                idx = np.arange(1, class_data.shape[0] + 1)
                class_data.insert(loc=0, column='序号', value=idx)
                row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                class_data['签到'] = None
                xls_write = write(xls_write, class_data, class_name, dept, row)
        if os.path.exists(os.path.join(path, 'split')):
            pass
        else:
            os.mkdir(os.path.join(path, 'split'))
        xls_write.save(os.path.join(path, 'split', f'{course_name}.xls'))



if __name__ == '__main__':

    warnings.filterwarnings('ignore')

    path = r'./'
    main(path)
