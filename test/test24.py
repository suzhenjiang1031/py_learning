import random
import time

def typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def math_quiz_game():
    print("\n" + "="*40)
    typing_effect("欢迎来到数学小天才挑战赛！")
    typing_effect("回答5道随机数学题，看看你能得多少分！")
    print("="*40 + "\n")
    
    score = 0
    operations = ['+', '-', '*']
    
    for i in range(5):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        op = random.choice(operations)
        
        if op == '+':
            answer = num1 + num2
        elif op == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2
            
        try:
            typing_effect(f"第{i+1}题: {num1} {op} {num2} = ?")
            user_answer = int(input("你的答案: "))
            
            if user_answer == answer:
                typing_effect("太棒了！正确！+10分！🎉")
                score += 10
            else:
                typing_effect(f"哎呀，错了！正确答案是 {answer}")
                
        except ValueError:
            typing_effect("请输入有效的数字！本题不得分！")
            
        time.sleep(0.5)
        print()
    
    print("="*40)
    typing_effect(f"游戏结束！你的总分是: {score}/50")
    if score == 50:
        typing_effect("完美！你是数学天才！🌟")
    elif score >= 30:
        typing_effect("很不错！继续加油！💪 c")
    else:
        typing_effect("别灰心，多练习你就行！😊")
    print("="*40)

if __name__ == "__main__":
    math_quiz_game()