import pygame
import random
import sys

# --- 全局常量 ---
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS_START = 10
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
DARK_MODE_BG = (30, 30, 30)
DARK_MODE_SNAKE = (0, 255, 127)
DARK_MODE_FOOD = (255, 99, 71)
SNAKE_COLOR = (0, 102, 0)
FOOD_COLOR = (255, 69, 0)
BLACK = (0, 0, 0)

# 初始化 Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇游戏 🐍")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)

# --- 工具函数 ---
def show_score(score, theme):
    color = WHITE if theme == 'dark' else BLACK
    text = font.render(f"score: {score}", True, color)
    screen.blit(text, [10, 10])

def random_food():
    return [
        random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
    ]

def game_over(score, theme):
    bg_color = DARK_MODE_BG if theme == 'dark' else SKY_BLUE
    text_color = WHITE if theme == 'dark' else BLACK
    screen.fill(bg_color)
    texts = ["game over", f"your score: {score}"]
    for i, line in enumerate(texts):
        text = font.render(line, True, text_color)
        screen.blit(text, [WIDTH // 2 - 80, HEIGHT // 2 - 30 + i * 40])
    pygame.display.update()
    pygame.time.wait(2000)
    main()  # 自动重新开始游戏

# --- 游戏主函数 ---
def main():
    snake = [[100, 100], [80, 100], [60, 100]]
    direction = 'RIGHT'
    food = random_food()
    score = 0
    speed = FPS_START
    paused = False
    theme = 'light'  # 可选：'light' 或 'dark'

    directions = {
        'UP': (0, -BLOCK_SIZE),
        'DOWN': (0, BLOCK_SIZE),
        'LEFT': (-BLOCK_SIZE, 0),
        'RIGHT': (BLOCK_SIZE, 0)
    }

    while True:
        bg_color = DARK_MODE_BG if theme == 'dark' else SKY_BLUE
        snake_color = DARK_MODE_SNAKE if theme == 'dark' else SNAKE_COLOR
        food_color = DARK_MODE_FOOD if theme == 'dark' else FOOD_COLOR

        screen.fill(bg_color)

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_TAB:
                    theme = 'dark' if theme == 'light' else 'light'  # 切换主题

                if not paused:
                    new_direction = direction
                    if event.key == pygame.K_w:
                        new_direction = 'UP'
                    elif event.key == pygame.K_s:
                        new_direction = 'DOWN'
                    elif event.key == pygame.K_a:
                        new_direction = 'LEFT'
                    elif event.key == pygame.K_d:
                        new_direction = 'RIGHT'
                    if directions[new_direction][0] + directions[direction][0] != 0 or \
                       directions[new_direction][1] + directions[direction][1] != 0:
                        direction = new_direction

        if paused:
            text_color = WHITE if theme == 'dark' else BLACK
            pause_text = font.render("Paused (press space to continue)", True, text_color)
            screen.blit(pause_text, [WIDTH // 2 - 100, HEIGHT // 2])
            pygame.display.update()
            clock.tick(5)
            continue

        # 移动蛇头
        dx, dy = directions[direction]
        head = [snake[0][0] + dx, snake[0][1] + dy]
        snake.insert(0, head)

        # 吃食物判断
        if head == food:
            score += 1
            food = random_food()
            speed = min(speed + 0.5, 20)
        else:
            snake.pop()

        # 撞墙/撞自己判断
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake[1:]):
            game_over(score, theme)

        # 绘制蛇和食物
        for block in snake:
            pygame.draw.rect(screen, snake_color, (*block, BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, food_color, (*food, BLOCK_SIZE, BLOCK_SIZE))

        show_score(score, theme)
        pygame.display.update()
        clock.tick(speed)

if __name__ == "__main__":
    main()
