# -*- coding: utf-8 -*-
"""
if, for, while
# @Date    : 2022年01月19日
# @Author  : Christal
"""
# 中奖判断
# number = eval(input("请输入您的6位中奖号码："))
# # if else
# if number == 987654:
#     print("恭喜您中奖了！")
# else:
#     print("您未中本期大奖")
# 简化形式
number = 987654
result = '恭喜您中奖了!' if number == 987654 else '很遗憾，您未中本期大奖'
print('恭喜您中奖了!' if number == 987654 else '很遗憾，您未中本期大奖')

# 计算1-10的累加和
s = 0
for i in range(1, 11):
    s += i
print(s)

# 计算水仙花数
# 153=1*1*1+5*5*5+3*3*3
for i in range(100, 1000):
    a = i % 10  # 获取个位数字
    b = (i//10) % 10  # 获取十位数字
    c = i//100  # 获取百位数字
    if (a**3+b**3+c**3) == i:
        print(i)



