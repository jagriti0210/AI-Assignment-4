import copy

puzzle = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],

    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],

    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9],
]

def print_grid(grid, title):
    print(f"\n{title}")
    print("+" + "-------+" * 3)
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("+" + "-------+" * 3)
        row_display = "| "
        for j in range(9):
            cell = grid[i][j]
            row_display += ("." if cell == 0 else str(cell)) + " "
            if (j + 1) % 3 == 0:
                row_display += "| "
        print(row_display)
    print("+" + "-------+" * 3)

def is_valid(grid, row, col, num):
    if num in grid[row]:
        return False

    column = [grid[r][col] for r in range(9)]
    if num in column:
        return False

    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3
    for r in range(box_start_row, box_start_row + 3):
        for c in range(box_start_col, box_start_col + 3):
            if grid[r][c] == num:
                return False

    return True

def find_empty_cell(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return None

def solve(grid):
    empty = find_empty_cell(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if solve(grid):
                return True

            grid[row][col] = 0

    return False

print("=" * 35)
print("  Sudoku Solver (CSP Backtracking)")
print("=" * 35)

print_grid(puzzle, "Puzzle (. = empty):")

solution = copy.deepcopy(puzzle)

if solve(solution):
    print_grid(solution, "Solution:")
    print("\nSudoku solved successfully!")
else:
    print("\nNo solution exists for this puzzle.")