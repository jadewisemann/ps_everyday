mapper = {'A': 1, 'B': 2, 'C': 3}
vis = set()
house = set()
for tc in range(int(input())):
    n = int(input())
    grid = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] in 'ABC':
                for k in range(1, mapper[grid[i][j]] + 1):
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        nx, ny = i + dx * k, j + dy * k
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                        if grid[nx][ny] == 'H' and (nx, ny) not in vis:
                            vis.add((nx, ny))
            elif grid[i][j] == "H" and (i, j) not in house:
                house.add((i, j))                

    print(f'#{tc + 1} {len(house - vis)}')