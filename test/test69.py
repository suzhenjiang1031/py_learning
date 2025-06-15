import random

# 22张主要塔罗牌（大阿尔卡那）
tarot_cards = {
    "The Fool": {
        "upright": "新的开始、自由、冒险",
        "reversed": "鲁莽、天真、不负责任"
    },
    "The Magician": {
        "upright": "创造力、意志力、行动力",
        "reversed": "欺骗、缺乏计划、浪费机会"
    },
    "The High Priestess": {
        "upright": "直觉、潜意识、神秘",
        "reversed": "隐藏秘密、困惑、内心不安"
    },
    "The Empress": {
        "upright": "丰收、爱、母性",
        "reversed": "依赖、浪费、情绪泛滥"
    },
    "The Emperor": {
        "upright": "权力、规则、稳定",
        "reversed": "固执、暴政、控制欲强"
    },
    "The Lovers": {
        "upright": "爱情、选择、和谐",
        "reversed": "分离、诱惑、冲突"
    },
    "The Chariot": {
        "upright": "胜利、掌控、自律",
        "reversed": "失控、阻碍、方向不明"
    },
    "Justice": {
        "upright": "公平、真理、责任",
        "reversed": "不公、欺骗、偏见"
    },
    "The Hermit": {
        "upright": "沉思、自省、孤独",
        "reversed": "疏离、逃避现实"
    },
    "Wheel of Fortune": {
        "upright": "好运、转折、命运",
        "reversed": "厄运、停滞、不稳定"
    },
    "Death": {
        "upright": "结束与重生、转化",
        "reversed": "抗拒改变、停滞、拖延"
    },
    "Temperance": {
        "upright": "平衡、节制、耐心",
        "reversed": "极端、冲动、不协调"
    },
    "The Devil": {
        "upright": "欲望、束缚、诱惑",
        "reversed": "解放、克服成瘾"
    },
    "The Tower": {
        "upright": "突变、瓦解、意外",
        "reversed": "慢性崩塌、恐惧改变"
    },
    "The Star": {
        "upright": "希望、灵感、治愈",
        "reversed": "失望、悲观、幻想破灭"
    },
    "The Moon": {
        "upright": "幻觉、直觉、潜意识",
        "reversed": "焦虑、困惑、隐藏的敌意"
    },
    "The Sun": {
        "upright": "成功、喜悦、正能量",
        "reversed": "傲慢、延迟、虚假乐观"
    },
    "Judgement": {
        "upright": "觉醒、救赎、自我反省",
        "reversed": "逃避审判、自责、犹豫"
    },
    "The World": {
        "upright": "圆满、完成、成就",
        "reversed": "未完成、滞留、未能解脱"
    }
}

def draw_cards(n):
    cards = random.sample(list(tarot_cards.keys()), n)
    result = []
    for card in cards:
        is_upright = random.choice([True, False])
        orientation = "正位" if is_upright else "逆位"
        meaning = tarot_cards[card]["upright" if is_upright else "reversed"]
        result.append((card, orientation, meaning))
    return result

def main():
    print("🔮 欢迎来到塔罗牌占卜室 🔮")
    print("你可以选择抽取 1 ~ 3 张牌来占卜今日运势。\n")

    while True:
        try:
            num = int(input("想抽几张牌？(1-3)，输入0退出："))
            if num == 0:
                print("感谢使用，愿宇宙与你同在 ✨")
                break
            elif 1 <= num <= 3:
                print("\n✨ 你抽到的牌是：\n")
                drawn = draw_cards(num)
                for card, orientation, meaning in drawn:
                    print(f"🃏 {card} ({orientation})：{meaning}")
                print("\n" + "-"*40 + "\n")
            else:
                print("⚠️ 请输入 1 到 3 之间的数字。")
        except ValueError:
            print("⚠️ 输入无效，请输入数字。")

if __name__ == "__main__":
    main()
