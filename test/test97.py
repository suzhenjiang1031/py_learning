import random
import curses

s = curses.initscr()
curses.curs_set(0)
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
win.timeout(100)

snk_x = 30
snk_y = 10
snake = [[snk_y, snk_x]]
food = [random.randint(1, 18), random.randint(1, 58)]
win.addch(food[0], food[1], '*')

key = curses.KEY_RIGHT

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        head[0] += 1
    elif key == curses.KEY_UP:
        head[0] -= 1
    elif key == curses.KEY_LEFT:
        head[1] -= 1
    elif key == curses.KEY_RIGHT:
        head[1] += 1

    snake.insert(0, head)

    if head == food:
        food = None
        while food is None:
            nf = [random.randint(1, 18), random.randint(1, 58)]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    if (head[0] in [0, 19] or head[1] in [0, 59] or head in snake[1:]):
        curses.endwin()
        quit()

    win.addch(head[0], head[1], '#')
