# -*- coding: utf-8 -*-
# @Time    :  2023/12/13 13:08
# @File    :  ExtractDataFunction.py
# @IDE     :  PyCharm

"""
"""
import json
import os
import time

import pandas as pd
from PyQt6.QtCore import QMutex, QThread, pyqtSignal


mutex = QMutex()


# 功能实现区
class ThreadJsonList_2(QThread):

    signal = pyqtSignal(object)  # 括号里填写信号传递的参数

    def __init__(self, folder_path, save_filename, judge_filename, key_1, key_2, state):

        super(ThreadJsonList_2, self).__init__()

        self.running = True

        self.folder_path = folder_path
        self.save_filename = save_filename
        self.judge_filename = judge_filename
        self.key_1 = key_1
        self.key_2 = key_2
        self.state = state

    def run(self):
        """
        提取开始
        :return:
        """
        try:
            mutex.lock()
            result = []
            fail_file = ''
            files = [f for f in os.listdir(self.folder_path) if self.judge_filename in f]
            num_files = len(files)
            key_1 = self.key_1
            key_2 = self.key_2
            for i, file_name in enumerate(files):
                time.sleep(0.06)
                file = os.path.join(self.folder_path, file_name)
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                if self.state == 1:
                    if len(data[key_1][key_2]) != 0:
                        for d1 in data[key_1][key_2]:
                            d1['uid'] = file_name.split('-')[0]
                            result += [d1]
                    elif len(data[key_1][key_2]) == 0:
                        progress = int((i + 1) * 100 / num_files)
                        self.signal.emit({'type': 'progress', 'data': progress})
                        continue
                    else:
                        fail_file += file_name
                    progress = int((i + 1) * 100 / num_files)
                    self.signal.emit({'type': 'progress', 'data': progress})
                else:
                    if len(data[key_1][key_2]) != 0:
                        result += data[key_1][key_2]
                    elif len(data[key_1][key_2]) == 0:
                        progress = int((i + 1) * 100 / num_files)
                        self.signal.emit({'type': 'progress', 'data': progress})
                        continue
                    else:
                        fail_file += file_name
                    progress = int((i + 1) * 100 / num_files)
                    self.signal.emit({'type': 'progress', 'data': progress})
                # self.signal.emit(progress)
                if not self.running:
                    mutex.unlock()
                    return
            parent_dir = os.path.dirname(os.path.dirname(self.folder_path))
            if os.path.exists(os.path.join(parent_dir, 'handle', 'original_data')):
                pass
            else:
                os.mkdir(os.path.join(parent_dir, 'handle', 'original_data'))
            df = pd.DataFrame(result)
            df.to_csv(os.path.join(parent_dir, 'handle', 'original_data', f'{self.save_filename}.csv'), encoding='utf-8', index=False)
            self.signal.emit({'type': 'finish', 'data': fail_file})
            mutex.unlock()
        except Exception as e:
            self.signal.emit({'type': 'error', 'data': str(e)})

    def cancel(self):

        self.running = False


class ThreadJsonList_2_3(QThread):

    signal = pyqtSignal(object)  # 括号里填写信号传递的参数

    def __init__(self, folder_path, save_filename, judge_filename, key_1, key_2, key_3):

        super(ThreadJsonList_2_3, self).__init__()

        self.running = True

        self.folder_path = folder_path
        self.save_filename = save_filename
        self.judge_filename = judge_filename
        self.key_1 = key_1
        self.key_2 = key_2
        self.key_3 = key_3

    def run(self):
        """
        提取开始
        :return:
        """
        try:
            mutex.lock()
            result = []
            fail_file = ''
            files = [f for f in os.listdir(self.folder_path) if self.judge_filename in f]
            num_files = len(files)
            key_1 = self.key_1
            key_2 = self.key_2
            key_3 = self.key_3

            for i, file_name in enumerate(files):
                time.sleep(0.06)
                file = os.path.join(self.folder_path, file_name)
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                if (len(data[key_1][key_2]) != 0) and (len(data[key_1][key_3]) == 0):
                    for d1 in data[key_1][key_2]:
                        d1['uid'] = file_name.split('-')[0]
                        result += [d1]
                elif (len(data[key_1][key_2]) == 0) and (len(data[key_1][key_3]) != 0):
                    for d2 in data[key_1][key_2]:
                        d2['uid'] = file_name.split('-')[0]
                        result += [d2]
                elif (len(data[key_1][key_2]) != 0) and (len(data[key_1][key_3]) != 0):
                    for d1 in data[key_1][key_2]:
                        d1['uid'] = file_name.split('-')[0]
                        result += [d1]
                    for d2 in data[key_1][key_3]:
                        d2['uid'] = file_name.split('-')[0]
                        result += [d2]
                elif (len(data[key_1][key_2]) == 0) and (len(data[key_1][key_3]) == 0):
                    progress = int((i + 1) * 100 / num_files)
                    self.signal.emit({'type': 'progress', 'data': progress})
                    continue
                else:
                    fail_file += file_name
                progress = int((i + 1) * 100 / num_files)
                self.signal.emit({'type': 'progress', 'data': progress})
                # self.signal.emit(progress)
                if not self.running:
                    mutex.unlock()
                    return
            parent_dir = os.path.dirname(os.path.dirname(self.folder_path))
            if os.path.exists(os.path.join(parent_dir, 'handle', 'original_data')):
                pass
            else:
                os.mkdir(os.path.join(parent_dir, 'handle', 'original_data'))
            df = pd.DataFrame(result)
            df.to_csv(os.path.join(parent_dir, 'handle', 'original_data', f'{self.save_filename}.csv'), encoding='utf-8', index=False)
            self.signal.emit({'type': 'finish', 'data': fail_file})
            mutex.unlock()
        except Exception as e:
            self.signal.emit({'type': 'error', 'data': str(e)})

    def cancel(self):

        self.running = False


