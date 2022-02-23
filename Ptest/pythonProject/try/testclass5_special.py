# -*- coding: utf-8 -*-
"""
__add__()
__len__()
# @Date    : 2022年02月22日
# @Author  : Christal
"""


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')

s = stu1 + stu2
print(s)
print(len(stu1))
