# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/18 14:32
# @File    :  eg.py
# @IDE     :  PyCharm

"""
"""
import pandas as pd


if __name__ == '__main__':

    path = 'C:\\Users\\admin\\Desktop\\WorkSpace\\am\\am\\user\\1.html'
    readTable = pd.read_html(path)
