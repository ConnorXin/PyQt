import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView, \
    QHBoxLayout, QVBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtCore import Qt
import pandas as pd
from docxtpl import DocxTemplate
import xlrd
import os
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.window_width, self.window_height = 700, 500
        self.resize(self.window_width, self.window_height)
        self.setWindowTitle('资金查控平台文书生成(河北)')

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.choice_btn = QPushButton('&选择待调单')
        self.choice_btn.clicked.connect(self.load_excel)
        layout.addWidget(self.choice_btn)

        self.gen_btn = QPushButton('&生成文书')
        self.gen_btn.clicked.connect(self.gen_word)
        layout.addWidget(self.gen_btn)

    def load_excel(self):
        fname = QFileDialog.getOpenFileName(self, '选择待调单', "./", "Excel Files (*.xls);;",)
        df = pd.read_excel(fname[0], dtype={"被查账/卡号": str})
        self.work_excel_file = fname[0]
        if df.size == 0:
            return

        df.fillna('', inplace=True)
        self.table.setRowCount(df.shape[0])
        self.table.setColumnCount(df.shape[1])
        self.table.setHorizontalHeaderLabels(df.columns)

        # returns pandas array object
        for row in df.iterrows():
            values = row[1]
            for col_index, value in enumerate(values):
                tableItem = QTableWidgetItem(str(value))
                self.table.setItem(row[0], col_index, tableItem)

        self.table.setColumnWidth(2, 300)

    def gen_word(self):
        df = pd.read_excel(self.work_excel_file, dtype={"被查账/卡号": str})
        workbook = xlrd.open_workbook(self.work_excel_file)
        worksheet = workbook.sheet_by_index(0)
        nrows = worksheet.nrows  # 获取该表总行数
        bankCount = df.groupby('选择银行').agg({'选择银行': 'count'})
        bankCount.columns = ['银行数量']
        bankName = bankCount.index.values
        bankCount.reset_index(inplace=True)

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
                    all_data.append({'账（卡）号': cardNo[0],
                                     '涉案账（卡）号与犯罪活动有何关联': '涉案账（卡）号与犯罪活动有往来转账记录'})
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

        cur_dir = self.work_excel_file.split('/')[: -1]
        curPath = '/'.join(cur_dir)
        # TODO 申请表
        tml_Applyfile = './采取查询手段申请表（新）.docx'
        if not os.path.exists(tml_Applyfile):
            QMessageBox.warning(self, '提示', "找不到模版", QMessageBox.StandardButton.Ok)
            return
        tplApply = DocxTemplate(tml_Applyfile)
        dataApply = {'items': data, 'bankNum': len(bankName), 'accountNum': len(df.iloc[:, 1].values),
                     'addData': addData}

        for idx, d in enumerate([dataApply]):
            context = d
            tplApply.render(context)
            # fname = QFileDialog.getSaveFileName(self, '生成文书', "./", "Word Files (*.docx);;", )
            tplApply.save(f'{curPath}/采取查询手段申请表{idx + 1}.docx')

        # TODO 协查通知书
        tplInform = DocxTemplate('./协助查询财产通知书.docx')
        for data in informData:
            context2 = data
            tplInform.render(context2)
            tplInform.save(f'{curPath}/协助查询财产通知书-{data["bankName"]}.docx')

        # TODO 附件
        tplAddWord = DocxTemplate('./附件.docx')
        for bank in list(bankDic.keys()):
            context3 = {'items': bankDic[bank]}

            tplAddWord.render(context3)
            tplAddWord.save(f'{curPath}/卡号附件-{bank}.docx')

        # TODO 附件总表
        for idx, df in enumerate([all_data]):
            all_df = pd.DataFrame(df)
            all_df.iloc[:, 0] = all_df.iloc[:, 0].astype(str)
            all_df.insert(loc=0, column='序号', value=np.arange(1, len(all_df.iloc[:, 0]) + 1))
            all_df.to_excel(f'{curPath}/待调单总表附件{idx + 1}.xls', index=False, engine='openpyxl')

        QMessageBox.information(self, '提示', "生成完毕", QMessageBox.StandardButton.Ok)


def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':

    main()