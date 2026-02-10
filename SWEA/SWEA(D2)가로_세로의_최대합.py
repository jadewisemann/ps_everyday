for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    rows = [sum(row) for row in grid]
    cols = [sum(col) for col in zip(*grid)]

    print(f'#{tc+1}', max(
        rows[i] + cols[j] - grid[i][j]
        for i in range(n)
        for j in range(n)
    ))
