# -*- coding: utf-8 -*-
# @Time    :  2023/12/12 14:26
# @File    :  ExtractData-ui_3.0.py
# @IDE     :  PyCharm

"""
modify
1 增加数据提取类型
2 删除清洗模块
3 界面更新
"""
import gc
import os
import sys
import time
import warnings

from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QSplitter, QListWidget, QTabWidget, QLabel, \
    QVBoxLayout, QFileDialog, QPushButton, QLineEdit, QProgressBar, QMessageBox, QCheckBox
from ExtractDataFunction import *


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.setWindowTitle('Data Extraction')
        self.resize(700, 400)

        self.font_name = 'Footlight MT Light'
        self.partly_size = 18
        self.state_font_name = 'Consolas'
        self.state_font_size = 12
        self.state_font = QFont(self.state_font_name, self.state_font_size)
        self.state_font.setBold(True)

        main_layout = QHBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(main_layout)

        splitter = QSplitter()
        main_layout.addWidget(splitter)

        self.left_widget = QListWidget()
        self.left_widget.addItem('JSON<list>')
        self.left_widget.addItem('JSON<dict>')
        self.left_widget.addItem('HTML<pandas>')
        self.left_widget.setFont(QFont(self.font_name, 12))
        self.left_widget.currentRowChanged.connect(self.update_tab_widget)
        self.right_widget = QTabWidget()

        splitter.addWidget(self.left_widget)
        splitter.addWidget(self.right_widget)

        self.update_tab_widget(0)
        # 设置初始宽度比例
        splitter.setSizes([100, 300])

        self.left_widget.setStyleSheet("QListWidget::item:selected { background-color: lightblue; color: black; }")
        self.right_widget.setStyleSheet("""
                    QTabBar::tab {
                        font-family: Consolas;
                        font-size: 14px;
                        font-weight: bold;
                        color: black;
                    }
        """)

    def update_tab_widget(self, index):

        if self.left_widget.currentItem() is None:
            return
        self.right_widget.clear()
        current_item_text = self.left_widget.currentItem().text()
        if current_item_text == 'JSON<list>':
            self.json_list_1param_ui()
            self.json_list_2param_ui()
            self.json_list_2_3param_ui()
            self.json_list_3param_ui()
        elif current_item_text == 'JSON<dict>':
            tab_json_2param = QWidget()
            # label2 = QLabel("Tab 2 Content")
            tab_json_2param.layout = QVBoxLayout()
            json_2param_open_folder_button = QPushButton('Open Folder', self)
            json_2param_open_folder_button.clicked.connect(self.open_folder_dialog)
            tab_json_2param.layout.addWidget(json_2param_open_folder_button)
            # tab2.layout.addWidget(label2)
            tab_json_2param.setLayout(tab_json_2param.layout)
            self.right_widget.addTab(tab_json_2param, "2 params dict")
        elif current_item_text == 'HTML<pandas>':
            self.html_pandas_regular_ui()
            self.html_pandas_168detail_ui()


    def open_folder_dialog(self):

        self.folder_path = QFileDialog.getExistingDirectory(self, 'Select Directory', '/')
        if self.folder_path:
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected')
            self.statusBar().setFont(self.state_font)

    '''ui'''
    def json_list_1param_ui(self):
        tab_1param = QWidget()
        # overall layout
        tab_1param.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        json_1param_open_folder_button = QPushButton('Open Folder', self)
        json_1param_open_folder_button.clicked.connect(self.open_folder_dialog)
        json_1param_open_folder_button.setFont(QFont(self.font_name, 12))
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(json_1param_open_folder_button, stretch=3)
        tab_1param.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_json_1param = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_json_1param.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_json_1param, stretch=3)
        tab_1param.layout.addLayout(layout_save_filename)
        # judge
        layout_judge_filename = QHBoxLayout()
        label_judge = QLabel('Judge')
        self.edit_judge_filename_json_1param = QLineEdit()
        label_judge.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_json_1param.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_json_1param, stretch=3)
        tab_1param.layout.addLayout(layout_judge_filename)
        # param value 1
        layout_param_value = QHBoxLayout()
        label_param_value = QLabel('Key 1')
        self.edit_param_value_json_1param_1 = QLineEdit()
        label_param_value.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_1param_1.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value.addWidget(label_param_value, stretch=1)
        layout_param_value.addWidget(self.edit_param_value_json_1param_1, stretch=3)
        tab_1param.layout.addLayout(layout_param_value)
        # show process
        self.progress_bar_json_list_1 = QProgressBar()
        self.progress_bar_json_list_1.setMinimum(0)
        self.progress_bar_json_list_1.setMaximum(100)
        tab_1param.layout.addWidget(self.progress_bar_json_list_1)
        # start button
        layout_start = QHBoxLayout()
        self.extract_button_json_list_1 = QPushButton('Extract', self)
        self.extract_button_json_list_1.clicked.connect(self.function_json_list_1)
        self.extract_button_json_list_1.setFont(QFont(self.font_name, 14))
        # self.progress_label = QLabel(self)
        # layout_start.addWidget(self.progress_label)
        self.cancel_button_json_list_1 = QPushButton('Cancel', self)
        self.cancel_button_json_list_1.setFont(QFont(self.font_name, 14))
        # self.cancel_button_json_list_1.clicked.connect(self.function_json_list_1_cancel)
        layout_start.addStretch()
        layout_start.addWidget(self.cancel_button_json_list_1)
        layout_start.addWidget(self.extract_button_json_list_1)
        self.extract_button_json_list_1.setShortcut('Return')
        tab_1param.layout.addLayout(layout_start)

        # set layout
        tab_1param.setLayout(tab_1param.layout)
        self.right_widget.addTab(tab_1param, 'one keys')

    def json_list_2param_ui(self):
        tab_2param = QWidget()
        # overall layout
        tab_2param.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        json_2param_open_folder_button = QPushButton('Open Folder', self)
        json_2param_open_folder_button.setFont(QFont(self.font_name, 12))
        json_2param_open_folder_button.clicked.connect(self.open_folder_dialog)
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(json_2param_open_folder_button, stretch=3)
        tab_2param.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_json_2param = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_json_2param.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_json_2param, stretch=3)
        tab_2param.layout.addLayout(layout_save_filename)
        # judge
        layout_judge_filename = QHBoxLayout()
        label_judge = QLabel('Judge')
        self.edit_judge_filename_json_2param = QLineEdit()
        label_judge.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_json_2param.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_json_2param, stretch=3)
        tab_2param.layout.addLayout(layout_judge_filename)
        # param value 1, 2
        layout_param_value_1 = QHBoxLayout()
        label_param_value_1 = QLabel('Key 1')
        self.edit_param_value_json_2param_1 = QLineEdit()
        self.edit_param_value_json_2param_1.setFont(QFont(self.font_name, self.partly_size))
        label_param_value_1.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_1.addWidget(label_param_value_1, stretch=1)
        layout_param_value_1.addWidget(self.edit_param_value_json_2param_1, stretch=3)
        tab_2param.layout.addLayout(layout_param_value_1)
        layout_param_value_2 = QHBoxLayout()
        label_param_value_2 = QLabel('Key 2')
        self.edit_param_value_json_2param_2 = QLineEdit()
        label_param_value_2.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_2param_2.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_2.addWidget(label_param_value_2, stretch=1)
        layout_param_value_2.addWidget(self.edit_param_value_json_2param_2, stretch=3)
        tab_2param.layout.addLayout(layout_param_value_2)
        # show process
        self.progress_bar_json_list_2 = QProgressBar()
        self.progress_bar_json_list_2.setMinimum(0)
        self.progress_bar_json_list_2.setMaximum(100)
        tab_2param.layout.addWidget(self.progress_bar_json_list_2)
        # start and cancel button
        layout_start = QHBoxLayout()
        self.extract_button_json_list_2 = QPushButton('Extract', self)
        self.extract_button_json_list_2.clicked.connect(self.function_json_list_2)
        self.extract_button_json_list_2.setFont(QFont(self.font_name, 14))
        # self.progress_label_2 = QLabel(self)
        # layout_start.addWidget(self.progress_label_2)
        self.checkFilenameIsUidBox_json_list_2 = QCheckBox('Filename is uid.')
        self.checkFilenameIsUidBox_json_list_2.setFont(QFont(self.state_font_name, 11))
        self.state = 0
        self.checkFilenameIsUidBox_json_list_2.stateChanged.connect(self.check_box_result)
        layout_start.addWidget(self.checkFilenameIsUidBox_json_list_2)
        self.cancel_button_json_list_2 = QPushButton('Cancel', self)
        self.cancel_button_json_list_2.setFont(QFont(self.font_name, 14))
        self.cancel_button_json_list_2.clicked.connect(self.stop_thread_json_list_2)
        layout_start.addStretch()
        layout_start.addWidget(self.cancel_button_json_list_2)
        layout_start.addWidget(self.extract_button_json_list_2)
        self.extract_button_json_list_2.setShortcut('Return')
        tab_2param.layout.addLayout(layout_start)
        # set layout
        tab_2param.setLayout(tab_2param.layout)
        self.right_widget.addTab(tab_2param, 'two keys')

    def json_list_2_3param_ui(self):
        tab_2_3param = QWidget()
        # overall layout
        tab_2_3param.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        json_2_3param_open_folder_button = QPushButton('Open Folder', self)
        json_2_3param_open_folder_button.setFont(QFont(self.font_name, 12))
        json_2_3param_open_folder_button.clicked.connect(self.open_folder_dialog)
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(json_2_3param_open_folder_button, stretch=3)
        tab_2_3param.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_json_2_3param = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_json_2_3param.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_json_2_3param, stretch=3)
        tab_2_3param.layout.addLayout(layout_save_filename)
        # judge
        layout_judge_filename = QHBoxLayout()
        label_judge = QLabel('Judge')
        self.edit_judge_filename_json_2_3param = QLineEdit()
        label_judge.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_json_2_3param.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_json_2_3param, stretch=3)
        tab_2_3param.layout.addLayout(layout_judge_filename)
        # param value 1, 2, 3
        layout_param_value_1 = QHBoxLayout()
        label_param_value_1 = QLabel('Key 2-1')
        self.edit_param_value_json_2_3param_1 = QLineEdit()
        self.edit_param_value_json_2_3param_1.setFont(QFont(self.font_name, self.partly_size))
        label_param_value_1.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_1.addWidget(label_param_value_1, stretch=1)
        layout_param_value_1.addWidget(self.edit_param_value_json_2_3param_1, stretch=3)
        tab_2_3param.layout.addLayout(layout_param_value_1)
        layout_param_value_2 = QHBoxLayout()
        label_param_value_2 = QLabel('Key 2-2')
        self.edit_param_value_json_2_3param_2 = QLineEdit()
        label_param_value_2.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_2_3param_2.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_2.addWidget(label_param_value_2, stretch=1)
        layout_param_value_2.addWidget(self.edit_param_value_json_2_3param_2, stretch=3)
        tab_2_3param.layout.addLayout(layout_param_value_2)
        layout_param_value_3 = QHBoxLayout()
        label_param_value_3 = QLabel('Key 2-3')
        self.edit_param_value_json_2_3param_3 = QLineEdit()
        label_param_value_3.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_2_3param_3.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_3.addWidget(label_param_value_3, stretch=1)
        layout_param_value_3.addWidget(self.edit_param_value_json_2_3param_3, stretch=3)
        tab_2_3param.layout.addLayout(layout_param_value_3)
        # show process
        self.progress_bar_json_list_2_3 = QProgressBar()
        self.progress_bar_json_list_2_3.setMinimum(0)
        self.progress_bar_json_list_2_3.setMaximum(100)
        tab_2_3param.layout.addWidget(self.progress_bar_json_list_2_3)
        # start and cancel button
        layout_start = QHBoxLayout()
        self.extract_button_json_list_2_3 = QPushButton('Extract', self)
        self.extract_button_json_list_2_3.clicked.connect(self.function_json_list_2_3)
        self.extract_button_json_list_2_3.setFont(QFont(self.font_name, 14))
        # self.progress_label = QLabel(self)
        # layout_start.addWidget(self.progress_label)
        self.cancel_button_json_list_2_3 = QPushButton('Cancel', self)
        self.cancel_button_json_list_2_3.setFont(QFont(self.font_name, 14))
        self.cancel_button_json_list_2_3.clicked.connect(self.stop_thread_json_list_2_3)
        layout_start.addStretch()
        layout_start.addWidget(self.cancel_button_json_list_2_3)
        layout_start.addWidget(self.extract_button_json_list_2_3)
        self.extract_button_json_list_2_3.setShortcut('Return')
        tab_2_3param.layout.addLayout(layout_start)
        # set layout
        tab_2_3param.setLayout(tab_2_3param.layout)
        self.right_widget.addTab(tab_2_3param, 'two-3 keys')

    def json_list_3param_ui(self):

        tab_3param = QWidget()
        # overall layout
        tab_3param.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        json_3param_open_folder_button = QPushButton('Open Folder', self)
        json_3param_open_folder_button.setFont(QFont(self.font_name, 12))
        json_3param_open_folder_button.clicked.connect(self.open_folder_dialog)
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(json_3param_open_folder_button, stretch=3)
        tab_3param.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_json_3param = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_json_3param.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_json_3param, stretch=3)
        tab_3param.layout.addLayout(layout_save_filename)
        # judge
        layout_judge_filename = QHBoxLayout()
        label_judge = QLabel('Judge')
        self.edit_judge_filename_json_3param = QLineEdit()
        label_judge.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_json_3param.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_json_3param, stretch=3)
        tab_3param.layout.addLayout(layout_judge_filename)
        # param value 1, 2, 3
        layout_param_value_1 = QHBoxLayout()
        label_param_value_1 = QLabel('Key 1')
        self.edit_param_value_json_3param_1 = QLineEdit()
        self.edit_param_value_json_3param_1.setFont(QFont(self.font_name, self.partly_size))
        label_param_value_1.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_1.addWidget(label_param_value_1, stretch=1)
        layout_param_value_1.addWidget(self.edit_param_value_json_3param_1, stretch=3)
        tab_3param.layout.addLayout(layout_param_value_1)
        layout_param_value_2 = QHBoxLayout()
        label_param_value_2 = QLabel('Key 2')
        self.edit_param_value_json_3param_2 = QLineEdit()
        label_param_value_2.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_3param_2.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_2.addWidget(label_param_value_2, stretch=1)
        layout_param_value_2.addWidget(self.edit_param_value_json_3param_2, stretch=3)
        tab_3param.layout.addLayout(layout_param_value_2)
        layout_param_value_3 = QHBoxLayout()
        label_param_value_3 = QLabel('Key 3')
        self.edit_param_value_json_3param_3 = QLineEdit()
        label_param_value_3.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_json_3param_3.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_3.addWidget(label_param_value_3, stretch=1)
        layout_param_value_3.addWidget(self.edit_param_value_json_3param_3, stretch=3)
        tab_3param.layout.addLayout(layout_param_value_3)
        # show process
        self.progress_bar_json_list_3 = QProgressBar()
        self.progress_bar_json_list_3.setMinimum(0)
        self.progress_bar_json_list_3.setMaximum(100)
        tab_3param.layout.addWidget(self.progress_bar_json_list_3)
        # start and cancel button
        layout_start = QHBoxLayout()
        self.extract_button_json_list_3 = QPushButton('Extract', self)
        self.extract_button_json_list_3.clicked.connect(self.function_json_list_3)
        self.extract_button_json_list_3.setFont(QFont(self.font_name, 14))
        self.cancel_button_json_list_3 = QPushButton('Cancel', self)
        self.cancel_button_json_list_3.setFont(QFont(self.font_name, 14))
        # self.cancel_button_json_list_3.clicked.connect(self.function_json_list_3_cancel)
        layout_start.addStretch()
        layout_start.addWidget(self.cancel_button_json_list_3)
        layout_start.addWidget(self.extract_button_json_list_3)
        self.extract_button_json_list_3.setShortcut('Return')
        tab_3param.layout.addLayout(layout_start)
        # set layout
        tab_3param.setLayout(tab_3param.layout)
        self.right_widget.addTab(tab_3param, 'three keys')

    def html_pandas_regular_ui(self):

        tab_html_regular = QWidget()
        # overall layout
        tab_html_regular.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        html_regular_open_folder_button = QPushButton('Open Folder', self)
        html_regular_open_folder_button.setFont(QFont(self.font_name, 12))
        html_regular_open_folder_button.clicked.connect(self.open_folder_dialog)
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(html_regular_open_folder_button, stretch=3)
        tab_html_regular.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_html_regular = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_html_regular.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_html_regular, stretch=3)
        tab_html_regular.layout.addLayout(layout_save_filename)
        # file judge
        layout_judge_filename = QHBoxLayout()
        label_judge_filename = QLabel('File Judge')
        self.edit_judge_filename_html_regular = QLineEdit()
        label_judge_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_html_regular.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge_filename, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_html_regular, stretch=3)
        tab_html_regular.layout.addLayout(layout_judge_filename)
        # data judge
        layout_dataframe_idx = QHBoxLayout()
        label_dataframe_idx = QLabel('Data Judge')
        self.edit_dataframe_idx_html_regular = QLineEdit()
        label_dataframe_idx.setFont(QFont(self.font_name, self.partly_size))
        self.edit_dataframe_idx_html_regular.setFont(QFont(self.font_name, self.partly_size))
        layout_dataframe_idx.addWidget(label_dataframe_idx, stretch=1)
        layout_dataframe_idx.addWidget(self.edit_dataframe_idx_html_regular, stretch=3)
        tab_html_regular.layout.addLayout(layout_dataframe_idx)
        # param value 1, 2, 3
        # layout_param_value_1 = QHBoxLayout()
        # label_param_value_1 = QLabel('Key 1')
        # self.edit_param_value_html_168detail_1 = QLineEdit()
        # self.edit_param_value_html_168detail_1.setFont(QFont(self.font_name, self.partly_size))
        # label_param_value_1.setFont(QFont(self.font_name, self.partly_size))
        # layout_param_value_1.addWidget(label_param_value_1, stretch=1)
        # layout_param_value_1.addWidget(self.edit_param_value_html_168detail_1, stretch=3)
        # tab_html_regular.layout.addLayout(layout_param_value_1)
        # layout_param_value_2 = QHBoxLayout()
        # label_param_value_2 = QLabel('Key 2')
        # self.edit_param_value_html_168detail_2 = QLineEdit()
        # label_param_value_2.setFont(QFont(self.font_name, self.partly_size))
        # self.edit_param_value_html_168detail_2.setFont(QFont(self.font_name, self.partly_size))
        # layout_param_value_2.addWidget(label_param_value_2, stretch=1)
        # layout_param_value_2.addWidget(self.edit_param_value_html_168detail_2, stretch=3)
        # tab_html_regular.layout.addLayout(layout_param_value_2)
        # show process
        self.progress_bar_html_regular = QProgressBar()
        self.progress_bar_html_regular.setMinimum(0)
        self.progress_bar_html_regular.setMaximum(100)
        tab_html_regular.layout.addWidget(self.progress_bar_html_regular)
        # start, test and cancel button
        layout_start = QHBoxLayout()
        self.extract_button_html_regular = QPushButton('Extract', self)
        # self.extract_button_html_regular.clicked.connect(self.function_html_regular)
        self.extract_button_html_regular.setFont(QFont(self.font_name, 14))
        self.cancel_button_html_regular = QPushButton('Cancel', self)
        self.cancel_button_html_regular.setFont(QFont(self.font_name, 14))
        # self.cancel_button_html_regular.clicked.connect(self.stop_thread_html_regular)
        # is it have useless data
        self.checkDataIsHaveUselessDataBox_html_regular = QCheckBox('have useless data.')
        self.checkDataIsHaveUselessDataBox_html_regular.setFont(QFont(self.state_font_name, 11))
        self.state = 0
        self.checkDataIsHaveUselessDataBox_html_regular.stateChanged.connect(self.check_box_result)
        layout_start.addWidget(self.checkDataIsHaveUselessDataBox_html_regular)
        # read_html list length label
        label_length = QLabel()
        label_length.setFont(QFont(self.state_font_name, 10))
        layout_start.addWidget(label_length)
        layout_start.addStretch()
        # test button
        self.test_button_html_regular = QPushButton('Test', self)
        self.test_button_html_regular.setFont(QFont(self.font_name, 14))
        self.test_state = 0
        # self.test_button_html_regular.clicked.connect(self.function_html_regular_isTest)
        layout_start.addWidget(self.cancel_button_html_regular)
        layout_start.addWidget(self.test_button_html_regular)
        layout_start.addWidget(self.extract_button_html_regular)
        self.extract_button_html_regular.setShortcut('Return')
        tab_html_regular.layout.addLayout(layout_start)
        # set layout
        tab_html_regular.setLayout(tab_html_regular.layout)
        self.right_widget.addTab(tab_html_regular, 'regular')

    def html_pandas_168detail_ui(self):

        tab_html_168detail = QWidget()
        # overall layout
        tab_html_168detail.layout = QVBoxLayout()
        # folder select
        layout_file_select = QHBoxLayout()
        label_file_select = QLabel('Folder')
        html_168detail_open_folder_button = QPushButton('Open Folder', self)
        html_168detail_open_folder_button.setFont(QFont(self.font_name, 12))
        html_168detail_open_folder_button.clicked.connect(self.open_folder_dialog)
        label_file_select.setFont(QFont(self.font_name, self.partly_size))
        layout_file_select.addWidget(label_file_select, stretch=1)
        layout_file_select.addWidget(html_168detail_open_folder_button, stretch=3)
        tab_html_168detail.layout.addLayout(layout_file_select)
        # save filename
        layout_save_filename = QHBoxLayout()
        label_filename = QLabel('Filename')
        self.edit_filename_html_168detail = QLineEdit()
        label_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_filename_html_168detail.setFont(QFont(self.font_name, self.partly_size))
        layout_save_filename.addWidget(label_filename, stretch=1)
        layout_save_filename.addWidget(self.edit_filename_html_168detail, stretch=3)
        tab_html_168detail.layout.addLayout(layout_save_filename)
        # file judge
        layout_judge_filename = QHBoxLayout()
        label_judge_filename = QLabel('File Judge')
        self.edit_judge_filename_html_168detail = QLineEdit()
        label_judge_filename.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_filename_html_168detail.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_filename.addWidget(label_judge_filename, stretch=1)
        layout_judge_filename.addWidget(self.edit_judge_filename_html_168detail, stretch=3)
        tab_html_168detail.layout.addLayout(layout_judge_filename)
        # data judge
        layout_judge_data = QHBoxLayout()
        label_judge_data = QLabel('Data Judge')
        self.edit_judge_data_html_168detail = QLineEdit()
        label_judge_data.setFont(QFont(self.font_name, self.partly_size))
        self.edit_judge_data_html_168detail.setFont(QFont(self.font_name, self.partly_size))
        layout_judge_data.addWidget(label_judge_data, stretch=1)
        layout_judge_data.addWidget(self.edit_judge_data_html_168detail, stretch=3)
        tab_html_168detail.layout.addLayout(layout_judge_data)
        # param value 1, 2, 3
        layout_param_value_1 = QHBoxLayout()
        label_param_value_1 = QLabel('Key 1')
        self.edit_param_value_html_168detail_1 = QLineEdit()
        self.edit_param_value_html_168detail_1.setFont(QFont(self.font_name, self.partly_size))
        label_param_value_1.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_1.addWidget(label_param_value_1, stretch=1)
        layout_param_value_1.addWidget(self.edit_param_value_html_168detail_1, stretch=3)
        tab_html_168detail.layout.addLayout(layout_param_value_1)
        layout_param_value_2 = QHBoxLayout()
        label_param_value_2 = QLabel('Key 2')
        self.edit_param_value_html_168detail_2 = QLineEdit()
        label_param_value_2.setFont(QFont(self.font_name, self.partly_size))
        self.edit_param_value_html_168detail_2.setFont(QFont(self.font_name, self.partly_size))
        layout_param_value_2.addWidget(label_param_value_2, stretch=1)
        layout_param_value_2.addWidget(self.edit_param_value_html_168detail_2, stretch=3)
        tab_html_168detail.layout.addLayout(layout_param_value_2)
        # show process
        self.progress_bar_html_168detail = QProgressBar()
        self.progress_bar_html_168detail.setMinimum(0)
        self.progress_bar_html_168detail.setMaximum(100)
        tab_html_168detail.layout.addWidget(self.progress_bar_html_168detail)
        # start, test and cancel button
        layout_start = QHBoxLayout()
        self.extract_button_html_168detail = QPushButton('Extract', self)
        self.extract_button_html_168detail.clicked.connect(self.function_html_168detail)
        self.extract_button_html_168detail.setFont(QFont(self.font_name, 14))
        self.cancel_button_html_168detail = QPushButton('Cancel', self)
        self.cancel_button_html_168detail.setFont(QFont(self.font_name, 14))
        self.cancel_button_html_168detail.clicked.connect(self.stop_thread_html_168detail)
        # tips label
        label_tips = QLabel('Attention: Need Json Files')
        label_tips.setFont(QFont(self.state_font_name, 11))
        layout_start.addWidget(label_tips)
        layout_start.addStretch()
        # test button
        self.test_button_html_168detail = QPushButton('Test', self)
        self.test_button_html_168detail.setFont(QFont(self.font_name, 14))
        self.test_state = 0
        self.test_button_html_168detail.clicked.connect(self.function_html_168detail_isTest)
        layout_start.addWidget(self.cancel_button_html_168detail)
        layout_start.addWidget(self.test_button_html_168detail)
        layout_start.addWidget(self.extract_button_html_168detail)
        self.extract_button_html_168detail.setShortcut('Return')
        tab_html_168detail.layout.addLayout(layout_start)
        # set layout
        tab_html_168detail.setLayout(tab_html_168detail.layout)
        self.right_widget.addTab(tab_html_168detail, '168detail')

    '''share function'''
    def check_box_result(self):

        cb = self.sender()
        if cb.isChecked():
            self.state = 1
        else:
            self.state = 0

    # TODO one param
    '''json list 1'''
    def function_json_list_1(self):
        pass

    '''json list 2'''
    def check_edit_empty_json_list_2(self):

        if self.edit_filename_json_2param.text() == '' and self.edit_param_value_json_2param_1.text() == '' and self.edit_param_value_json_2param_2.text() == '' and self.edit_judge_filename_json_2param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Text is not allowed to be empty.')
            return
        elif self.edit_filename_json_2param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Filename is not allowed to be empty.')
            return
        elif self.edit_judge_filename_json_2param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Judge is not allowed to be empty.')
            return
        elif self.edit_param_value_json_2param_1.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 1 is not allowed to be empty.')
            return
        elif self.edit_param_value_json_2param_2.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 2 is not allowed to be empty.')
            return
        else:
            return

    def function_json_list_2(self):

        self.extract_button_json_list_2.setEnabled(False)
        self.check_edit_empty_json_list_2()

        self.flag = 1
        QTimer.singleShot(0, self.thread_start_json_list_2)

    def thread_start_json_list_2(self):

        filename = self.edit_filename_json_2param.text()
        judge = self.edit_judge_filename_json_2param.text()
        key_1 = self.edit_param_value_json_2param_1.text()
        key_2 = self.edit_param_value_json_2param_2.text()
        state = self.state

        self.thread = ThreadJsonList_2(self.folder_path, filename, judge, key_1, key_2, state)
        self.thread.signal.connect(self.handle_signal_json_list_2)
        self.thread.start()
        self.begin_time = time.time()

    def handle_signal_json_list_2(self, data):
        signal_type = data.get('type')
        signal_data = data.get('data')

        if signal_type == 'progress':
            self.update_progress_json_list_2(signal_data)
        elif signal_type == 'finish':
            self.process_finished_json_list_2(signal_data)
        elif signal_type == 'error':
            self.show_error_message_json_list_2(signal_data)

    def update_progress_json_list_2(self, progress):
        # self.progress_label_json_list_2.setText(f"Traversal Progress: {progress}%")
        # print(self.)
        self.progress_bar_json_list_2.setValue(progress)
        if self.flag == 1:
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Begin')
            self.flag = 0
            try:
                self.statusBar().removeWidget(self.right_label)
            except:
                pass
            self.right_label = QLabel('Running', self)
            self.statusBar().addPermanentWidget(self.right_label)

    def process_finished_json_list_2(self, fail_file):
        if fail_file == '':
            pass
        else:
            reply = QMessageBox.information(self, 'Read Fail Files', fail_file)
        self.end_time = time.time()
        # self.progress_label_2.setText("Traversal Completed!")
        self.extract_button_json_list_2.setEnabled(True)
        time_interval = self.end_time - self.begin_time
        if time_interval <= 60:
            self.right_label.setText(f'Run time: {int(time_interval)}s')
        elif time_interval <= 3600:
            self.right_label.setText(f'Run time: {int(time_interval // 60)}m{int(time_interval % 60)}s')
        else:
            self.right_label.setText(f'Run time: {int(time_interval // 3600)}h{int((time_interval % 3600) // 60)}m{int(time_interval % 60)}s')
        self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Complete')
        self.statusBar().addPermanentWidget(self.right_label)

    def show_error_message_json_list_2(self, error_message):
        reply = QMessageBox.critical(self, 'Error', error_message)
        self.extract_button_json_list_2.setEnabled(True)

    def stop_thread_json_list_2(self):

        if hasattr(self, 'thread') and self.thread.isRunning():  # 检查线程是否正在运行
            self.thread.cancel()
            del self.thread
            gc.collect()
            self.extract_button_json_list_2.setEnabled(True)
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Interrupt')
            self.right_label.setText('Process Canceled.')
            self.statusBar().addPermanentWidget(self.right_label)

    '''json list 2_3'''
    def check_edit_empty_json_list_2_3(self):

        if self.edit_filename_json_2_3param.text() == '' and self.edit_param_value_json_2_3param_1.text() == '' and self.edit_param_value_json_2_3param_2.text() == '' and self.edit_param_value_json_2_3param_3.text() == '' and self.edit_judge_filename_json_2_3param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Text is not allowed to be empty.')
            return
        elif self.edit_filename_json_2_3param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Filename is not allowed to be empty.')
            return
        elif self.edit_judge_filename_json_2_3param.text() == '':
            QMessageBox.warning(self, 'Warning', 'Judge is not allowed to be empty.')
            return
        elif self.edit_param_value_json_2_3param_1.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 1 is not allowed to be empty.')
            return
        elif self.edit_param_value_json_2_3param_2.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 2 is not allowed to be empty.')
            return
        elif self.edit_param_value_json_2_3param_3.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 3 is not allowed to be empty.')
            return
        else:
            return

    def function_json_list_2_3(self):

        # 防止多次点击按钮
        self.extract_button_json_list_2_3.setEnabled(False)
        self.check_edit_empty_json_list_2_3()
        self.flag = 1
        QTimer.singleShot(0, self.thread_start_json_list_2_3)

    def thread_start_json_list_2_3(self):

        filename = self.edit_filename_json_2_3param.text()
        judge = self.edit_judge_filename_json_2_3param.text()
        key_1 = self.edit_param_value_json_2_3param_1.text()
        key_2 = self.edit_param_value_json_2_3param_2.text()
        key_3 = self.edit_param_value_json_2_3param_3.text()

        self.thread = ThreadJsonList_2_3(self.folder_path, filename, judge, key_1, key_2, key_3)
        self.thread.signal.connect(self.handle_signal_json_list_2_3)
        # self.thread.signal.connect(self.show_error_message)
        # self.thread.signal.connect(self.update_progress)
        # self.thread.finished.connect(self.traversal_finished)
        self.thread.start()
        self.begin_time = time.time()

    def handle_signal_json_list_2_3(self, data):
        signal_type = data.get('type')
        signal_data = data.get('data')
        if signal_type == 'progress':
            self.update_progress_json_list_2_3(signal_data)
        elif signal_type == 'finish':
            self.process_finished_json_list_2_3(signal_data)
        elif signal_type == 'error':
            self.show_error_message_json_list_2_3(signal_data)

    def update_progress_json_list_2_3(self, progress):
        # self.progress_label_json_list_2.setText(f"Traversal Progress: {progress}%")
        # print(self.)
        self.progress_bar_json_list_2_3.setValue(progress)
        if self.flag == 1:
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Begin')
            self.flag = 0
            try:
                self.statusBar().removeWidget(self.right_label)
            except:
                pass
            self.right_label = QLabel('Running', self)
            self.statusBar().addPermanentWidget(self.right_label)

    def process_finished_json_list_2_3(self, fail_file):
        if fail_file == '':
            pass
        else:
            reply = QMessageBox.information(self, 'Read Fail Files', fail_file)
        self.end_time = time.time()
        time_interval = self.end_time - self.begin_time
        if time_interval <= 60:
            self.right_label.setText(f'Run time: {int(time_interval)}s')
        elif time_interval <= 3600:
            self.right_label.setText(f'Run time: {int(time_interval // 60)}m{int(time_interval % 60)}s')
        else:
            self.right_label.setText(f'Run time: {int(time_interval // 3600)}h{int((time_interval % 3600) // 60)}m{int(time_interval % 60)}s')
        self.extract_button_json_list_2_3.setEnabled(True)
        self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Complete')
        self.statusBar().addPermanentWidget(self.right_label)

    def show_error_message_json_list_2_3(self, error_message):
        reply = QMessageBox.critical(self, 'Error', error_message)
        self.extract_button_json_list_2_3.setEnabled(True)

    def stop_thread_json_list_2_3(self):

        if hasattr(self, 'thread') and self.thread.isRunning():  # 检查线程是否正在运行
            self.thread.cancel()
            del self.thread
            gc.collect()
            self.extract_button_json_list_2_3.setEnabled(True)
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Interrupt')
            self.right_label.setText('Process Canceled.')
            self.statusBar().addPermanentWidget(self.right_label)

    # TODO three param
    '''json list 3'''
    def function_json_list_3(self):
        pass

    '''html 168detail model'''
    def check_edit_empty_html_168detail(self):

        if self.edit_filename_html_168detail.text() == '' and self.edit_judge_filename_html_168detail.text() == '' and self.edit_judge_data_html_168detail.text() == '' and self.edit_param_value_html_168detail_1.text() == '' and self.edit_param_value_html_168detail_2.text() == '':
            QMessageBox.warning(self, 'Warning', 'Text is not allowed to be empty.')
            return
        elif self.edit_filename_html_168detail.text() == '':
            QMessageBox.warning(self, 'Warning', 'Filename is not allowed to be empty.')
            return
        elif self.edit_judge_filename_html_168detail.text() == '':
            QMessageBox.warning(self, 'Warning', 'File Judge is not allowed to be empty.')
            return
        elif self.edit_judge_data_html_168detail.text() == '':
            QMessageBox.warning(self, 'Warning', 'Data Judge is not allowed to be empty.')
            return
        elif self.edit_param_value_html_168detail_1.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 1 is not allowed to be empty.')
            return
        elif self.edit_param_value_html_168detail_2.text() == '':
            QMessageBox.warning(self, 'Warning', 'Key 2 is not allowed to be empty.')
            return
        else:
            return

    def function_html_168detail(self):

        self.extract_button_html_168detail.setEnabled(False)
        self.check_edit_empty_html_168detail()
        self.flag = 1
        QTimer.singleShot(0, self.thread_start_html_168detail)

    def function_html_168detail_isTest(self):

        self.check_edit_empty_html_168detail()
        self.flag = 1
        self.test_state = 1
        QTimer.singleShot(0, self.thread_start_html_168detail)

    def thread_start_html_168detail(self):

        filename = self.edit_filename_html_168detail.text()
        judge_file = self.edit_judge_filename_html_168detail.text()
        judge_data = self.edit_judge_data_html_168detail.text()
        key_1 = self.edit_param_value_html_168detail_1.text()
        key_2 = self.edit_param_value_html_168detail_2.text()
        test_state = self.test_state

        self.thread = ThreadHtml168Detail(self.folder_path, filename, judge_file, judge_data, key_1, key_2, test_state)
        self.thread.signal.connect(self.handle_signal_html_168detail)
        self.thread.start()
        self.begin_time = time.time()

    def handle_signal_html_168detail(self, data):
        signal_type = data.get('type')
        signal_data = data.get('data')
        if signal_type == 'progress':
            self.update_progress_html_168detail(signal_data)
        elif signal_type == 'finish':
            self.process_finished_html_168detail(signal_data)
        elif signal_type == 'error':
            self.show_error_message_html_168detail(signal_data)

    def update_progress_html_168detail(self, progress):

        self.progress_bar_html_168detail.setValue(progress)
        if self.flag == 1:
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Begin')
            self.flag = 0
            try:
                self.statusBar().removeWidget(self.right_label)
            except:
                pass
            self.right_label = QLabel('Running', self)
            self.statusBar().addPermanentWidget(self.right_label)

    def process_finished_html_168detail(self, fail_file):
        if fail_file == '':
            pass
        else:
            reply = QMessageBox.information(self, 'Read Fail Files', fail_file)
        self.end_time = time.time()
        time_interval = self.end_time - self.begin_time
        if time_interval <= 60:
            self.right_label.setText(f'Run time: {int(time_interval)}s')
        elif time_interval <= 3600:
            self.right_label.setText(f'Run time: {int(time_interval // 60)}m{int(time_interval % 60)}s')
        else:
            self.right_label.setText(f'Run time: {int(time_interval // 3600)}h{int((time_interval % 3600) // 60)}m{int(time_interval % 60)}s')
        self.extract_button_html_168detail.setEnabled(True)
        self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Complete')
        self.statusBar().addPermanentWidget(self.right_label)

    def show_error_message_html_168detail(self, error_message):
        reply = QMessageBox.critical(self, 'Error', error_message)
        self.extract_button_html_168detail.setEnabled(True)

    def stop_thread_html_168detail(self):

        if hasattr(self, 'thread') and self.thread.isRunning():  # 检查线程是否正在运行
            self.thread.cancel()
            del self.thread
            gc.collect()
            self.extract_button_html_168detail.setEnabled(True)
            self.statusBar().showMessage(f'Folder {os.path.basename(self.folder_path)} already be selected-Interrupt')
            self.right_label.setText('Process Canceled.')
            self.statusBar().addPermanentWidget(self.right_label)


def main():

    warnings.filterwarnings('ignore')
    app = QApplication(sys.argv)
    extract = MainWindow()
    extract.show()
    sys.exit(app.exec())


if __name__ == '__main__':

    main()
