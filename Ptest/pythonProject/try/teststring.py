# -*- coding: utf-8 -*-
"""
# @Date    : 2022年01月18日
# @Author  : Christal
"""
# 字符串索引
s = "HELLOWORLD"
print(s[0], s[-1])
# 正向递增序列，不包括最后一个
print(s[2:7])
# 逆向递增序列
print(s[-8:-3])
print(s[2:])

# 字符串拼接
x = '2022年'
y = '北京冬奥会'
print(x+y)

# 字符串的内容输出10次
print(10*x)

# 判断‘北京' 是否在y字符串中
print('北京' in y)

# eval()函数
# eval()函数去掉字符串s最外侧的引号
s = '3.14+3'
print(s, type(s))
x = eval(s)
print(x, type(x))

# eval()与input()联用
age = eval(input('请输入您的年龄：'))
print(age, type(age))

