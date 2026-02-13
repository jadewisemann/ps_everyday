from collections import deque

for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    
    res = 0
    vis = set()

    ii, ij = next(
        (i, j)
        for i in range(n)
        for j in range(n)
        if grid[i][j] == 2
    )

    queue = deque([(ii, ij, 0)])
    while queue:
        si, sj, dist = queue.popleft()

        if grid[si][sj] == 3:
            res = dist - 1
            break

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = si + di, sj + dj
            
            if (
                not (0 <= ni < n and 0 <= nj < n)
                or grid[ni][nj] == 1
                or (ni, nj) in vis
            ):
                continue
            
            queue.append((ni, nj, dist + 1))
            vis.add((ni, nj))

    print(f"#{tc + 1} {res}")