#!/usr/bin/env python
# coding: utf-8

# # 函数

# ## 定义函数

# In[ ]:


# 问候
def greet_user(username):
    print("Hello, "+username.title()+"!")

greet_user('jesse')

# pets
def describe_pet(animal_type,pet_name):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is '"+pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet('dog','willie')


# In[ ]:


# 默认值
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is '"+pet_name.title()+".")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')


# ## 返回值

# In[ ]:


# 返回简单值，返回全名
def get_formatted_name(first_name, last_name):
    full_name=first_name+" "+last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)


# In[ ]:


# 中间名可选
def get_formatted_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name=first_name+" "+middle_name+" "+last_name
    else:
        full_name=first_name+" "+last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)
    


# In[ ]:


# 返回字典
def build_person(first_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)

# 字典中加入可选形参age
def build_person(first_name,last_name,age=""):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person

musician = build_person('jimi','hendrix',age = 27)
print(musician)


# In[ ]:


# 结合使用函数和while循环
def get_formatted_name(first_name,last_name,middle_name):
    if middle_name == 'no':
        full_name=first_name+" "+last_name
    else:
        full_name=first_name+" "+middle_name+" "+last_name 
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("enter 'q'at any time to quit")
    first_name=input("first name:")
    if first_name == 'q':
        break
    middle_name=input("Please input your middle name or type no")
    if middle_name == 'q':
        break
    last_name=input("last name")
    if last_name == 'q':
        break
    full_name = get_formatted_name(first_name,last_name,middle_name)
    print("Hello, "+full_name.title()+"!")


# In[ ]:


# 传递列表
def greet_users(names):
    for name in names:
        message = "Hello, "+name.title()+"!"
        print(message)
usernames = ['hannah','ty','margot']
greet_users(usernames)


# In[ ]:


# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


# In[ ]:


# 禁止函数修改列表，可选用列表的副本[:]
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: "+current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []
print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)


# In[ ]:


# 传递任何数量的实参,形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

# 将print语句替换为一个循环，对配料列表遍历
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print("- "+topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


# In[ ]:


# 结合使用位置实参和任意数量实参, 如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+
         "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')


# In[ ]:


# 创建一个字典，其中包含我们知道的有关用户的一切
def build_profile(first,last,**user_info):
    profile = {}
    profile['first name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',
                            location='princeton',
                            field='physics')
print(user_profile)


# ## import py文件中的函数

# In[ ]:


import pizza2
pizza2.make_pizza(16,'pepperoni')
pizza2.make_pizza(12,'mushrooms','green peppers','extra cheese')


# In[ ]:


from pizza2 import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


# In[ ]:


# 使用as给函数指定别名
from pizza2 import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')


# In[ ]:


# 使用as给模块指定别名
import pizza2 as p
from pizza2 import make_pizza
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')


# In[ ]:


# 导入模块中的所有函数,使用星号（*）运算符可让Python导入模块中的所有函数
from pizza2 import *
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')


# ## 函数编写指南

# ```
# def function_name(parameter_0,parameter_1='default value')
# function_name(value_0,parameter_1='value')
# ```

# # 类

# ## 创建和使用类

# In[ ]:


# 创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title()+" is now sitting")
    
    def roll_over(self):
        print(self.name.title()+" rolled over!")
my_dog = Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")


# In[ ]:


class Car():
  """docstring for Car"""
  def __init__(self, make,model,year):
    self.make = make
    self.model = model
    self.year = year
  def get_descriptive_name(self):
    long_name = str(self.year)+' '+self.make+' '+self.model
    return long_name.title()
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())


# In[ ]:


# 给属性设置默认值
class Car():
  """docstring for Car"""
  def __init__(self, make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  def get_descriptive_name(self):
    long_name = str(self.year)+' '+self.make+' '+self.model
    return long_name.title()
  def read_odometer(self):
    print("This car has "+str(self.odometer_reading)+" miles on it")
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()  


# ## 修改属性的值

# In[ ]:


# 直接修改属性的值
import car
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# In[ ]:


# 通过方法修改属性的值
class Car():
  """docstring for Car"""
  def __init__(self, make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  def get_descriptive_name(self):
    long_name = str(self.year)+' '+self.make+' '+self.model
    return long_name.title()
  def read_odometer(self):
    print("This car has "+str(self.odometer_reading)+" miles on it")
  def update_odometer(self,mileage):
    self.odometer_reading = mileage

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()


# In[ ]:


# 通过方法对属性的值进行递增
class Car():
  """docstring for Car"""
  def __init__(self, make,model,year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  def get_descriptive_name(self):
    long_name = str(self.year)+' '+self.make+' '+self.model
    return long_name.title()
  def read_odometer(self):
    print("This car has "+str(self.odometer_reading)+" miles on it")
  def update_odometer(self,mileage):
    self.odometer_reading = mileage
  def increment_odometer(self,miles):
    self.odometer_reading += miles

my_used_car = Car('subaru','outback',2013)
print(my_new_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# ## 继承

# In[ ]:


# 添加子类-电动车
import car
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())


# In[ ]:


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-KWh battery")
my_tesla = ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# ## 导入类

# In[ ]:


from car import Car

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# In[ ]:


from car2 import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# In[ ]:


from car2 import Car, ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())


# In[ ]:


import car2
my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())


# In[ ]:


from collections import OrderedDict
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")

