for tc in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(n)]
    
    houses = {
    (i, j)
        for i in range(n)
        for j in range(n)
        if grid[i][j] == "H"
    }

    [
        houses.discard((i + k * di, j + k * dj))
        for i in range(n) for j in range(n) if grid[i][j] in 'ABC'    
        for k in range(1, {'A': 1, 'B': 2, 'C': 3}[grid[i][j]] + 1)
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1))
    ]

    print(f'#{tc + 1} {len(houses)}')