class ThreadHtml168Detail(QThread):

    signal = pyqtSignal(object)

    def __init__(self, folder_path, save_filename, judge_filename, judge_data, key_1, key_2, isTest):

        super(ThreadHtml168Detail, self).__init__()

        self.running = True

        self.folder_path = folder_path
        self.save_filename = save_filename
        self.judge_filename = judge_filename
        self.judge_data = judge_data
        self.key_1 = key_1
        self.key_2 = key_2
        self.test_state = isTest

    def run(self):
        """
        提取开始
        :return:
        """
        try:
            mutex.lock()
            result = []
            if self.test_state == 0:
                files = [f for f in os.listdir(self.folder_path) if self.judge_filename in f]
            else:
                files = [f for f in os.listdir(self.folder_path) if self.judge_filename in f][: 100]
            num_files = len(files)
            key_1 = self.key_1
            key_2 = self.key_2
            judge_data = self.judge_data

            for i, file_name in enumerate(files):
                # time.sleep(0.06)
                file = os.path.join(self.folder_path, file_name)
                with open(file, 'r', encoding='utf-8') as f:
                    data = json.loads(f.read())
                if data[key_1][judge_data]:
                    html_text = pd.read_html(data[key_1][key_2])
                    table = html_text[0].T
                    table.columns = table.iloc[0, :]
                    table1 = table.iloc[1, :]
                    table1['名称'] = table.iloc[3, 0]
                    table1['额度'] = table.iloc[3, 1]
                    table1['注册来源'] = table.iloc[3, 2]
                    table1['最后出款时间'] = table.iloc[3, 7]
                    table1['会员层级'] = table.iloc[3, 9]
                    table1['双重验证'] = table.iloc[3, 10]

                    table1 = pd.DataFrame(table1).T
                    table1['uid'] = file_name.split('.')[0]

                    table1.columns = ['会员账号', '状态', '新增日期', '注册IP', '最后登入IP', '最后登入时间', '6',
                                      '最后入款时间', '8', '最后下注游戏', '当前使用钱包', '等级', '备注', '13',
                                      '名称', '额度', '注册来源', '最后出款时间', '会员层级', '双重验证', 'uid']
                    result.append(table1)
                else:
                    progress = int((i + 1) * 100 / num_files)
                    self.signal.emit({'type': 'progress', 'data': progress})
                    continue
                progress = int((i + 1) * 100 / num_files)
                self.signal.emit({'type': 'progress', 'data': progress})
                if not self.running:
                    mutex.unlock()
                    return
            parent_dir = os.path.dirname(os.path.dirname(self.folder_path))
            if os.path.exists(os.path.join(parent_dir, 'handle', 'original_data')):
                pass
            else:
                os.mkdir(os.path.join(parent_dir, 'handle', 'original_data'))
            df = pd.concat(result)
            df.to_csv(os.path.join(parent_dir, 'handle', 'original_data', f'{self.save_filename}.csv'), encoding='utf-8', index=False)
            self.signal.emit({'type': 'finish', 'data': ''})
            mutex.unlock()
        except Exception as e:
            if str(file_name) != '':
                self.signal.emit({'type': 'error', 'data': str(e) + ', File:' + str(file_name)})
            else:
                self.signal.emit({'type': 'error', 'data': str(e)})

    def cancel(self):

        self.running = False
