import random

subjects = ["量子力学", "能量场", "灵魂", "宇宙", "意识"]
verbs = ["影响", "操控", "连接", "感应", "共振"]
objects = ["脑电波", "心灵", "DNA", "时间", "空间"]

def generate_phrase():
    return f"{random.choice(subjects)}可以{random.choice(verbs)}{random.choice(objects)}。"

for _ in range(5):
    print(generate_phrase())
