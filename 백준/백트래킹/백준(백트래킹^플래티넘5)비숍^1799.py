main_diag = [False] * (10 * 2)
anit_diag = [False] * (10 * 2)

def play_bishop(n, cells, idx, cnt, curr_max):
    # pruning
    if cnt +(len(cells) - idx) <= curr_max:
        return curr_max

    # base condition
    if idx == len(cells):
        return cnt
    
    # main
    r, c = cells[idx]

    if not main_diag[r + c] and not anit_diag[r - c + n]:
        main_diag[r + c], anit_diag[r - c + n] = True, True
        curr_max = play_bishop(n, cells, idx + 1, cnt + 1, curr_max)
        main_diag[r + c], anit_diag[r - c + n] = False, False

    curr_max = play_bishop(n, cells, idx + 1, cnt, curr_max)    

    return curr_max


# get input
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

possible_cells = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j]
]

black_cells  = [
    cell
    for cell in possible_cells
    if not (cell[0] + cell[1]) % 2
]


white_cells  = [
    cell
    for cell in possible_cells
    if (cell[0] + cell[1]) % 2
]

print(
    play_bishop(n, black_cells, 0, 0, 0) +
    play_bishop(n, white_cells, 0, 0, 0)
)
