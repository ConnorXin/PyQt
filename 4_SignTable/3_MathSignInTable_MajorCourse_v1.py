# -*- coding: utf-8 -*-
# @time    : 2023/11/12 17:28
# @file    : 3_MathSignInTable_MajorCourse_v1.py
# @software: PyCharm

"""
"""
import os.path
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


def data_rebuilt(data):

    dept = data['院系'].values[0]
    course_name = data['课程名称'].values[0]
    teacher = data['教师'].values[0]
    rebuil = data[['学号', '姓名', '班级', '修读类别']]

    return rebuil, dept, course_name, teacher


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
    # 设置行高列宽
    worksheet.col(0).width = 6 * 256
    worksheet.col(1).width = 14 * 256
    for i in range(2, 7):
        worksheet.col(i).width = 12 * 256
    worksheet.row(0).height_mismatch = True
    worksheet.row(0).height = 60 * 9
    for i in range(1, len(values) + 4):
        worksheet.row(i).height_mismatch = True
        worksheet.row(i).height = 60 * 7

    return write_object


def major(path):

    file = [dir for dir in os.listdir(path) if '教学任务' in dir and 'result' not in dir][0]
    df = pd.read_excel(os.path.join(path, file), dtype=str)
    df.dropna(inplace=True)
    df = df[df['上课院系'] == '数学与统计学院']
    df_havespace = df[df.行政班.str.contains(' ')]
    df_nospace = df[~df.行政班.str.contains(' ')]
    df_havespace['行政班'] = df_havespace['行政班'].str.split()
    df_havespace = df_havespace.explode('行政班')

    df_concat = pd.concat([df_nospace, df_havespace], ignore_index=True)
    df_concat.drop_duplicates(inplace=True)

    return df_concat


def main(path):

    global df, no_data, no_data_rebuilt, class_major, class_statis, course, over_last
    files_list = [dir for dir in os.listdir(path) if '教学任务' not in dir and 'result' not in dir]
    class_major = major(path)
    for file in tqdm(files_list):

        df = pd.read_excel(os.path.join(path, file), dtype=str)
        if file == '概率统计.xls' or file == '概率论.xls' or file == '线性代数.xls':
            df = df[df['院系'] == '数学与统计学院']
        if file == '深度学习.xls':
            df = df[df['课程名称'] == '深度学习']
        xls_write = xlwt.Workbook()
        for no_name, no_data in df.groupby('课程序号'):
            class_statis = no_data.groupby('班级').agg({'学号': 'count'})
            class_statis['学号'] = class_statis['学号'].astype('int64')
            class_statis.sort_values(by='学号', ascending=False, inplace=True)
            if (class_statis.shape[0] == 1) or (class_statis.shape[0] == 2 and class_statis['学号'].values[1] < 20) or \
                    (class_statis.shape[0] > 2 and class_statis['学号'].values[0] > 30 and class_statis['学号'].values[1] < 20):
                # 2021110212
                no_data.sort_values(by=['修读类别', '学号'], ascending=[False, True], inplace=True)
                no_data['学号'] = no_data['学号'].astype(str)
                no_data_rebuilt, dept, course, teacher = data_rebuilt(no_data)
                idx = np.arange(1, no_data_rebuilt.shape[0] + 1)
                no_data_rebuilt.insert(loc=0, column='序号', value=idx)
                no_data_rebuilt['签到'] = None
                major_name = class_major[class_major['行政班'] == class_statis.index[0]]['专业'].values[0]
                row = f'专业:{major_name}  班级:{class_statis.index[0]}  课程名称:{course}  授课教师:{teacher}'
                xls_write = write(xls_write, no_data_rebuilt, class_statis.index[0], dept, row)
            elif class_statis['学号'].values[0] > 30 and class_statis['学号'].values[1] > 30:
                if class_statis.shape[0] == 2:
                    for class_name, class_data in no_data.groupby('班级'):
                        class_data.sort_values(by=['修读类别', '学号'], ascending=[False, True], inplace=True)
                        class_data['学号'] = class_data['学号'].astype(str)
                        class_data_rebuilt, dept, course, teacher = data_rebuilt(class_data)
                        idx = np.arange(1, class_data_rebuilt.shape[0] + 1)
                        class_data_rebuilt.insert(loc=0, column='序号', value=idx)
                        class_data_rebuilt['签到'] = None
                        major_name = class_major[class_major['行政班'] == class_name]['专业'].values[0]
                        row = f'专业:{major_name}  班级:{class_name}  课程名称:{course}  授课教师:{teacher}'
                        xls_write = write(xls_write, class_data_rebuilt, class_name, dept, row)
                else:
                    class_statis_over = no_data[no_data['班级'].isin(class_statis[class_statis['学号'] >= 30].index)]
                    class_statis_under = no_data[~no_data['班级'].isin(class_statis[class_statis['学号'] >= 30].index)]
                    over_last = class_statis_over['班级'].map(lambda x: str(x)[-1])
                    under_last = class_statis_under['班级'].map(lambda x: str(x)[-1])
                    over_under_diff = set(under_last) - set(over_last)  # 没有存在的班级
                    over_last = over_last.sort_values().values
                    max_ = over_last[-1]
                    for i, j in class_statis_over.groupby('班级'):
                        temp = [j]
                        for m, n in class_statis_under.groupby('班级'):
                            if str(i)[-1] == str(m)[-1] or (str(i)[-1] == max_ and str(m)[-1] in list(over_under_diff)):
                                temp += [n]
                        temp_concat = pd.concat(temp, ignore_index=True)
                        temp_concat.sort_values(by=['修读类别', '学号'], ascending=[False, True], inplace=True)
                        temp_concat['学号'] = temp_concat['学号'].astype(str)
                        temp_concat_rebuilt, dept, course, teacher = data_rebuilt(temp_concat)
                        idx = np.arange(1, temp_concat_rebuilt.shape[0] + 1)
                        temp_concat_rebuilt.insert(loc=0, column='序号', value=idx)
                        temp_concat_rebuilt['签到'] = None
                        major_name = class_major[class_major['行政班'] == i]['专业'].values[0]
                        row = f'专业:{major_name}  班级:{i}  课程名称:{course}  授课教师:{teacher}'
                        xls_write = write(xls_write, temp_concat_rebuilt, i, dept, row)
            else:
                no_data.sort_values(by=['修读类别', '学号'], ascending=[False, True], inplace=True)
                no_data['学号'] = no_data['学号'].astype(str)
                no_data_rebuilt, dept, course, teacher = data_rebuilt(no_data)
                idx = np.arange(1, no_data_rebuilt.shape[0] + 1)
                no_data_rebuilt.insert(loc=0, column='序号', value=idx)
                no_data_rebuilt['签到'] = None
                major_name = class_major[class_major['行政班'] == class_statis.index[0]]['专业'].values[0]
                row = f'专业:{major_name}  班级:{class_statis.index[0]}  课程名称:{course}  授课教师:{teacher}'
                xls_write = write(xls_write, no_data_rebuilt, class_statis.index[0], dept, row)
        xls_write.save(os.path.join(path, 'result', f'{course}.xls'))


if __name__ == '__main__':

    warnings.filterwarnings('ignore')
    path = r'./Math_Academy/'
    main(path)
