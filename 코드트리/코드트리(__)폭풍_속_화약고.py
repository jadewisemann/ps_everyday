
def slide(grid, turn, n):
    curr_dir = turn % 4
    new_grid = [[0] * n for _ in range(n)]

    if curr_dir == 0:
        for j in range(n):
            temp = [grid[i][j] for i in range(n) if grid[i][j] != 0]
            for i in range(len(temp)):
                new_grid[n - len(temp) + i][j] = temp[i]

    elif curr_dir == 1:
        for i in range(n):
            temp = [el for el in grid[i] if el != 0 ]
            for j in range(len(temp)):
                new_grid[i][j] = temp[j]

    elif curr_dir == 2:
        for j in range(n):
            temp = [grid[i][j] for i in range(n) if grid[i][j] != 0]
            for i in range(len(temp)):
                new_grid[i][j] = temp[i]

    elif curr_dir == 3:
        for i in range(n):
            temp = [el for el in grid[i] if el != 0 ]
            for j in range(len(temp)):
                new_grid[i][n - len(temp) + j] = temp[j]

    return new_grid


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
    grid = slide(grid, turn, n)
    target = fire(grid, n, turn, curr_line)
    if target:
        explode(grid, target[0], target[1], n)
    
    grid = slide(grid, turn, n)
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

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = float('inf')

solve(0, grid, k, n)

print(ans)

