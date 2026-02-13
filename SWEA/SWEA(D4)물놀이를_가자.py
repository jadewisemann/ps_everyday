from collections import deque

for tc in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]
    
    dist = [[-1] * m for _ in range(n)]

    queue = deque([])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "W":
                queue.append((i, j))
                dist[i][j] = 0
    
    while queue:
        si, sj = queue.popleft()

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = si + di, sj + dj

            if (
                not (0 <= ni < n and 0 <= nj < m)
                or dist[ni][nj] != -1
            ):
                continue
             
            dist[ni][nj] = dist[si][sj] + 1
            queue.append((ni, nj))

    res = sum(
        sum(row)
        for row in dist
    )
    print(f'#{tc + 1} {res}')