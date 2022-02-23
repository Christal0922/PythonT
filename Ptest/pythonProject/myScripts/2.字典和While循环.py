#!/usr/bin/env python
# coding: utf-8

# # 字典

# ## 键-值对

# In[ ]:


#键-值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

#访问键-值对
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")

#添加键-值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25


# In[ ]:


#先创建一个空字典
alien_0={}
alien_0['color']='green'
alien_0['points'] = 5
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
#删除键-值对
del alien_0['points']
print(alien_0)


# In[ ]:


#多行字典
favorite_languages = {
   'gen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is "+
     favorite_languages['sarah'].title()+".")
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title())

#遍历字典中的所有键
for name in favorite_languages.keys():
    print(name.title())
    
#套用IF语句
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi"+name.title()+", I see your favorite language is "+
             favorite_languages[name].title()+"!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#按顺序遍历字典中的所有键， sorted
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")


# In[ ]:


#遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last':'fermi'
}
for key, value in user_0.items():
    print("\nKey: "+key)
    print("Value: "+value)
    


# In[ ]:


#遍历字典中的所有值
favorite_languages = {
   'gen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#通过对包含重复元素的列表调用set()，可让Python找出列表中独一无二的元素，并使用这些元素来创建一个集合
print("\n")
for language in set(favorite_languages.values()):
    print(language.title())
    


# ## 字典列表

# In[ ]:


#嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# In[ ]:


#创建30个绿色的外星人
aliens = []
for alien_number in range(30):
    new_alien ={'color': 'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: "+str(len(aliens)))
#修改前3个外星人的信息
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print("...")
#elif
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[:5]:
    print(alien)
print("...")


# In[ ]:


##在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese']
}
print("You ordered a "+pizza['crust']+"-crust pizza"+
     "with the following toppings")
for topping in pizza['toppings']:
    print("\t"+topping)


# In[ ]:


#在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}

for username, user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    
    print("\tFull name: "+full_name.title())
    print("\tLocation: "+location.title())


# # 用户输入和While循环

# ## input()

# In[ ]:


message = input("Tell me something, and I will repeat it back to you:")
print(message)


# In[ ]:


name = input("Please enter your name: ")
print("Hello, "+name+"!")

prompt = "If you tell us who you are, we can personalize the mesages you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, "+name+"!")


# In[ ]:


age = input("How old are you? ")
age = int(age)
age >= 18

height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


# ## 求模运算符 %

# In[ ]:


# 将两个数相除并返回余数
# 判断奇偶性
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number"+str(number)+" is even.")
else:
    print("\nThe number"+str(number)+" is odd.")
    


# ## While循环

# In[ ]:


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
    


# In[ ]:


# 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

#不让quit打印出来
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)


# In[ ]:


#使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)


# In[ ]:


# 使用break 退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")
        


# In[ ]:


# 在循环中使用continue,用continue语句，
#不像break语句那样不再执行余下的代码并退出整个循环。例如，来看一个从1数到10，但只打印其中偶数的循环：
# 如果程序陷入无限循环，可按Ctrl + C，也可关闭显示程序输出的终端窗口
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue
    print(current_number)


# ## 使用while循环处理列表和字典

# In[ ]:


# 在列表之间移动元素
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止,将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# In[ ]:


# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# In[ ]:


#使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb?")
    
    responses[name]=response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

#调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name+" would like to climb "+response+".")

