from collections import deque
import sys

input = sys.stdin.readline

# get input 
n, m = map(int, input().strip().split())
grid = [
    list(map(int, list(input().strip())))
    for _ in range(n)
]

# loop grid, brute-force
vis = [[False for _ in range(m)] for _ in range(n)]

def get_count_walls(i, j):
    global vis
    q = deque([(i, j)])
    vis[i][j] = True
    cnt, walls = 1, set()

    while q:
        si, sj = q.popleft()

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = si + di, sj + dj

            if not (0 <= ni < n and 0 <= nj < m): continue
            if vis[ni][nj]: continue
            
            if grid[ni][nj] == 0:
                cnt += 1
                vis[ni][nj] = True
                q.append((ni, nj))
            else:
                walls.add((ni, nj))   

    return (cnt, walls)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and not vis[i][j]:            
            cnt, walls = get_count_walls(i, j)
            for wi, wj in walls:
                grid[wi][wj] +=  cnt
            
for i in range(n):
    print("".join(
        str(grid[i][j] % 10 if grid[i][j] > 0 else 0)
        for j in range(m)
    )
)
