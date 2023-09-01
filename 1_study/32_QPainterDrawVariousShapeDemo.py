# -*- coding: utf-8 -*-
# @time    : 2023/8/6 9:13
# @author  : w-xin
# @file    : 32_QPainterDrawVariousShapeDemo.py
# @software: PyCharm

"""
QPainter 可以绘制各种图形

弧形
圆形
椭圆
矩阵
多边形
图像
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPainterDrawVariousShapeDemo(QWidget):

    def __init__(self):

        super(QPainterDrawVariousShapeDemo, self).__init__()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('QPainterDrawVariousShape Demo')
        self.resize(600, 600)


    def paintEvent(self, event):

        panter = QPainter(self)
        panter.begin(self)

        # 绘制弧形
        # rect: 绘制矩形的区域 在举行内进行绘制弧形  0, 10: left, top; 100, 100: 宽度高度
        # a - 0: 起始的角度
        # alen - 50 * 16: 结束的角度  1个 alen 等于 1/16 度  比度小
        panter.setPen(Qt.blue)
        panter.drawArc(QRect(0, 20, 100, 100), 0, 50 * 16)

        # 绘制带弦的弧
        # 参数与 drawArc 一样
        panter.drawChord(QRect(160, 20, 100, 100), 12, 130 * 16)

        # 通过弧绘制圆
        panter.setPen(Qt.red)
        panter.drawArc(QRect(160 * 2, 20, 100, 100), 0, 360 * 16)

        # 绘制扇形
        # 参数与弧形差不多
        panter.drawPie(QRect(160 * 3, 20, 100, 100), 0, 90 * 16)

        # 绘制椭圆  宽和高肯定是不一样的  若是一样的就是绘制圆
        panter.drawEllipse(QRect(30, 140, 150, 100))

        # 绘制多边形
        # 绘制五边形 指定5个点
        point1 = QPoint(180, 220)
        point2 = QPoint(200, 300)
        point3 = QPoint(280, 340)
        point4 = QPoint(280, 390)
        point5 = QPoint(180, 430)
        # 创建多边形对象
        polygon = QPolygon([point1, point2, point3, point4, point5])
        panter.drawPolygon(polygon)

        # 绘制图像
        image = QImage('./images_3/book.png')
        # 指定绘制区域 将图片缩小到原来的三分之一
        # 10, 400: 窗口的坐标
        rect = QRect(240, 140, image.width() / 3, image.height() / 3)
        panter.drawImage(rect, image)

        panter.end()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main = QPainterDrawVariousShapeDemo()
    main.show()
    sys.exit(app.exec_())
