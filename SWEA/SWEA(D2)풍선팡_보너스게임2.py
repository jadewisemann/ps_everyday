for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc + 1}', 
        max(
            sum(
                grid[i][k] + grid[k][j]
                for k in range(n)
            ) - grid[i]
            for i in range(n)
            for j in range(n)
        )
    )

