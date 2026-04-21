
tank = {'^': 'U', 'v': 'D', '<': 'L', '>': 'R'}
move = {'U': (-1, 0, '^'), 'D': (1, 0, 'v'), 'L': (0, -1, '<'), 'R': (0, 1, '>')}

for tc in range(int(input())):
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    input()
    
    ci, cj = next(
        (i, j)
        for i in range(h)
        for j in range(w)
        if grid[i][j] in tank
    )
    d = tank[grid[ci][cj]]

    for op in input():
        if op == 'S':
            di, dj, _ = move[d]
            for k in range(1, h+w):
                ni, nj = ci + di * k, cj + dj * k
                
                if not (0 <= ni < h and 0 <= nj < w) or grid[ni][nj] == '#':
                    break
                
                if grid[ni][nj] == '*':
                    grid[ni][nj] = '.'
                    break
        else:
            d = op
            di, dj, shape = move[d]
            grid[ci][cj] = shape
            ni, nj = ci + di, cj + dj
            
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == '.': 
                grid[ci][cj], grid[ni][nj] = '.', shape
                ci, cj = ni, nj
         
    print(f"#{tc + 1}", end=" ")
    for row in grid:
        print("".join(row))