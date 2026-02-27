for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    
    si, sj = 99, 0
    for j in range(100):
        if grid[99][j] == 2:
            sj = j
            break

    dirs = [(0, -1), (0, 1), (-1, 0)] 
    
    while True:
        if si == 0:
            break

        for di, dj in dirs:
            ni, nj = si + di, sj + dj
            
            if 0 <= ni < 100 and 0 <= nj < 100 and grid[ni][nj] == 1:
                grid[si][sj] = 0 
                si, sj = ni, nj
                break
                
    res = sj
    print(f'#{tc} {res}')