# -*- coding: utf-8 -*-
"""
绘制随机漫步图
# @Date    : 2022年01月17日
# @Author  : Christal
"""
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# $创建一个RandomWalk实例，并将其包含的点都绘制出来
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=15)
# plt.show()

# 只要程序处于活动状态，就不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    # remove the axes.n
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # 法一
    # plt.xticks([])
    # plt.yticks([])


    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break

