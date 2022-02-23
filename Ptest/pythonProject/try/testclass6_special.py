# -*- coding: utf-8 -*-
"""
__new__()
__add__()
# @Date    : 2022年02月22日
# @Author  : Christal
"""


class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__被调用了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('__new_obj被调用了，new_obj的id值为{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__被调用了，id值为{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object这个类对象的id为：', id(object))
print('Person这个类对象的id为：', id(Person))

p = Person('张三', 20)
print('p这个实例对象的id为：', id(p))
