from collections import deque

n, m = map(int, input().split())
grid = [input() for _ in range(m)]

vis = [[False for _ in range(n)] for _ in range(m)]

bans, wans = 0, 0
for i in range(m):
    for j in range(n):
        if vis[i][j]: continue

        cnt = 0
        q = deque([(i, j)])
        curr = grid[i][j]
        vis[i][j] = True
        
        while q:
            ci, cj = q.popleft()
            cnt += 1

            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ni, nj = ci + di, cj + dj
            
                if not(0 <= ni < m and 0 <= nj < n): continue
                if vis[ni][nj]: continue
                if grid[ni][nj] != curr: continue
                q.append((ni, nj))
                vis[ni][nj] = True

        if curr == "B":
            bans += cnt ** 2
        else:
            wans += cnt ** 2

print(wans, bans)