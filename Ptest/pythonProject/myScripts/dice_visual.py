# -*- coding: utf-8 -*-
"""
同时掷2个骰子
# @Date    : 2022年01月17日
# @Author  : Christal
"""
from die import Die
import pygal

# 创建2个D6骰子
die1 = Die()
die2 = Die(10)

# 掷骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die1.roll()+die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
# hist.x_labels = range(2, 13)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('./Fig/dice_visual2.svg')

