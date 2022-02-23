# -*- coding: utf-8 -*-
"""
# @Date    : 2022年02月22日
# @Author  : Christal
"""


def get_sum(num):
    s = 0
    for i in range(1, num + 1):
        s += i
    print(f'1到{num}之间的累加和为：{s}')


get_sum(10)
