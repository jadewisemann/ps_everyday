from collections import deque

n, m = map(qint, input().split())
grp = []
si, sj = 0, 0

for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        si, sj = i, tmp.index(2)
    grp.append(tmp)

vis = [[-1] * m for _ in range(n)]
dq = deque([[si, sj, 0]])
vis[si][sj] = 0

while dq:
    ci, cj, dist = dq.popleft()
    
    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        ni, nj = ci + di, cj + dj
        
        if 0 <= ni < n and 0 <= nj < m:
            if grp[ni][nj] == 1 and vis[ni][nj] == -1:
                vis[ni][nj] = dist + 1
                dq.append([ni, nj, dist + 1])

for i in range(n):
    for j in range(m):
        if grp[i][j] == 0:
            print(0, end=' ')
        else:
            print(vis[i][j], end=' ')
    print()