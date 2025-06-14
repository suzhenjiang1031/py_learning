# mbti_test.py

def ask_question(question, option1, option2):
    print(f"\n{question}")
    print(f"1. {option1}")
    print(f"2. {option2}")
    while True:
        choice = input("请输入 1 或 2：")
        if choice in ['1', '2']:
            return int(choice)
        print("⚠️ 输入错误，请重新输入。")

def run_test():
    print("欢迎参加超简版 MBTI 性格测试！请根据你最真实的选择回答：")

    score = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}

    # 一共 8 个问题，每对2个
    score['E'] += ask_question("你更喜欢哪种场景？", "和朋友一起出去玩", "一个人看书刷剧")
    score['I'] += 1 - score['E']

    score['S'] += ask_question("你更关注：", "现在的具体细节", "未来的可能性和想象")
    score['N'] += 1 - score['S']

    score['T'] += ask_question("面对冲突时你更倾向于：", "讲道理分析逻辑", "讲感受关注情绪")
    score['F'] += 1 - score['T']

    score['J'] += ask_question("你计划假期时：", "提前订好所有行程", "走到哪玩到哪")
    score['P'] += 1 - score['J']

    # 判断类型
    personality = ""
    personality += 'E' if score['E'] > score['I'] else 'I'
    personality += 'S' if score['S'] > score['N'] else 'N'
    personality += 'T' if score['T'] > score['F'] else 'F'
    personality += 'J' if score['J'] > score['P'] else 'P'

    print("\n🎉 测试完成！你的性格类型是：", personality)
    descriptions = {
        "INTJ": "战略家：有想法、有计划、有远见。",
        "INFP": "调停者：理想主义，重视内心情感。",
        "ENTP": "辩论家：善于分析，口才好，喜欢挑战观点。",
        "ESFP": "表演者：热情洋溢，爱社交，享受当下。",
        # 可继续补充
    }
    print("性格简述：", descriptions.get(personality, "独特而神秘的你！"))

if __name__ == "__main__":
    run_test()
