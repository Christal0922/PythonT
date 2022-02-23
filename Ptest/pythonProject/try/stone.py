# -*- coding: utf-8 -*-
"""
石头剪刀布小游戏
# @Date    : 2022年01月19日
# @Author  : Christal
"""
import random


player_score = 0
computer_score = 0
# 选择玩家角色
print('''
******* 欢迎来到4399游戏平台 *******
    石头     剪刀   布
*********************************
''')
player_name = input('请输入玩家姓名：')
print('1. 貂蝉\t2. 曹操\t3. 诸葛')
choice = eval(input('请选择电脑角色: '))
if choice == 1:
    computer_name = '貂蝉'
elif choice == '2':
    computer_name = '曹操'
elif choice == '3':
    computer_name = '诸葛'
else:
    computer_name = '匿名'
print(player_name, 'VS', computer_name)

while True:
    # 玩家出拳
    player_fist = eval(input('-------请出拳：1. 石头\t2. 剪刀\t3. 布-------\n'))
    if player_fist == 1:
        player_fist_name = '石头'
    elif player_fist == 2:
        player_fist_name = '剪刀'
    elif player_fist == 3:
        player_fist_name = '布'
    else:
        player_fist_name = '石头'
        player_fist = 1
    print(player_name, '玩家出拳：', player_fist_name)

    # 电脑角色出拳
    computer_fist = random.randint(1, 3)
    if computer_fist == 1:
        computer_fist_name = '石头'
    elif computer_fist == 2:
        computer_fist_name = '剪刀'
    else:
        computer_fist_name = '布'
    print(computer_name, '玩家出拳：', computer_fist_name)

    # 判断胜负
    if player_fist == computer_fist:
        print('平局')
    elif (player_fist == 1 and computer_fist == 2) or (player_fist == 2 and computer_fist == 3) or \
            (player_fist == 3 and computer_fist == 1):
        print('玩家： ', player_name, '胜')
        player_score += 1
    else:
        print('电脑： ', computer_name, '胜')
        computer_score += 1
    answer = input('再来一局不？y/n\n')
    if answer == 'n':
        break

print('--------------------------')
print(player_name, player_score)
print(computer_name, computer_score)
print('---------------------------')
if player_score == computer_score:
    print('平局')
elif player_score > computer_score:
    print(player_name, '胜利')
else:
    print(computer_name, '胜利')





