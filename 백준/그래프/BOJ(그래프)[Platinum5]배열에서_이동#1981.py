from collections import deque

def bfs_with_restriction(n, grid, si, sj, ei, ej, low, high):
    if not(low <= grid[si][sj] <= high):
        return False

    vis = [[False for _ in range(n)] for _ in range(n)]
    q = deque([(si, sj)])
    vis[si][sj] = True
   
    while q:
        ci, cj = q.popleft()
        
        if ci == ei and cj == ej:
            return True

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if not(0 <= ni < n and 0 <= nj < n): continue
            if vis[ni][nj]: continue
            if low <= grid[ni][nj] <= high:
                vis[ni][nj] = True
                q.append((ni, nj))
    
    return False

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

every_number = sorted(list(set([
    num 
    for row in grid
    for num in row 
])))

global_min = float('inf')
l, r = 0, 0
n_every_number = len(every_number)

while l < n_every_number and r < n_every_number:
    l_val, r_val = every_number[l], every_number[r]
    if bfs_with_restriction(n, grid, 0, 0, n-1, n-1, l_val, r_val):
        diff = r_val - l_val
        if diff < global_min:
            global_min = diff
        l += 1
    else:
        r += 1

print(global_min)