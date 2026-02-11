for tc in range(int(input())):
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    ii, ij = None, None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '2':
                ii, ij = i, j

    res = 0

    stck = [(ii, ij)]
    vis = set()
    vis.add((ii, ij))
    
    while stck:
        si, sj = stck.pop()
        
        if grid[si][sj] == '3':
            res = 1
            break

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = si + di, sj + dj
            if not (0 <= ni < n and 0 <= nj < n)  or grid[ni][nj] == '1' or (ni, nj) in vis:
                continue
            vis.add((ni, nj))
            stck.append((ni, nj))

    print(f'#{tc + 1} {res}')