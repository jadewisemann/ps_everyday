def solve():
    si, sj, ei, ej  = 0, 0, 0, 0
    grid  = []
    for i in range(16):
        row = list(map(int, list(input())))
        grid.append(row)
        for j in range(16):
            if   row[j] == 2: si, sj = i, j

    vis = [
        [False for _ in range(16)]
        for _ in range(16)
    ]    

    q = [(si, sj)]    
    while q:
        ci, cj  = q.pop()

        if grid[ci][cj] == 3: return 1

        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if (
                not(0 <= ni < 16 and 0 <= nj < 16) or
                vis[ni][nj] or
                grid[ni][nj] == 1
            ): 
                continue
        
            q.append((ni, nj))
            vis[ni][nj] = True
                
if __name__ == "__main__":
    for _ in range(10):
        print(f'#{int(input())} {solve() or 0}')