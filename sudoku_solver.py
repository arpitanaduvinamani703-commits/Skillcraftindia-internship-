def print_grid(grid):
    for row in grid:
        print(row)

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, row, col, num):
    # Row check
    if num in grid[row]:
        return False
    
    # Column check
    for i in range(9):
        if grid[i][col] == num:
            return False
    
    # 3x3 box check
    box_x = (row // 3) * 3
    box_y = (col // 3) * 3
    
    for i in range(box_x, box_x + 3):
        for j in range(box_y, box_y + 3):
            if grid[i][j] == num:
                return False
    
    return True

def solve(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    
    row, col = empty
    
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True
            
            grid[row][col] = 0
    
    return False


# Example Sudoku Input (0 means empty)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve(grid):
    print("Solved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists")
