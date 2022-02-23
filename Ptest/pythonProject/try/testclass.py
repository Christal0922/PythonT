# -*- coding: utf-8 -*-
"""
定义类和子类
# @Date    : 2022年02月22日
# @Author  : Christal
"""


class Person(object):  # Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))


# 定义子类
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        super().info()
        print('成绩：{0}'.format(self.score))


# 测试
stu = Student('Jack', 20, '1001')
stu.info()
