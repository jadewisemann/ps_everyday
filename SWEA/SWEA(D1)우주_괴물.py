for tc in range(int(input())):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    zero_cnt = 0
    si, sj = 0, 0 
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                si, sj = i, j
            elif grid[i][j] == 0:
                zero_cnt += 1
    
    attacked_cnt = 0
    for di, dj in ((0, 1), (0, -1),(1, 0), (-1, 0)):
        k = 1
        while k < n:
            ni, nj = si + di * k, sj + dj * k

            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                break

            if grid[ni][nj] == 1:
                break

            if grid[ni][nj] == 0:
                attacked_cnt += 1

            k += 1

    print(f'#{tc + 1} {zero_cnt - attacked_cnt}')