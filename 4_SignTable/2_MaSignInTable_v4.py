# -*- coding: utf-8 -*-
# @time    : 2023/11/5 20:33
# @file    : 2_MaSignInTable_v4.py
# @software: PyCharm

"""
"""
import os
import socket
import sys
from sys import argv, exit
from warnings import filterwarnings

from numpy import arange
from pandas import read_excel, concat
from xlwt import XFStyle, Font, Alignment, Borders, Workbook
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton, QMessageBox, QFileDialog


class SingleInstanceApp(QWidget):
    def __init__(self):
        super().__init__()

    def check_single_instance(self):
        server_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            server_.bind(("127.0.0.1", 12345))  # 绑定特定的IP和端口
        except socket.error:
            QMessageBox.warning(self, '警告', '程序已经在运行中。')
            sys.exit(1)

        server_.listen(1)
        return server_


class SignTable(QWidget):

    def __init__(self):

        super(SignTable, self).__init__()
        self.setWindowTitle('马院签到表')
        self.resize(400, 150)

        layout = QVBoxLayout()
        label = QLabel('请选择文件', self)
        file_btn = QPushButton('选择文件', self)
        file_btn.clicked.connect(self.open_file_dialog)
        # folder_btn = QPushButton('选择文件夹', self)
        # folder_btn.clicked.connect(self.open_floder_dialog)
        btn = QPushButton('生成文件')

        layout.addWidget(label)
        layout.addWidget(file_btn)
        layout.addWidget(btn)

        self.setLayout(layout)

        btn.clicked.connect(self.generate)


    def titleStyle(self):
        style = XFStyle()

        font = Font()
        font.name = '宋体'
        font.bold = True
        # 定义字体大小  220就是11号字体，基数 20 * 号数，11号字体就是 20 * 11 = 220
        font.height = 20 * 16
        style.font = font

        alignment = Alignment()
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = Alignment.VERT_CENTER
        style.alignment = alignment

        return style

    def minTitleStyle(self):
        style = XFStyle()

        font = Font()
        font.name = 'Arial'
        font.bold = False
        font.height = 20 * 10
        style.font = font

        alignment = Alignment()
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = Alignment.VERT_CENTER
        style.alignment = alignment

        return style

    def contentStyle(self):
        style = XFStyle()

        font = Font()
        font.name = 'Arial'
        font.bold = False
        font.height = 20 * 10
        style.font = font

        alignment = Alignment()  # 设置字体在单元格的位置
        # 水平方向 居中：HORZ_CENTER  左对齐：HORZ_LEFT  右对齐：HORZ_RIGHT
        alignment.horz = Alignment.HORZ_CENTER
        # 垂直方向 居中：VERT_CENTER  顶部对齐：VERT_TOP  底部对齐：VERT_BOTTOM
        alignment.vert = Alignment.VERT_CENTER
        style.alignment = alignment

        border = Borders()  # 给单元格加框线
        border.left = Borders.THIN  # 左
        border.top = Borders.THIN  # 上
        border.right = Borders.THIN  # 右
        border.bottom = Borders.THIN  # 下
        style.borders = border

        return style

    def write(self, write_object, df, sheet_name, dept, row):

        worksheet = write_object.add_sheet(sheet_name)
        work_columns = df.columns
        values = df.apply(lambda x: tuple(x), axis=1).values.tolist()
        # 写入标题以及详细信息
        worksheet.write(0, 0, dept, self.titleStyle())
        worksheet.write(1, 0, row, self.minTitleStyle())
        # 写入 columns
        content_style = self.contentStyle()
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


    def open_file_dialog(self):

        self.path, _ = QFileDialog.getOpenFileName(self, '打开文件', './', 'Excel File (*.xlsx *.xls)')


    def generate(self):


        path = self.path
        # print(path)
        # file_stu = [dir for dir in os.listdir(path) if '上课名单' in dir][0]
        df_stu = read_excel(path, dtype=str)

        df_stu_filter = df_stu.loc[df_stu['课程名称'].isin(['思想道德与法治', '中国近现代史纲要', '习近平新时代中国特色社会主义思想概论', '马克思主义基本原理'])]
        df_stu_filter = df_stu_filter[['课程名称', '学号', '姓名', '班级', '院系', '修读类别', '教师']]

        try:
            for course_name, course_data in df_stu_filter.groupby('课程名称'):
                xls_write = Workbook()
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
                            rebuil_merge = concat([retrieve, class_data], ignore_index=True)
                            rebuil_merge['学号'] = rebuil_merge['学号'].astype('int64')
                            rebuil_merge.sort_values(by=['学号', '修读类别'], inplace=True)
                            rebuil_merge['学号'] = rebuil_merge['学号'].astype(str)
                            rebuil_merge.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                            idx = arange(1, rebuil_merge.shape[0] + 1)
                            rebuil_merge.insert(loc=0, column='序号', value=idx)
                            row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                            rebuil_merge['签到'] = None
                            xls_write = self.write(xls_write, rebuil_merge, class_name, dept, row)
                        else:
                            class_data['学号'] = class_data['学号'].astype('int64')
                            class_data.sort_values(by=['学号', '修读类别'], inplace=True)
                            class_data['学号'] = class_data['学号'].astype(str)
                            class_data.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                            idx = arange(1, class_data.shape[0] + 1)
                            class_data.insert(loc=0, column='序号', value=idx)
                            row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                            class_data['签到'] = None
                            xls_write = self.write(xls_write, class_data, class_name, dept, row)
                    else:
                        class_data['学号'] = class_data['学号'].astype('int64')
                        class_data.sort_values(by=['学号', '修读类别'], inplace=True)
                        class_data['学号'] = class_data['学号'].astype(str)
                        class_data.drop(labels=['课程名称', '院系', '教师'], axis=1, inplace=True)
                        idx = arange(1, class_data.shape[0] + 1)
                        class_data.insert(loc=0, column='序号', value=idx)
                        row = f'班级:{class_name}  课程名称:{course_name}  授课教师:{teacher}'
                        class_data['签到'] = None
                        xls_write = self.write(xls_write, class_data, class_name, dept, row)
                current_dir = os.path.dirname(path)
                if os.path.exists(os.path.join(current_dir, 'result')):
                    pass
                else:
                    os.mkdir(os.path.join(current_dir, 'result'))
                xls_write.save(os.path.join(current_dir, 'result', f'{course_name}.xls'))
            reply = QMessageBox.information(self, '提示', '完成')
        except Exception as e:
            reply = QMessageBox.critical(self, 'Error', f'{e}\n请检查文件是否符合')


if __name__ == '__main__':

    filterwarnings('ignore')

    app = QApplication(argv)
    single_instance_app = SingleInstanceApp()
    server = single_instance_app.check_single_instance()  # 检查单例实例
    main = SignTable()
    main.show()
    exit(app.exec_())