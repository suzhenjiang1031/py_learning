def total_n_queens(n):
    def is_valid(row, col, queens):
        for r, c in enumerate(queens[:row]):
            if c == col:
                return False
            if abs(row - r) == abs(col - c):
                return False
        return True
    
    def backtrack(row, queens):
        nonlocal count
        if row == n:
            count += 1
            return
        for col in range(n):
            if is_valid(row, col, queens):
                queens[row] = col  
                backtrack(row + 1, queens)  
    
    count = 0
    queens = [0] * n 
    backtrack(0, queens) 
    return count

if __name__ == "__main__":
    n = int(input()) 
    print(total_n_queens(n)) 