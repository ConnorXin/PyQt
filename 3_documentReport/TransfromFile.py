# -*- coding: utf-8 -*-
# @Author  :  connor
# @Time    :  2023/8/3 17:14
# @File    :  TransfromFile.py
# @IDE     :  PyCharm

"""
批量生成文件
"""
from docxtpl import DocxTemplate
import xlrd
import pandas as pd
import numpy as np



if __name__ == '__main__':

    file = "./待调单-1.xls"
    pd.set_option('display.float_format', lambda x: '%.2f' % x)
    df = pd.read_excel(file, dtype={"被查帐/卡号": str})
    workbook = xlrd.open_workbook(file)  # 文件路径
    worksheet = workbook.sheet_by_index(0)  # 索引读取 打开第一个 sheet
    nrows = worksheet.nrows  # 获取该表总行数
    bankCount = df.groupby('选择银行').agg({'选择银行': 'count'})
    bankCount.columns = ['银行数量']
    bankName = bankCount.index.values
    bankCount.reset_index(inplace = True)


    data = []
    addData = []
    informData = []
    all_data = []
    bankDic = {}
    flag = 1
    for i in range(len(bankName)):
        df_temp = df[df.iloc[:, 2] == bankName[i]]
        accountCount = len(df_temp.index)
        if accountCount <= 10:
            cardNo = df_temp.iloc[:, 1].values
            if accountCount == 1:
                data.append({'no': i + 1, 'bankName': bankName[i], 'cardNo': cardNo[0]})
                informData.append({'bankName': bankName[i], 'cardNo': cardNo[0]})
                all_data.append({'账（卡）号': cardNo[0], '涉案账（卡）号与犯罪活动有何关联': '涉案账（卡）号与犯罪活动有往来转账记录'})
            else:
                cardNoStr = ','.join(cardNo)
                data.append({'no': i + 1, 'bankName': bankName[i], 'cardNo': cardNoStr})
                informData.append({'bankName': bankName[i], 'cardNo': cardNoStr})
                for card in cardNo:
                    all_data.append({'账（卡）号': card,
                                     '涉案账（卡）号与犯罪活动有何关联': '涉案账（卡）号与犯罪活动有往来转账记录'})
        else:
            data.append({'no': i + 1, 'bankName': bankName[i],
                         'cardNo': f"{df_temp.iloc[:, 1].values[0]}等{accountCount}个涉案账户，详见相关账户表"})
            informData.append({'bankName': bankName[i],
                               'cardNo': f"{df_temp.iloc[:, 1].values[0]}等{accountCount}个，详见附件"})
            k = 0
            addDataInform = []
            for card in df_temp.iloc[:, 1].values:
                cordType = df_temp.iloc[:, 0].values[k]

                addData.append({'no': flag, 'cardNo': card, 'remark': '涉案账（卡）号与犯罪活动有往来转账记录'})

                addDataInform.append({'no': flag, 'type': cordType, 'cardNo': card, 'bankName': bankName[i],
                                      'locType': '账户及交易明细', 'timeLabel': '开户至今'})
                k += 1
                flag += 1
                all_data.append({'账（卡）号': card,
                                 '涉案账（卡）号与犯罪活动有何关联': '涉案账（卡）号与犯罪活动有往来转账记录'})
            flag = 1
            bankDic[f'{bankName[i]}'] = addDataInform


    data.append({'bankNum': len(data[0].keys()), 'accountNum': len(df.iloc[:, 1].values)})

    # TODO 申请表
    dataApply = {'items': data, 'bankNum': len(bankName), 'accountNum': len(df.iloc[:, 1].values),
                'addData': addData}
    tpl = DocxTemplate('./原表格/采取查询手段申请表（新）.docx')
    for idx, d in enumerate([dataApply]):

        context = d
        tpl.render(context)
        tpl.save(f'./采取查询手段申请表{idx + 1}.docx')


    # TODO 协查通知书

    tpl2 = DocxTemplate('./原表格/协助查询财产通知书.docx')
    for data in informData:

        context2 = data
        tpl2.render(context2)
        tpl2.save(f'./协助查询财产通知书-{data["bankName"]}.docx')


    # TODO 附件
    tpl3 = DocxTemplate('./原表格/附件.docx')

    for bank in list(bankDic.keys()):
        context3= {'items': bankDic[bank]}

        tpl3.render(context3)
        tpl3.save(f'./卡号附件-{bank}.docx')

    # TODO 附件总表
    for idx, df in enumerate([all_data]):

        all_df = pd.DataFrame(df)
        all_df.iloc[:, 0] = all_df.iloc[:, 0].astype(str)
        all_df.insert(loc = 0, column = '序号', value = np.arange(1, len(all_df.iloc[:, 0]) + 1))
        all_df.to_excel(f'待调单总表附件{idx + 1}.xls', index=False, engine='openpyxl')

