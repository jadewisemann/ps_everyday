
for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    areas = [
        (ni - i + 1) * (nj - j + 1)
        for i in range(n) for j in range(n)
        for ni in range(i, n) for nj in range(j, n)
        if grid[ni][nj] == grid[i][j]
    ]

    print(f'#{tc + 1} {areas.count(max(areas))}')