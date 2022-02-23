#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#print的应用
print("Hello Python world")


# In[ ]:


#赋值
message = "Hello Python world"
print(message)


# In[ ]:


#字符串
#修改大小写
name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())


# In[ ]:


#合并字符串
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name
print(full_name)
print("Hello,"+full_name.title()+"!")


# In[ ]:


#制表符\t, 换行符\n
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# In[ ]:


#删除单次末尾空白-暂时
favorite_language=' python '
favorite_language.rstrip()

#永久删除空白
favorite_language=favorite_language.rstrip()
#删除开头、末尾或均删除
print(favorite_language.rstrip())
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()


# In[ ]:


#str（）将数字型变成字符型
age=23
message="Happy "+str(age)+"rd Birthday!"
print(message)


# In[ ]:


#Python 之禅
import this


# In[ ]:


#列表,索引从0而不是1开始，最后一个索引为-1
bicycles=['trek','cannondale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])


# In[ ]:


#修改列表元素
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)


# In[ ]:


#在列表中添加元素,append----
motorcycles=['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)


# In[ ]:


#创建空列表
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)


# In[ ]:


#在列表中插入元素，insert()
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)


# In[ ]:


#从列表中删除元素，poppop()可删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类
motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print(motorcycles)

#从列表中删除列表末尾元素，pop，列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素
motorcycles=['honda','yamaha','suzuki']
poped_motorcycle=motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)
#pop提供位置索引，删除任何位置的元素
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print("The first motorcycle I owned was a "+first_owned.title()+".")

#根据值删除元素，remove 
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
#remove 2
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive='ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me")


# In[ ]:


#排序
#利用sort对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #正序
cars.sort(reverse=True)#倒序
print(cars)
#利用sorted进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))

#倒着打印列表,永久性改变, reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)


# In[ ]:


#确定列表的长度 len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)


# In[ ]:


#for 循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
#更多操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick")


# In[ ]:


#创建数值列表， range(),函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）
for value in range(1,5):
    print(value)

#list()将range函数的值直接转换成列表
numbers=list(range(1,6))
print(numbers)

#range()函数指定步长，如打印1-10内的偶数
even_numbers=list(range(2,11,2))
print(even_numbers)

#创建前10个整数1-10的平方
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
#法2
squares=[value**2 for value in range(1,11)]


# In[ ]:


#对数字列表进行简单计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)


# In[ ]:


#列表包含1-10的立方
tests=[value**3 for value in range(1,11)]
print(tests)
tests=[]
#法二
for value in range(1,11):
    test=value**3
    tests.append(test)
print(tests)


# In[ ]:


#切片，元素提取
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])#没有指定开头索引，自动从列表开头开始
print(players[2:])#没有指定结尾索引，自动从列表结尾
print(players[-3:])#输出最后三位
#复制列表,[:]
players = ['charles', 'martina', 'michael', 'florence', 'eli']
my_players=players[:]

players.append('michale')
my_players.append('chris')
print(players,my_players)


# In[ ]:


#元组，不可修改的元素
#定义元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
#修改元组变量，虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions=(400,100)


# In[ ]:


#if语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
        

#if else
age=17
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18")
    
#if-elif-else 
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $40.")
#法2
age=12
if age<4:
    price=0
elif age<19:
    price=5
else:
    price=10
print("Your admission cost is $"+str(price)+".")


# In[ ]:


#检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
#循环 in+for
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding "+requested_topping+".")
print("Finished making your pizza!\n")

#in+for+if
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding "+requested_topping+".")
print("Finished making your pizza!\n")

#确保列表不为空
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
        print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")
    
#使用两个或多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry, we don't have"+requested_topping+".")


# In[ ]:


#字典，键，值
alien_0 = {'color':'green','points':5}
alien_0['color']
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!\n")
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#创建空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
print("The alien is "+alien_0['color']+'.')
alien_0['color']='yellow'
print("The alien is now "+alien_0['color']+'.\n')

#移动外星人的例子
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
#新位置=老位置+增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position: " + str(alien_0['x_position'])+".\n")
    


# In[ ]:


#删除键—值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


# In[ ]:


#由类似对象组成的字典
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("Sarah's favortite language is "+
     favorite_languages['sarah'].title()+
     ".")


# In[ ]:




