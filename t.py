from collections import deque
from itertools import permutations

n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

starting_points = []
for _ in range(k):
    ri, ci = map(int, input().split())
    starting_points.append((ri, ci))

stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))

cases = permutations(stones, m)

global_max = 0
for (ii, ij) in starting_points:
    for case in cases:
        local_max = 0
        vis = [[-1] * n for _ in range(n)]
        vis[ii][ij] = 0
        queue = deque([(ii, ij)])
        
        while queue:
            si, sj = queue.popleft()
            
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = si + di, sj + dj

                if not (0 <= ni < n and 0 <= nj < n): continue 
                if vis[ni][nj] != -1: continue
                if grid[ni][nj] == 1 and (ni, nj) not in case: continue

                queue.append((ni, nj))
                vis[ni][nj] = vis[si][sj] + 1
                if vis[ni][nj] > local_max:
                    local_max = vis[ni][nj]

        print(vis)
        if local_max > global_max:
            global_max = local_max

print(local_max)
