for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    grid = [input().split() for _ in range(n)]
    
    cnt = 0
    
    for row in grid:
        cnt += "".join(row).split('0').count('1' * k)
    
    for j in range(n):
        col_str = "".join(grid[i][j] for i in range(n))
        cnt += col_str.split('0').count('1' * k)

    print(f'#{tc} {cnt}')