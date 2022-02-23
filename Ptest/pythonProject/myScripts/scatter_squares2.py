# -*- coding: utf-8 -*-
"""
# @Date    : 2022年01月06日
# @Author  : Christal
"""
import matplotlib.pyplot as plt

# 输入特定的x,y
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values,y_values, s=100)

# 输入计算的值
x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# c设置数据点颜色，edgecolors设置轮廓颜色
# c,c='red', 你还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量
# c, 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 自动保存图表
plt.savefig('E:\\PythonT\\Ptest\\pythonProject\\myScripts\\Fig\\squares_plot.png', bbox_inches='tight')
# 显示图表
plt.show()
