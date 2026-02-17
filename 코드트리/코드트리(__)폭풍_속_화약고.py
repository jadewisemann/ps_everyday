
def slide(grid, turn):
    rotate_90 = lambda grid: [list(row) for row in zip(*grid[::-1])]
    slide_left = lambda row: ([x for x in row if x!= 0] + [0] * row.count(0))

    temp_grid = grid
    rot_cnt = {0: 1, 1: 0, 2: 3, 3: 2}[turn % 4]

    for _ in range(rot_cnt):
        temp_grid = rotate_90(temp_grid)
    
    temp_grid = [slide_left(row) for row in temp_grid]

    for _ in range((4 - rot_cnt) % 4):
        temp_grid = rotate_90(temp_grid)
    
    return temp_grid


def fire(grid, n, turn, curr_line):
    direction = turn % 4

    if direction == 0:
        for i in range(n):
            if grid[i][curr_line] > 0:
                return i, curr_line
    elif direction == 1:
        for j in range(n - 1, -1, -1):
            if grid[curr_line][j] > 0:
                return curr_line, j
    elif direction == 2:
        for i in range(n - 1, -1, -1):
            if grid[i][curr_line] > 0:
                return i, curr_line
    elif direction == 3:
        for j in range(n):
            if grid[curr_line][j] > 0:
                return curr_line, j

    return None

from collections import deque

def explode(grid, ii, ij, n):
    if grid[ii][ij] == 0: return

    que = deque([(ii, ij, grid[ii][ij])])
    bombed = set([(ii, ij)])

    while que:
        si, sj, v = que.popleft()

        if v <= 1: continue

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            for dist in range(1, v):
                ni, nj = si + di * dist, sj + dj * dist

                if not(0 <= ni < n and 0 <= nj < n): break
                if grid[ni][nj] == 0: continue
                if (ni, nj) in bombed: continue
                
                bombed.add((ni, nj))
                que.append((ni, nj, grid[ni][nj]))

    for i, j in bombed:
        grid[i][j] = 0


def simulate(grid, n, turn, curr_line):
    grid = slide(grid, turn)
    target = fire(grid, n, turn, curr_line)
    if target:
        explode(grid, target[0], target[1], n)
    
    grid = slide(grid, turn)
    return grid


def solve(turn, curr_grid, k, n):
    global ans
    
    count = 0
    for r in range(n):
        for c in range(n):
            if curr_grid[r][c] > 0:
                count += 1

    if turn == k:
        ans = min(ans, count)
        return
    
    if count == 0:
        ans = 0
        return
    
    if ans == 0: return

    for i in range(n):
        next_grid = simulate([row[:] for row in curr_grid], n, turn, i)
        solve(turn + 1, next_grid, k, n)


k, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')

solve(0, grid, k, n)

print(ans)

