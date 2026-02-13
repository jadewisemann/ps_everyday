def solve(grid, n, curr_col, mask, memo):
    if (curr_col, mask) in memo:
        return memo[(curr_col, mask)] 
    
    if curr_col == n:
        return 0
    
    memo[(curr_col, mask)] = min(
        grid[row][curr_col] + solve(grid, n, curr_col + 1, mask | (1 << row), memo)
        for row in range(n)
        if not (mask & (1 << row))
    )

    return memo[(curr_col, mask)]

for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    print(f'#{tc + 1} {solve(grid, n, 0, 0, {})}')