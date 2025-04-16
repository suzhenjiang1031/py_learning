def solve_n_queens(n):
    solutions = []
    board = [['.'] * n for _ in range(n)]
    cols = set()
    diag1 = set()  
    diag2 = set()  

    def backtrack(r):
        if r == n:
            solutions.append([' '.join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            board[r][c] = 'Q'
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            board[r][c] = '.'
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)

    if not solutions:
        print("None")
    else:
        for i, sol in enumerate(solutions):
            for row in sol:
                print(row)
            if i != len(solutions) - 1:
                print()

n = int(input("请输入 n："))
solve_n_queens(n)
print("程序执行完毕")
