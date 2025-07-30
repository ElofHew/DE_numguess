"""
@Name: DE_numguess
@Author: ElofHew
@Date: 2025-07-30
@Version: 3.0
@License: MIT
@Description: A simple number guessing game.
"""

import os
import sys
import time
import json
import random

__about__ = """
DE Number Guessing Game
(c) 2025 Oak Studio
(c) 2024~2025 ElofHew
GitHub Repo:
https://github.com/ElofHew/DE_numguess
My Bilibili:
https://space.bilibili.com/642688364
"""

__help__ = """
DE Number Guessing Game Help
 = Boot from Arguments:
 + -h : Show help.
 + -a : Show about.
 + -g : Start game.
 = Item meaning:
 + Player : Your name.
 + Range : 0 ~ ? (default 100)
 + Times : Times of a round of game. (default 50)
 + Score : The Score from the last game.
"""

# 功能函数
def clear_screen():
    """清屏"""
    os.system("clear" if os.name != "nt" else "cls")

# 游戏运行需要的函数
def end_menu():
    """游戏结束菜单"""
    print("Do you want to play again? (y/n)")
    while True:
        choice = input("> ")
        if choice.lower() == "y":
            return 0
        elif choice.lower() == "n":
            print("Goodbye!")
            return 1
        else:
            print("Invalid input. Please enter (y/n)")

def game_main(gplayer, gtimes, grange):
    """游戏主函数"""
    rdm = random.randint(0, grange)
    print(f"{gplayer}, Good luck!")
    print(f"Guess a number between 0 and {grange} in {gtimes} times:" if gtimes > 0 else f"Guess a number between 0 and {grange} (Unlimited times):")
    game_times = 0
    while game_times < gtimes if gtimes > 0 else True:
        try:
            print("----------")
            guess = int(input("> "))
            if guess == rdm:
                print("You win!")
                break
            elif 0 <= guess < rdm:
                print("Smaller.")
            elif rdm < guess <= grange:
                print("Bigger.")
            else:
                raise ValueError
            game_times += 1
            if gtimes > 0 and game_times != gtimes:
                print(f"{gtimes - game_times} times left.")
        except ValueError:
            print(f"Invalid input. (0 ~ {grange}).")
    print("--------------------")
    if game_times == gtimes:
        print(f"Game over. The number was {rdm}.")
    end_score = int(100 - (game_times / gtimes * 100)) if gtimes > 0 and game_times < gtimes else 0
    print(f"Your score is {end_score if gtimes > 0 else '0 (Unlimited times cannot be scored)'}.")
    if os.getcwd() == os.path.dirname(os.path.realpath(__file__)):
        config_data, _ = load_config()
        config_data["score"] = end_score
        game_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(game_path, "config.json"), "w") as f:
            json.dump(config_data, f)
    return end_score

def load_config():
    """加载配置文件"""
    game_path = os.path.dirname(os.path.realpath(__file__))
    if os.getcwd() == game_path:
        config_file_path = os.path.join(game_path, "config.json")
        if not os.path.exists(config_file_path):
            config_data = {"player": None, "range": 100, "times": 50, "score": 0}
            with open(config_file_path, "w") as f:
                json.dump(config_data, f)
        with open(config_file_path, "r") as f:
            config_data = json.load(f)
        json_ready = True
    else:
        print("WARNING: Working directory not correct. Using default values.")
        config_data = {"player": "Player", "range": 100, "times": 50, "score": 0}
        json_ready = False
    return config_data, json_ready

def check_json():
    """检查配置文件"""
    config_data, json_ready = load_config()
    json_player = config_data.get("player", None)
    json_times = config_data.get("times", 50)
    json_range = config_data.get("range", 100)
    json_score = config_data.get("score", 0)

    if not json_ready:
        return json_player, json_times, json_range, json_score

    if json_player is None:
        while True:
            new_json_player = str(input("Please enter your name: "))
            if new_json_player == "":
                print("Invalid input. Please enter a name.")
                continue
            else:
                break
    else:
        new_json_player = json_player

    print("========================================")
    print("         Config a Round of Game         ")
    print(" (Enter for skip, otherwise for change) ")
    print("----------------------------------------")

    while True:
        print("Would you like to change the times of a game?")
        set_times = input(f"(Current: {json_times if json_times != 0 else '0 (Unlimited)'}) > ")
        if set_times == "":
            new_json_times = json_times
            break
        try:
            set_times = int(set_times)
            if set_times < 0:
                print("Invalid input. Please enter a positive number.")
                continue
            new_json_times = set_times
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        print("Would you like to change the range of a game?")
        set_range = input(f"(Current: {json_range}) > ")
        if set_range == "":
            new_json_range = json_range
            break
        try:
            set_range = int(set_range)
            if set_range < 0:
                print("Invalid input. Please enter a positive number.")
                continue
            new_json_range = set_range
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_json_score = json_score

    new_config_data = {
        "player": new_json_player,
        "range": new_json_range,
        "times": new_json_times,
        "score": new_json_score,
    }
    game_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(game_path, "config.json"), "w") as f:
        json.dump(new_config_data, f)

    return new_json_player, new_json_times, new_json_range, new_json_score

def game_ready():
    """游戏准备"""
    gplayer, gtimes, grange, gscore = check_json()
    clear_screen()
    print(f"Welcome {gplayer}!")
    if gscore:
        print(f"Last score is {gscore}.")
    print(f"Game will start in 2s...")
    time.sleep(2)
    return gplayer, gtimes, grange

def game_in():
    """游戏入口"""
    try:
        while True:
            clear_screen()
            gplayer, gtimes, grange = game_ready()
            clear_screen()
            game_main(gplayer, gtimes, grange)
            result = end_menu()
            if result == 1:
                return 1
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(1)

def help():
    """帮助"""
    print(__help__)
    input("Press any key to continue...")

def about():
    """关于"""
    print(__about__)
    input("Press any key to continue...")

def main():
    """主函数"""
    while True:
        clear_screen()
        print("=========================")
        print(" DE Number Guessing Game ")
        print("=========================")
        print(" 1. Start game")
        print(" 2. About")
        print(" 3. Help")
        print(" 0. Exit")
        print("-------------------------")
        try:
            choice = int(input("> "))
            if choice == 1:
                if game_in() == 1:
                    sys.exit(0)
            elif choice == 2:
                about()
            elif choice == 3:
                help()
            elif choice == 0:
                print("Goodbye!")
                sys.exit(0)
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter 1/2/3/0.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(1)

if __name__ == "__main__":
    # 处理命令行参数
    if sys.argv[1:]:
        if sys.argv[1] == "-h":
            help()
        elif sys.argv[1] == "-a":
            about()
        elif sys.argv[1] == "-g":
            game_in()
        else:
            print("Invalid argument. Please enter -h/-a/-g.")
    else:
        # 主程序
        main()
