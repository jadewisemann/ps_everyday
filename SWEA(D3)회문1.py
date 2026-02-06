for tc in range(10):
    n = int(input())
    grid = [input() for _ in range(8)]
    cnt = 0

    for i in range(8):
        for j in range(8 - n + 1):
            row_sub = grid[i][j:j + n]
            if row_sub == row_sub[::-1]:
                cnt += 1
            
            col_sub = "".join(grid[j+k][i] for k in range(n))
            if col_sub == col_sub[::-1]:
                cnt  += 1

    print(f'#{tc + 1} {cnt}')