# -*- coding: UTF-8 -*-
"""
@File    ：readFile.py
@Author  ：xin-w
@Date    ：2023/7/10 19:22 
@IDE     ：PyCharm 
"""


import os
import json
import time
import traceback

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree


class Handle:
    def txt2csv(self, path, fname, filename, keyNum, **dic):
        """

        :param path: 文件路径
        :param fname: 文件包含名称
        :param filename: 保存文件名
        :param keyNum: 字典数
        :param dic: 字典参数
        :return: 失败文件  保存的文件 df
        """
        result = []
        fail_file = []
        for i in os.listdir(path):  # 获取 path 中所有的文件列表
            if f'{fname}' in i:
                file = f"{path}\\{i}"
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.loads(f.read())

                    if keyNum == 1:
                        try:
                            result += data[dic['dic_1']]
                            print(f'{i} read successfully.')
                        except:
                            fail_file.append(i)
                    elif keyNum == 2:
                        try:
                            dicValue = data[dic['dic_1']][dic['dic_2']]

                            dicValue['entryId'] = i.split('.')[0]
                            result += [dicValue]
                            print(f'{i} read successfully.')
                            # if i == '438107198.txt':
                            #     df = pd.DataFrame(result)
                            #     break
                        except:
                            traceback.print_exc()
                            fail_file.append(i)
                    elif keyNum == 31:
                        try:
                            result += data[dic['dic_1']][dic['dic_2']][dic['dic_3']]
                        except:
                            fail_file.append(i)
                    elif keyNum == 32:
                        try:
                            if (len(data[dic['dic_1']][dic['dic_2']]) != 0) and (len(data[dic['dic_1']][dic['dic_3']]) == 0):
                                for d1 in data[dic['dic_1']][dic['dic_2']]:
                                    d1['userId'] = i.split('-')[0]
                                    d1List = [d1]
                                    result += d1List
                                print(f'{i} read successfully.')
                            elif (len(data[dic['dic_1']][dic['dic_2']]) == 0) and (len(data[dic['dic_1']][dic['dic_3']]) != 0):
                                for d2 in data[dic['dic_1']][dic['dic_3']]:
                                    d2['userId'] = i.split('-')[0]
                                    d2List = [d2]
                                    result += d2List
                                print(f'{i} read successfully.')
                            elif (len(data[dic['dic_1']][dic['dic_2']]) != 0) and (len(data[dic['dic_1']][dic['dic_3']]) != 0):
                                for d1 in data[dic['dic_1']][dic['dic_2']]:
                                    d1['userId'] = i.split('-')[0]
                                    d1List = [d1]
                                    result += d1List
                                for d2 in data[dic['dic_1']][dic['dic_3']]:
                                    d2['userId'] = i.split('-')[0]
                                    d2List = [d2]
                                    result += d2List
                                print(f'{i} read successfully.')
                        except:
                            fail_file.append(i)
                except:
                    fail_file.append(i)

        print('---------------------------')
        print(np.unique(np.array(fail_file)))
        df = pd.DataFrame(result)
        # df = pd.concat(result)
        df.to_csv(f'./{filename}.csv', encoding='utf-8-sig', index=False)
        print(f'{filename} csv save successfully.')

        return fail_file, df


    def html2csv(self, path, fname, filename):
        """
        html 文件保存 csv 文件
        :param path: 文件路径
        :param fname: 文件包含名称
        :param filename: 保存文件名
        :return: 失败文件  保存的文件 df
        """
        fail_read = []
        list_dict = []
        for i in os.listdir(path):
            if f'{fname}' in i:
                with open(f'{path}\\{i}', mode='r', encoding='utf-8') as f:
                    html_text = f.read()
                soup = BeautifulSoup(html_text, 'html.parser')

                table = soup.find_all('table')[0]
                trs = table.find_all('tr')[1: ]

                dict_data = {}
                for tr in trs:
                    ths = tr.find_all('th')
                    tds = tr.find_all('td')
                    thsTemp = []
                    for th in ths:
                        thsTemp.append(th.text)
                    thsTemp = ','.join(thsTemp)
                    if ('登录账号' in thsTemp) and ('所属上级' in thsTemp):
                        dict_data['登录账号'] = tds[0].text.replace('\n', '').strip()
                        dict_data['所属上级'] = tds[1].text.replace('\n', '').strip()
                    elif ('会员姓名' in thsTemp) and ('类别/层级' in thsTemp):
                        dict_data['会员姓名'] = tds[0].text.replace('\n', '').strip()
                        dict_data['类别/层级'] = tds[1].text.replace('\n', '').strip()
                    elif ('会员余额' in thsTemp) and ('积分' in thsTemp):
                        dict_data['会员余额'] = tds[0].text.replace('\n', '').strip()
                        dict_data['积分'] = tds[1].text.replace('\n', '').strip()
                    elif ('当前打码量' in thsTemp) and ('出款所需打码' in thsTemp):
                        dict_data['当前打码量'] = tds[0].text.replace('\n', '').strip()
                        dict_data['出款所需打码'] = tds[1].text.replace('\n', '').strip()
                    elif '总打码量' in thsTemp:
                        dict_data['总打码量'] = tds[0].text.replace('\n', '').strip()
                    elif ('银行地址' in thsTemp) and ('银行账号' in thsTemp):
                        dict_data['银行地址'] = tds[0].text.replace('\n', '').strip()
                        dict_data['银行账号'] = tds[1].text.replace('\n', '').strip()
                    elif ('现取银行' in thsTemp) and ('注册时间' in thsTemp):
                        dict_data['现取银行'] = tds[0].text.replace('\n', '').strip()
                        dict_data['注册时间'] = tds[1].text.replace('\n', '').strip()
                    elif ('支付宝账号' in thsTemp) and ('支付宝实名' in thsTemp):
                        dict_data['支付宝账号'] = tds[0].text.replace('\n', '').strip()
                        dict_data['支付宝实名'] = tds[1].text.replace('\n', '').strip()
                    elif 'USDT提款地址' in thsTemp:
                        dict_data['USDT提款地址'] = tds[0].text.replace('\n', '').strip()
                    elif ('GoPay提款地址' in thsTemp) and ('GoPay实名' in thsTemp):
                        dict_data['GoPay提款地址'] = tds[0].text.replace('\n', '').strip()
                        dict_data['GoPay实名'] = tds[1].text.replace('\n', '').strip()
                    elif ('OkPay提款地址' in thsTemp) and ('OkPay实名' in thsTemp):
                        dict_data['OkPay提款地址'] = tds[0].text.replace('\n', '').strip()
                        dict_data['OkPay实名'] = tds[1].text.replace('\n', '').strip()
                    elif ('ToPay提款地址' in thsTemp) and ('ToPay实名' in thsTemp):
                        dict_data['ToPay提款地址'] = tds[0].text.replace('\n', '').strip()
                        dict_data['ToPay实名'] = tds[1].text.replace('\n', '').strip()
                    elif ('VPay提款地址' in thsTemp) and ('VPay实名' in thsTemp):
                        dict_data['VPay提款地址'] = tds[0].text.replace('\n', '').strip()
                        dict_data['VPay实名'] = tds[1].text.replace('\n', '').strip()
                    elif '注册时间' in thsTemp:
                        dict_data['注册时间'] = tds[0].text.replace('\n', '').strip()
                    elif ('注册IP' in thsTemp) and ('注册来源' in thsTemp):
                        dict_data['注册IP'] = tds[0].text.replace('\n', '').strip()
                        dict_data['注册来源'] = tds[1].text.replace('\n', '').strip()
                    elif ('注册系统' in thsTemp) and ('最后登录时间' in thsTemp):
                        dict_data['注册系统'] = tds[0].text.replace('\n', '').strip()
                        dict_data['最后登录时间'] = tds[1].text.replace('\n', '').strip()
                    elif ('电话' in thsTemp) and ('微信号' in thsTemp):
                        dict_data['电话'] = tds[0].text.replace('\n', '').strip()
                        dict_data['微信号'] = tds[1].text.replace('\n', '').strip()
                    elif ('QQ' in thsTemp) and ('邮箱' in thsTemp):
                        dict_data['QQ'] = tds[0].text.replace('\n', '').strip()
                        dict_data['邮箱'] = tds[1].text.replace('\n', '').strip()
                    elif ('总提款次数' in thsTemp) and ('总提款金额' in thsTemp):
                        dict_data['总提款次数'] = tds[0].text.replace('\n', '').strip()
                        dict_data['总提款金额'] = tds[1].text.replace('\n', '').strip()
                    elif ('首次提款' in thsTemp) and ('最高提款' in thsTemp):
                        dict_data['首次提款'] = tds[0].text.replace('\n', '').strip()
                        dict_data['最高提款'] = tds[1].text.replace('\n', '').strip()
                    elif ('当日提款金额' in thsTemp) and ('当日提款次数' in thsTemp):
                        dict_data['当日提款金额'] = tds[0].text.replace('\n', '').strip()
                        dict_data['当日提款次数'] = tds[1].text.replace('\n', '').strip()
                    elif ('总充值次数' in thsTemp) and ('总充值金额' in thsTemp):
                        dict_data['总充值次数'] = tds[0].text.replace('\n', '').strip()
                        dict_data['总充值金额'] = tds[1].text.replace('\n', '').strip()
                    elif ('首次充值' in thsTemp) and ('最高充值' in thsTemp):
                        dict_data['首次充值'] = tds[0].text.replace('\n', '').strip()
                        dict_data['最高充值'] = tds[1].text.replace('\n', '').strip()
                    elif ('当日充值金额' in thsTemp) and ('当日充值次数' in thsTemp):
                        dict_data['首次充值'] = tds[0].text.replace('\n', '').strip()
                        dict_data['最高充值'] = tds[1].text.replace('\n', '').strip()
                    elif '备注' in thsTemp:
                        dict_data['备注'] = tds[0].text.replace('\n', '').strip()
                list_dict += [dict_data]
                print(f'{i} read successfully.')
                # if i == '100278.html':
                #     df = pd.DataFrame(list_dict)
                #     break
            else:
                fail_read.append(i)
        print('---------------------------')
        print(fail_read)
        df = pd.DataFrame(list_dict)
        df.to_csv(f'./original_data/{filename}.csv', encoding='utf-8-sig', index=False)
        print(f'{filename} save successfully.')

        return fail_read, df


    def htmlPd2csv(self, path, fname, filename, **dic):
        """
        pandas to read html
        :param path: 文件路径
        :param fname: 文件包含名
        :param filename: 保存文件名
        :return: fail files  df
        """
        '''
        tables = []
        fail_file = []
        for i in os.listdir(path):
            try:
                if f'{fname}' in i:
                    with open(f'{path}\\{i}', mode='r', encoding='utf-8') as f:
                        data = json.loads(f.read())
                    html_text = pd.read_html(data[dic['dic_1']][dic['dic_2']])
                    table = html_text[0].T
                    # value = table.iloc[1, :].values
                    # value = np.append(value, table.iloc[3, :].values)
                    # # value = table.iloc[1, :]
                    # df.loc[len(df.index)] = value
                    table.columns = table.iloc[0, :]
                    table1 = table.iloc[1, :]
                    table1['名称'] = table.iloc[3, 0]
                    table1['额度'] = table.iloc[3, 1]
                    table1['注册来源'] = table.iloc[3, 2]
                    table1['最后出款时间'] = table.iloc[3, 7]
                    table1['会员层级'] = table.iloc[3, 9]
                    table1['双重验证'] = table.iloc[3, 10]

                    table1 = pd.DataFrame(table1).T

                    table1.columns = ['会员账号', '状态', '新增日期', '注册IP', '最后登入IP', '最后登入时间', '6',
                                      '最后入款时间', '8', '最后下注游戏', '当前使用钱包', '等级', '备注', '13',
                                      '名称', '额度', '注册来源', '最后出款时间', '会员层级', '双重验证']
                    tables.append(table1)
                    print(f'{i} read completely.')
                    # if i == '104397171.txt':
                    #     df = pd.concat(tables)
                    #     break
            except:
                fail_file.append(i)'''
        tables = []
        fail_file = []
        for i in os.listdir(path):
            try:
                if f'{fname}' in i:
                    data = pd.read_html(f'{path}\\{i}')
                    table = data[0]
                    tables.append(table)
                    print(f'{i} read completely.')
                    # if i == '11.html':
                    #     df = pd.concat(tables)
                    #     break
            except:
                fail_file.append(i)


        print('---------------------------')
        print(np.unique(np.array(fail_file)))
        df = pd.concat(tables)
        # df = df.append(tables)
        df.to_csv(f'./original_data/{filename}.csv', encoding='utf-8-sig', index=False)
        print(f'{filename} file save successfully.')

        return fail_file, df


    def txtHtml2csv(self, path, fname, filename, **dic):
        """
        txt 文件中是 html 内容
        :param path: 文件路径
        :param fname: 文件包含名
        :param filename: 保存文件名
        :param dic: 字典参数
        :return: 失败文件
        """
        list_dict = []
        fail_file = []
        for i in os.listdir(path):
            try:
                if f'{fname}' in i:
                    with open(f'{path}\\{i}', mode='r', encoding='utf-8') as f:
                        html_text = json.loads(f.read())
                    soup = BeautifulSoup(html_text[dic['dic_1']][dic['dic_2']], 'html.parser')
                    tds = soup.find_all('td')

                    dict_data = {}
                    dict_data['agentAccount'] = tds[0].text.strip()
                    dict_data['username'] = tds[1].text.strip()
                    dict_data['statu'] = tds[2].text.strip()
                    dict_data['limit'] = tds[3].text.strip()
                    dict_data['newAddDate'] = tds[4].text.strip()
                    dict_data['lastLoginIp'] = tds[5].text.strip()
                    dict_data['lastLoginTime'] = tds[6].text.strip()
                    list_dict.append(dict_data)
                    print(f'{i} read completely.')
            except:
                fail_file.append(i)
                traceback.print_exc()

        print('---------------------------')
        print(f'{fail_file} file read failed.')
        df = pd.DataFrame(list_dict)
        df.to_csv(f'./{filename}.csv', encoding='utf-8-sig', index=False)
        print(f'{filename} file save successfully.')


    def list2csv(self, path, fname, filename, **dic):
        """
        txt 中数据是 list 而不是 dict
        :param path: 文件路径
        :param fname: 文件包含名
        :param filename: 保存文件名
        :param dic: 字典参数
        :return: 失败文件  合并 df
        """
        rowList = []
        fail_file = []
        for i in os.listdir(path):
            try:
                if f'{fname}' in i:
                    with open(f'{path}\\{i}', mode='r', encoding='utf-8') as f:
                        data = json.loads(f.read())

                    d = data[dic['dic_1']]
                    if len(d) == 0:
                        continue
                    else:
                        lenLi = np.arange(len(d[0]))
                        for j in range(len(d)):
                            dic_row = {}
                            for li in lenLi:
                                dic_row[f'{li}'] = d[j][li]
                            rowList.append(dic_row)
                        print(f'{i} read successfully.')
            except:
                fail_file.append(i)

        print('---------------------------')
        print(f'{fail_file} file read failed.')
        df = pd.DataFrame(rowList)
        df.to_csv(f'./handled/{filename}.csv', encoding = 'utf-8-sig', index = False)
        print(f'{filename} file save successfully.')

        return fail_file, df


    def basisHandle(self, data, filename):
        """

        :param data: df
        :param filename: df file name
        :return: handled df
        """
        print(data.shape)

        data.dropna(axis=0, how='all', inplace=True)
        data.dropna(axis=1, how='all', inplace=True)
        data.drop_duplicates(inplace=True)

        cols = data.columns
        for col in cols:
            if data[col].duplicated().sum() == len(data[col]) - 1:
                data.drop(labels = col, axis = 1, inplace = True)

        print(f'{filename} handle successfully.')

        return data


    def split_str(self, val, idx):
        """

        :param data: 数据列
        :return: 分割后的 array
        """
        valSplit = val.split('：')[idx]

        return valSplit


    def timeTransfrom(self, val):


        timeNum = val  # 毫秒时间戳
        timeTemp = float(timeNum / 1000)
        tupTime = time.localtime(timeTemp)
        stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)

        return stadardTime


    def GetUID(self):

        p = etree.HTMLParser()
        fname = '.html'
        path = 'C:\\Users\\admin\\Desktop\\WorkSpace\\am\\am\\user'

        idList = []
        for i in os.listdir(path):  # 获取 path 中所有的文件列表
            if f'{fname}' in i:
                file = f"{path}\\{i}"
                html = etree.parse(f'{file}', p)
                trs = html.xpath("//tr[@class='tr']")
                for tr in trs:
                    idDic = {}
                    temp = [i.strip() for i in tr.xpath(f'//*[@id="tr_{tr.xpath("td//span/@id")[0]}"]/td[5]/a/text()')]
                    idDic['highAcc'] = temp[0]
                    idDic['uid'] = tr.xpath('td//span/@id')[0]
                    idList.append(idDic)

                print(f'{i} read successfully.')

        df = pd.DataFrame(idList)
        df.to_csv('./handled_data/uid.csv', encoding='utf-8-sig', index=False)
        print('uid csv save successfully.')
