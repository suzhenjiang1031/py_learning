import random
import os
import time

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def generate_board(size=4):
    total_pairs = (size * size) // 2
    symbols = [chr(65+i) for i in range(total_pairs)] * 2  # 如：['A', 'B', 'C', 'D', ...]
    random.shuffle(symbols)
    board = [symbols[i*size:(i+1)*size] for i in range(size)]
    return board

def display_board(board, revealed):
    print("\n🧠 记忆力训练游戏 - 当前状态：\n")
    size = len(board)
    print("   " + " ".join([f"{i}" for i in range(size)]))
    for i in range(size):
        row = []
        for j in range(size):
            if revealed[i][j]:
                row.append(board[i][j])
            else:
                row.append("*")
        print(f"{i}  " + " ".join(row))
    print()

def get_coords(prompt, size):
    while True:
        try:
            coords = input(prompt).strip().split(",")
            if len(coords) != 2:
                raise ValueError
            x, y = map(int, coords)
            if 0 <= x < size and 0 <= y < size:
                return x, y
        except ValueError:
            print("⚠️ 输入格式应为：行,列  比如 0,1")

def memory_game():
    size = 4  # 可改为6或更多
    board = generate_board(size)
    revealed = [[False]*size for _ in range(size)]
    matched = 0
    total_pairs = (size * size) // 2

    while matched < total_pairs:
        clear_screen()
        display_board(board, revealed)

        print("请选择第一张牌 (格式如 0,1)：")
        x1, y1 = get_coords(">> ", size)
        if revealed[x1][y1]:
            print("⚠️ 这张牌已经被揭示了！")
            time.sleep(1)
            continue

        revealed[x1][y1] = True
        clear_screen()
        display_board(board, revealed)

        print("请选择第二张牌 (格式如 0,1)：")
        x2, y2 = get_coords(">> ", size)
        if revealed[x2][y2] or (x1 == x2 and y1 == y2):
            print("⚠️ 不可以选择相同或已揭示的牌")
            revealed[x1][y1] = False
            time.sleep(1)
            continue

        revealed[x2][y2] = True
        clear_screen()
        display_board(board, revealed)

        if board[x1][y1] == board[x2][y2]:
            print("🎉 配对成功！")
            matched += 1
        else:
            print("❌ 不匹配，再试一次！")
            time.sleep(1.5)
            revealed[x1][y1] = False
            revealed[x2][y2] = False

    print("🏆 恭喜你，全部配对完成！训练完成！")

if __name__ == "__main__":
    memory_game()
