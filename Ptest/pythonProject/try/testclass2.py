# -*- coding: utf-8 -*-
"""
方法重写
# @Date    : 2022年02月22日
# @Author  : Christal
"""


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}\n年龄：{1}'.format(self.name, self.age))

    def __str__(self):
        return '我的名字是{0},今年{1}岁'.format(self.name, self.age)


stu1 = Student('张三', 20)
o = object()
print(dir(o))
print(dir(stu1))
print(stu1)
print(o)
