responses = {
    "你好": "你好呀！",
    "你是谁": "我是一个简单的机器人。",
    "再见": "再见，祝你愉快！"
}

while True:
    user_input = input("你说：")
    if user_input in responses:
        print("机器人：", responses[user_input])
    else:
        print("机器人：我不太明白你说什么。")
