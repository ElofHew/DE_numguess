# Number Guessing Game v2.2
# By Dan_Evan
# Helped by MeltIce
# 2025.01.01

# v2.0版本更新内容：
# 1. 增加了手动选择范围的功能
# 2. 增加了重新游戏功能
# 3. 优化了游戏逻辑
# 4. 添加了游戏提示信息
# 5. 添加了游戏结束菜单

# v2.1版本更新内容：
# 1. 优化了游戏节奏
# 2. 优化了报错提示信息
# 3. 解决了很多不正常操作导致的报错

# v2.2版本更新内容：
# 1. 修复已知BUG
# 2. 优化了游戏提示信息
# 3. 整合游戏代码块

import random
import time
import sys

def display_menu():
    print("\n请选择范围：")
    time.sleep(0.2)
    print("1 > 入门(0~50)")
    print("2 > 较少(0~100)")
    print("3 > 正常(0~200)")
    print("4 > 较多(0~500)")
    print("5 > 很多(0~1000)")
    print("0 > 手动选择范围")
    time.sleep(0.2)

def choose_difficulty(diff):
    if diff == 1:
        return random.randint(0, 50), 0, 50
    elif diff == 2:
        return random.randint(0, 100), 0, 100
    elif diff == 3:
        return random.randint(0, 200), 0, 200
    elif diff == 4:
        return random.randint(0, 500), 0, 500
    elif diff == 5:
        return random.randint(0, 1000), 0, 1000
    else:
        return None, None, None

def get_manual_range():
    while True:
        try:
            frsrt = int(input("请输入范围最小数字："))
            frend = int(input("请输入范围最大数字："))
            if frsrt > frend:
                print("错误！(最小数不能大于最大数)")
                continue
            elif frsrt == frend:
                print("错误！(最小数不能等于最大数)")
                continue
            else:
                return frsrt, frend
        except ValueError:
            print("错误！(输入有误)")
            continue

def play_game(rdm, frsrt, frend):
    print("游戏开始！(提示：范围是", frsrt, "~", frend, ")")
    time.sleep(0.5)
    while True:
        try:
            inn = int(input("> "))
            if inn < rdm:
                print("你猜小了！")
            elif inn > rdm:
                print("你猜大了！")
            elif inn == rdm:
                print("你猜对了！")
                print("恭喜你赢得了本次游戏！")
                time.sleep(0.5)
                return True
        except ValueError:
            print("你的输入有误！")

def end_game_menu():
    while True:
        try:
            print("\n===结束菜单===")
            print("1 > 重新开始游戏")
            print("2 > 退出游戏")
            rsult = int(input("> "))
            if rsult == 1:
                time.sleep(0.5)
                return True
            elif rsult == 2:
                print("\n再见！")
                print("(程序将在3秒后退出)")
                time.sleep(3)
                sys.exit()
            else:
                print("你的输入有误！")
        except ValueError:
            print("你的输入有误！")

def start_game():
    while True:
        display_menu()
        while True:
            try:
                diff = int(input("> "))
                if diff == 0:
                    frsrt, frend = get_manual_range()
                    rdm = random.randint(frsrt, frend)
                    print("当前范围是：", frsrt, "~", frend)
                    time.sleep(0.5)
                else:
                    rdm, frsrt, frend = choose_difficulty(diff)
                    if rdm is None:
                        print("你的输入有误！")
                        continue

                if play_game(rdm, frsrt, frend):
                    if end_game_menu():
                        break
            except ValueError:
                print("你的输入有误！")



print("====================\n"
      "    猜数字小游戏\n"
      "====================\n"
      "作者主站：https://www.drevan.xyz\n"
      "新年快乐！更新时间：2025-01-01\n")
time.sleep(0.5)
while True:
    try:
        print("你今天看上去很聪明 :)")
        print("1 > 进入游戏")
        print("2 > 退出")
        print("0 > 关于")
        start = input("> ")
        if int(start) == 1:
            start_game()
        elif int(start) == 2:
            print("\n再见！")
            print("(程序将在5秒后退出)")
            time.sleep(5)
            break
        elif int(start) == 0:
            print("本项目由B站UP主Dan_Evan个人编写\n"
                  "(这个py项目十分没有技术含量)\n"
                  "(并且堆满了石山代码……)\n"
                  "(初学者请大佬见谅！)\n"
                  "我的粉丝交流群：927441490\n"
                  "我的B站UID：642688364\n")
            input("(按回车退出) > ")
            print("\n")
        else:
            print("你的输入有误！")
    except ValueError:
        print("你的输入有误！") 



# 有bug或改进可以向我提出，本人会积极采纳各位的观点（前提是我会[doge]）

# 本项目由B站UP主Dan_Evan个人编写
# 欢迎关注我的B站(UID：642688364)
# (这个py项目十分没有技术含量)
# (并且堆满了石山代码……)
# (初学者请大佬见谅！)
# 我的粉丝交流QQ群：927441490
# 我的QQ：2352235176

# By Dan_Evan
# Helped by MeltIce