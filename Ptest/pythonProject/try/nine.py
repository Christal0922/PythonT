# -*- coding: utf-8 -*-
"""
输出九九乘法表
# @Date    : 2022年01月19日
# @Author  : Christal
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(j)+'*'+str(i)+'='+str(j*i), end='\t')
    print()

