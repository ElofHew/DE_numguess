print("====================\n"
      "猜数字小游戏\n"
      "====================\n")
import time
time.sleep(2)
start = input("你准备好开始了吗？\n"
              "是的 = 1 , 没有 = 2\n")
if int(start) == 1:
    time.sleep(1)
    print("正在获取一个数字……")
    import random
    rdm = (random.randint(0, 100))
    time.sleep(2)
    print("游戏开始！"
          "(提示：范围0~100)")
    time.sleep(1)
    while rdm <= 100:
        inn = int(input("请输入你的猜测："))
        if inn < rdm:
            print("你猜小了！")
        elif inn > rdm:
            print("你猜大了！")
        elif inn == rdm:
            print("你猜对了！")
            print("恭喜你赢得了本次游戏！")
            print("(程序将在10秒后退出)")
            time.sleep(10)
            break
        else:
            print("你的输入有误！")
elif int(start) == 2:
    print("再见！")
    print("(程序将在10秒后退出)")
    time.sleep(10)
else:
    print("你的输入有误！")
    print("(程序将在10秒后退出)")
    time.sleep(10)

# 本项目由B站UP主Dan_Evan个人编写，本人新手不喜勿喷
# 有问题或改进可以向我提出，本人会积极采纳各位的观点（前提是我会[doge]）

# 我的粉丝交流群：927441490    我的B站UID：642688364

# By Dan_Evan