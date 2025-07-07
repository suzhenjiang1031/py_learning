import random
import time

def roll_dice():
    print("掷骰子中...")
    time.sleep(1)
    print(f"🎲 点数是：{random.randint(1,6)}")

# 示例：多次掷骰子
for _ in range(5):
    roll_dice()
