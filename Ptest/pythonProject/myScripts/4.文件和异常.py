#!/usr/bin/env python
# coding: utf-8

# # 文件

# ## 读取文件

# In[ ]:


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

    #消除空行
    print(contents.rstrip())


# In[ ]:


# file path
file_path = 'E:\PythonT\myscript\Test\ehmatthes\chapter_10\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# In[ ]:


with open('ehmatthes\chapter_10\pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())


# In[ ]:


# 逐行读取
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        


# In[ ]:


# 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print(lines)


# In[ ]:


# 使用文件的内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))


# In[ ]:


# 包含一百万位的大型文件
file_path='ehmatthes\chapter_10\pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52]+"...")
print(len(pi_string))


# In[ ]:


# 圆周率中有你的生日吗？
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi！")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# ## 写入文件

# In[ ]:


# ，调用open()时提供了两个实参（见Ø）。第一个实参也是要打开的文件的名称；
# 第二个实参（'w'）告诉Python，我们要以写入模式打开这个文件。打开文件时，可指定读取模
# 式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")


# In[ ]:


# 写入多行
filename = 'programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


# In[ ]:


# 附加到文件
filename = 'programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a brower.\n")
    


# # 异常

# ## try-except模块

# In[ ]:


# ZeroDivisionError
# 如果try代码块中的代码运行起来没有问题，Python将跳过except代码块；如果try代码块中的代码导致了错误，Python将查找
# 这样的except代码块，并运行其中的代码，即其中指定的错误与引发的错误相同
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# In[ ]:


# FileNotFoundError
# 字符串前面加r，禁止字符串转义
try:
    with open(r'ehmatthes\chapter_10\alice.txt','rb') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = "Sorry, the file does not exist. "
    print(message)
else:
    words = contents.split()
    num_words = len(words)
    print("The file has about "+str(num_words)+" words.")


# In[ ]:


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename,encoding='UTF-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file does not exist")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file has about "+str(num_words)+"words.")
filename = r'ehmatthes\chapter_10\alice.txt'
count_words(filename)

# 计算循环
filenames = [r'ehmatthes\chapter_10\alice.txt',
             r'ehmatthes\chapter_10\siddhartha.txt',
             r'ehmatthes\chapter_10\moby_dick.txt',
            r'ehmatthes\chapter_10\little_women.txt']
for filename in filenames:
    count_words(filename)


# # 存储数据

# ## json.dump()

# In[ ]:


import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)


# In[ ]:


import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)


# ## 保存和读取用户生成的数据

# In[ ]:


# remember_me.py
import json
username = input("What's your name? ")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remmeber you wehn you come back, "+
         username+"!")


# In[ ]:


# greet_user.py
import json
filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, "+username+"!")


# In[ ]:


import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back!")
else:
    print("Welcome back, "+username+"!")


# In[ ]:


import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
def greet_user():
    """问候用户，并指出其名字"""
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you come back!")
    else:
        print("Welcome back, "+username+"!")
greet_user()


# In[ ]:


import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
def get_stored_username():
    """如果用户存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back!")
greet_user()


# # 测试代码

# ## 测试函数

# In[ ]:


import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

suite = unittest.TestSuite()
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    runner.run(suite)


# In[ ]:


class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self, new_response):
        """存储单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答案"""
        print("Survey results: ")
        for response in self.responses:
            print('- '+response)
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# 显示问题并存储答案
my_survey.show_question()
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
# 显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

