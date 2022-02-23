# -*- coding: utf-8 -*-
"""
这是阿拉斯加锡特卡2018年1月5日的天气数据，其中包含当天的最高气温和最低气温
# @Date    : 2022年01月17日
# @Author  : Christal
"""
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = './input/death_valley_2018_simple.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)

# 从文件中获取NAME
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("Daily high and low temperatures-2018\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
# plt.savefig('./Fig/weather.png', bbox_inches='tight')
plt.show()
