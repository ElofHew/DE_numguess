# 注意，已知bug：游戏结束后，无法重新开始游戏，只能退出游戏。
# 2.0版本已修复，请使用2.0版本。

import time, random, sys

print("====================\n"
      "    猜数字小游戏\n"
      "====================\n")
time.sleep(1)
while True:
    print("你今天看上去很聪明 :)")
    print("1 > 进入游戏")
    print("2 > 退出")
    print("0 > 关于")
    start = input("> ")
    if int(start) == 1:
        time.sleep(0.5)
        print("请选择范围：")
        time.sleep(0.2)
        print("1 > 入门(0~50)")
        print("2 > 较少(0~100)")
        print("3 > 正常(0~200)")
        print("4 > 较多(0~500)")
        print("5 > 很多(0~1000)")
        print("0 > 手动选择范围")
        time.sleep(0.2)
        while True:
            diff = input("> ")
            if int(diff) == 1:
                rdm = (random.randint(0, 50))
                frsrt = int(0)
                frend = int(50)
            elif int(diff) == 2:
                rdm = (random.randint(0, 100))
                frsrt = int(0)
                frend = int(100)
            elif int(diff) == 3:
                rdm = (random.randint(0, 200))
                frsrt = int(0)
                frend = int(200)
            elif int(diff) == 4:
                rdm = (random.randint(0, 500))
                frsrt = int(0)
                frend = int(500)
            elif int(diff) == 5:
                rdm = (random.randint(0, 1000))
                frsrt = int(0)
                frend = int(1000)
            elif int(diff) == 0:
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
                            rdm = (random.randint(frsrt, frend))
                            print("当前范围是：", frsrt, "~", frend)
                            time.sleep(0.5)
                            print("即将开始游戏！")
                            break
                    except:
                        print("错误！(输入有误)")
            time.sleep(1)
            print("游戏开始！"
                  "(提示：范围是", frsrt, "~", frend, ")")
            time.sleep(0.5)
            while True:
                try:
                    inn = int(input("请输入你的猜测："))
                    if inn < rdm:
                        print("你猜小了！")
                    elif inn > rdm:
                        print("你猜大了！")
                    elif inn == rdm:
                        print("你猜对了！")
                        print("恭喜你赢得了本次游戏！")
                        time.sleep(2)
                        while True:
                            try:
                                print("\n===结束菜单===")
                                print("1 > 重新开始游戏")
                                print("2 > 退出游戏")
                                rsult = input("> ")
                                if int(rsult) == 1:
                                    time.sleep(1)
                                    continue
                                elif int(rsult) == 2:
                                    print("\n再见！")
                                    print("(程序将在3秒后退出)")
                                    time.sleep(3)
                                    sys.exit()
                                else:
                                    print("你的输入有误！")
                            except ValueError:
                                print("你的输入有误！")
                        break
                    else:
                        print("你的输入有误！")
                        break
                except:
                    print("你的输入有误！")
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
        continue


# 本项目由B站UP主Dan_Evan个人编写
# 我的粉丝交流QQ群：927441490
# 我的B站UID：642688364

# By Dan_Evan