# -*- coding: utf-8 -*-
"""
c.__dict__ 输出实例对象的实例字典
C.__mro__ 输出层次结构
# @Date    : 2022年02月22日
# @Author  : Christal
"""

print(dir(object))


class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建C类的实例对象
x = C('Jack', 20)
# print(dir(C)) # 类原有的属性
print('输出实例对象的实例字典'.center(50, '-'))
print(x.__dict__)
print(C.__dict__)
print('{0:-^50}'.format('输出对象所属的类'))
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出C类父类的元组
print(C.__base__)
print(C.__mro__)  # 输出类的层次结构
print(A.__subclasses__())  # 输出A子类的列表
