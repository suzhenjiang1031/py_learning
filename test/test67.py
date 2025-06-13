# tiny_painter_bot.py

WIDTH = 10
HEIGHT = 5

def create_canvas():
    return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_canvas(canvas):
    print("\n画布：")
    for row in canvas:
        print(''.join(row))
    print()

def move_robot(canvas, position, direction, steps):
    x, y = position
    for _ in range(steps):
        if direction == "UP":
            x = max(0, x - 1)
        elif direction == "DOWN":
            x = min(HEIGHT - 1, x + 1)
        elif direction == "LEFT":
            y = max(0, y - 1)
        elif direction == "RIGHT":
            y = min(WIDTH - 1, y + 1)
        canvas[x][y] = '*'
    return (x, y)

def main():
    canvas = create_canvas()
    position = (HEIGHT // 2, WIDTH // 2)  # 初始在中间
    canvas[position[0]][position[1]] = '*'

    print("🎨 欢迎来到 TinyPainterBot！输入命令：MOVE <方向> <步数>，或 PRINT 查看画布，EXIT 退出。")
    while True:
        cmd = input(">> ").strip().upper()
        if cmd == "EXIT":
            break
        elif cmd == "PRINT":
            print_canvas(canvas)
        elif cmd.startswith("MOVE"):
            parts = cmd.split()
            if len(parts) == 3 and parts[1] in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
                try:
                    steps = int(parts[2])
                    position = move_robot(canvas, position, parts[1], steps)
                except ValueError:
                    print("❌ 无效的步数，请输入整数。")
            else:
                print("❌ 命令格式应为：MOVE <UP|DOWN|LEFT|RIGHT> <步数>")
        else:
            print("❌ 不支持的命令。")

if __name__ == "__main__":
    main()
