grid = [list(map(int, input().strip())) for _ in range(9)]

row_used = [[False] * 10 for _ in range(9)]
col_used = [[False] * 10 for _ in range(9)]
sect_used = [[False] * 10 for _ in range(9)]

cand =  []

for i in range(9):
    for j in range(9):
        num = grid[i][j]
        s = (i // 3) * 3 + (j // 3)
        if num != 0:
            row_used[i][num] = True
            col_used[j][num] = True
            sect_used[s][num] = True
        else:
            cand.append((i, j, s))

def solve_sudoku(cand_idx, grid, cand):
    if cand_idx == len(cand):
        return True
    
    x, y, s = cand[cand_idx]

    for number in range(1, 10):
        if row_used[x][number] or col_used[y][number] or sect_used[s][number]:
            continue

        grid[x][y] = number
        row_used[x][number] = col_used[y][number] = sect_used[s][number] = True

        if solve_sudoku(cand_idx + 1, grid, cand):
            return True
        
        grid[x][y] = 0
        row_used[x][number] = col_used[y][number] = sect_used[s][number] = False

    return False


if solve_sudoku(0, grid, cand):
    for row in grid:
        print("".join(map(str, row)))
