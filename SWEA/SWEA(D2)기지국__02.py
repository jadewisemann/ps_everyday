mapper = {'A': 1, 'B': 2, 'C': 3}

for tc in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(n)]
    
    houses = {
        (i, j)
        for i in range(n)
        for j in range(n)
        if grid[i][j] == "H"
    }

    for i in range(n):
        for j in range(n):
            if grid[i][j] in 'ABC':
                for k in range(1, mapper[grid[i][j]] + 1):
                    for ni, nj in ((i - k, j), (i + k, j), (i, j - k), (i, j + k)):
                        houses.discard((ni, nj))
    
    print(f'#{tc + 1} {len(houses)}')