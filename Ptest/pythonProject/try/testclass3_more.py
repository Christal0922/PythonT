# -*- coding: utf-8 -*-
"""
多态
# @Date    : 2022年02月22日
# @Author  : Christal
"""


class Animal(object):
    def eat(self):
        print('动物都要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃肉')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


def fun(obj):
    obj.eat()


fun(Dog())
fun(Cat())
fun(Person())
